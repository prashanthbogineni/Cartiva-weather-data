import os
import csv
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from model import WeatherData, Base

# setup database
engine = create_engine('sqlite:///weather_data.db')
Session = sessionmaker(bind=engine)
session = Session()

# get all files in wx_data directory
files = [f for f in os.listdir('wx_data') if os.path.isfile(os.path.join('wx_data', f))]

def process_file(file):
    with open(os.path.join('wx_data', file), 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for i, row in enumerate(reader):
            date = datetime.strptime(row[0], '%Y%m%d').date()
            max_temp = int(row[1])
            min_temp = int(row[2])
            precipitation = int(row[3])
            try:
                weather_data = WeatherData(date=date, max_temp=max_temp, min_temp=min_temp, precipitation=precipitation)
                session.add(weather_data)
                session.commit()
            except IntegrityError:
                session.rollback()

start_time = datetime.now()
print(f"Ingestion started at {start_time}")

for file in [files[0]]:
    process_file(file)

end_time = datetime.now()
print(f"Ingestion ended at {end_time}")
print(f"Duration: {end_time - start_time}")
print(f"Number of records ingested: {session.query(WeatherData).count()}")

session.close()
