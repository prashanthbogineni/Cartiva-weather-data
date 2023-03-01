import os
import sys
import csv
import asyncio
import functools
import traceback
from datetime import datetime
import concurrent.futures
from sqlalchemy import create_engine
import contextlib
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()
sys.path.append(os.getcwd())

from models.weather_data_table import WeatherData

# setup database
engine = create_engine("sqlite:///weather_data.db")


@contextlib.contextmanager
def get_session(cleanup=False):
    session = Session(bind=engine)
    Base.metadata.create_all(engine)

    try:
        yield session
    except Exception:
        print("---------------------")
        session.rollback()
    finally:
        session.close()

    if cleanup:
        Base.metadata.drop_all(engine)


@contextlib.contextmanager
def get_conn(cleanup=False):
    conn = engine.connect()
    Base.metadata.create_all(engine)

    yield conn
    conn.close()

    if cleanup:
        Base.metadata.drop_all(engine)


async def process_file(run, loop, file_name, cleanup=True):
    with open(os.path.join("data_ingestion/wx_data", file_name), "r") as f:
        print(file_name)
        reader = csv.reader(f, delimiter="\t")
        async with asyncio.Lock():

            with get_session(cleanup) as session:
                session.add_all(
                    [
                        WeatherData(
                            date=datetime.strptime(row[0], "%Y%m%d").date(),
                            max_temp=int(row[1]),
                            min_temp=int(row[2]),
                            precipitation=int(row[3]),
                        )
                        for i, row in enumerate(reader) 
                    ]
                )
                session.commit()


def load_files(file_names):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=500)
    loop = asyncio.new_event_loop()
    run = functools.partial(loop.run_in_executor, executor)
    asyncio.set_event_loop(loop)

    print(f"download started at : {datetime.now().time()}")
    try:
        loop.run_until_complete(
            asyncio.gather(
                *[process_file(run, loop, file_name) for file_name in file_names]
            )
        )
    except Exception:
        print(traceback.format_exc())
        loop.close()
        print("failed due to unknown reasons. Please retry again")
    finally:
        with get_session() as session:
            print(f"Number of records ingested: {session.query(WeatherData).count()}")
            loop.close()


if __name__ == "__main__":
    start_time = datetime.now()
    print(f"Ingestion started at {start_time}")
    file_names = [
        f
        for f in os.listdir("data_ingestion/wx_data")
        if os.path.isfile(os.path.join("data_ingestion/wx_data", f))
    ]
    print("Number of files discovered : ", len(file_names))
    load_files(file_names)


end_time = datetime.now()
print(f"Ingestion ended at {end_time}")
print(f"Duration: {end_time - start_time}")
