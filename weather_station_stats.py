from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from model import WeatherData, WeatherStatistics, Base
engine = create_engine('sqlite:///weather_data.db')
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(WeatherData).filter(WeatherData.max_temp != -9999, WeatherData.min_temp != -9999, WeatherData.precipitation != -9999)
df = pd.read_sql(query.statement, query.session.bind)
df['year'] = pd.DatetimeIndex(df['date']).year


stats = df.groupby(['year', 'station_id']).agg({
    'max_temp': 'mean',
    'min_temp': 'mean',
    'precipitation': 'sum'
})
stats = stats.reset_index()
stats['max_temp'] = stats['max_temp'] / 10
stats['min_temp'] = stats['min_temp'] / 10
stats['precipitation'] = stats['precipitation'] / 10

for index, row in stats.iterrows():
    weather_statistics = WeatherStatistics(
        station_id=row['station_id'],
        year=row['year'],
        avg_max_temp=row['max_temp'],
        avg_min_temp=row['min_temp'],
        total_precipitation=row['precipitation']
    )
    session.add(weather_statistics)
session.commit()