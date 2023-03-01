# CORTEVA-WEATHER-DATA

Tech: python + Flask + Pandas + pytest

This is a REST API service developed using Flask.

* REST api's would be exposed as per defined in doc : https://github.com/corteva/code-challenge-template
* Data Ingestion  which is a combination of Transformation + Loading would be performed as a prescript activity.


## initial Set up 

Configure Virtual Environment in IDE : 

    If linux/Mac :
         python3 -m venv env
    
    If Windows : 
        python -m venv env

A folder **env** will be created.To Activate Virtual Environment : 

    if Linux/Mac:
        
        source env/bin/activate

    if Windows:

        env/Scripts/activate


Install the requirements : 

    pip install -r requirements.txt


# Getting Started

## To Run the Project 

- To Run the Project as a whole :
 - Run `source entrypoint.sh` on Linux or `sh entrypoint.sh` on git bash on windows

  Note: While running Project as a whole `Initiate Setup can be skipped`

- To Run individual files
 - Run `source models.sh` on Linux or `sh models.sh` on git bash on windows
 - Run `source data_ingestion.sh` on Linux or `sh data_ingestion.sh` on git bash on windows
 - Run `source data_analysis.sh` on Linux or `sh data_analysis.sh` on git bash on windows
 - Run `source backend.sh` on Linux or `sh backend.sh` on git bash on windows

- To Run Tests :
 - Run `source test.sh` on Linux or `sh test.sh` on git bash on windows

- To Stop the Application :
  - Press ctrl+c or cmd+c to stop the application
  

## Data Modeling

 * `SQLAlchemy` has been used to model the data here.
 * Tables are created in local sqlite `weatrher_data.db` database 


## Data Ingestion

 * Weather data can be injected into the data model using below command:
       `python3 data_ingestion\ingest_data.py`
 * Screenshot of the time taken to inject the data into database has been attached
    - File Name : result_data_ingestion.png


## Data Analysis
 
  * Data Analysis has been performed using `Pandas` library.
  * Data Analysis has been performed using below command:
        `python3 data_analysis\weather_station_stats.py`
    - File Name : result_data_analysis.png


## REST API
    
  * Flask Framework has been used to implement REST API.
  * Only 'GET request' is enabled
  * Default Pagination : 50 Records
  
  ### List of APIS exposed : 
   - /api/weather
   - /api/weather/stats

   Screenshots of REST apis with response times:
    - RESTAPI-api-weather-stats.png
    - RESTAPI-api-weather.png