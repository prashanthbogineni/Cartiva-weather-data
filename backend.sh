#!bin/bash


echo "Data Modelling"
python models/weather_data_table.py
python models/weather_statisitics_table.py
echo "------------------------------------------------"

echo "Data Ingestion"
python data_ingestion/ingest_data.py
echo "------------------------------------------------"

echo "Data Analysis"
python data_analysis/weather_station_stats.py
echo "------------------------------------------------"

echo "Rest API"
cd backend_app
python -m flask run