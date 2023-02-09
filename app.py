from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather_data.db'
db = SQLAlchemy(app)

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    max_temp = db.Column(db.Float)
    min_temp = db.Column(db.Float)
    precipitation = db.Column(db.Float)
    station_id = db.Column(db.String)
    

class WeatherStatistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    avg_max_temp = db.Column(db.Float)
    avg_min_temp = db.Column(db.Float)
    total_precipitation = db.Column(db.Float)
    station_id = db.Column(db.String)

@app.route('/api/weather', methods=['GET'])
def get_weather_data():
    date = request.args.get('date')
    station_id = request.args.get('station_id')
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    weather_data = WeatherData.query
    if date:
        weather_data = weather_data.filter_by(date=date)
    if station_id:
        weather_data = weather_data.filter_by(station_id=station_id)

    weather_data = weather_data.paginate(page=page, per_page=per_page).items

    return jsonify([{
        'date': data.date,
        'max_temp': data.max_temp,
        'min_temp': data.min_temp,
        'precipitation': data.precipitation,
        'station_id': data.station_id
    } for data in weather_data])

@app.route('/api/weather/stats', methods=['GET'])
def get_weather_statatics():
    year = request.args.get('year')
    station_id = request.args.get('station_id')
    page = request.args.get('page')
    per_page = request.args.get('per_page')

    weather_statatics = WeatherStatistics.query
    if year:
        weather_statatics = weather_statatics.filter_by(year=year)
    if station_id:
        weather_statatics = weather_statatics.filter_by(station_id=station_id)

    weather_statatics = weather_statatics.paginate(page=page, per_page=per_page).items

    return  jsonify([{
        'data': [{'year': ws.year, 
        'station': ws.station, 
        'avg_max_temp': ws.avg_max_temp, 
        'avg_min_temp': ws.avg_min_temp, 
        'accumulated_prec':ws.total_precipitation}]} for ws in weather_statatics])


if __name__ == '__main__':
    print("app running")
    app.run()