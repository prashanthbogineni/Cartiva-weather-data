from app.extensions import db


class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    max_temp = db.Column(db.Float)
    min_temp = db.Column(db.Float)
    precipitation = db.Column(db.Float)
    station_id = db.Column(db.String)


    def __repr__(self):
        return f'{self.id}{self.date}'


class WeatherStatistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    avg_max_temp = db.Column(db.Float)
    avg_min_temp = db.Column(db.Float)
    total_precipitation = db.Column(db.Float)
    station_id = db.Column(db.String)

    def __repr__(self):
        return f'{self.id}{self.year}'
