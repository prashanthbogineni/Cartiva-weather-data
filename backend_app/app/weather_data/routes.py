from app.weather_data import bp
from flask import request, jsonify



@bp.route("/")
def index():
    return "This is CORTEVA project"
