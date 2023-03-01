from sqlalchemy import create_engine, Column, Integer, Float, Date, UniqueConstraint
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class WeatherData(Base):
    __tablename__ = "weather_data"
    id = Column(Integer, primary_key=True)
    station_id = Column(Integer)
    date = Column(Date)
    max_temp = Column(Integer)
    min_temp = Column(Integer)
    precipitation = Column(Float)
    __table_args__ = (
        UniqueConstraint(
            "date", "max_temp", "min_temp", "precipitation", name="unique_val_uc"
        ),
    )


engine = create_engine("sqlite:///weather_data.db")
Base.metadata.create_all(engine)
