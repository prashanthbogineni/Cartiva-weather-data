from flask import Blueprint

bp = Blueprint("weather_data", __name__)

from app.weather_data import routes

