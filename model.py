from sqlalchemy import create_engine, Column, Integer, Float, Date, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    station_id = Column(Integer)
    date = Column(Date)
    max_temp = Column(Integer)
    min_temp = Column(Integer)
    precipitation = Column(Float)
    __table_args__ = (UniqueConstraint('date', 'max_temp', 'min_temp', 'precipitation', name='unique_val_uc'),)

class WeatherStatistics(Base): 
    __tablename__ = 'weather_statistics' 
    id = Column(Integer, primary_key=True) 
    station_id = Column(Integer, nullable=False) 
    year = Column(Integer, nullable=False) 
    avg_max_temp = Column(Float) 
    avg_min_temp = Column(Float) 
    total_precipitation = Column(Float)

engine = create_engine('sqlite:///weather_data.db')
Base.metadata.create_all(engine)