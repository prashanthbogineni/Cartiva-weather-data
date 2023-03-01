from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class WeatherStatistics(Base):
    __tablename__ = "weather_statistics"
    id = Column(Integer, primary_key=True)
    station_id = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    avg_max_temp = Column(Float)
    avg_min_temp = Column(Float)
    total_precipitation = Column(Float)


engine = create_engine("sqlite:///weather_data.db")
Base.metadata.create_all(engine)
