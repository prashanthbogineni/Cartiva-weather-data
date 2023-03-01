import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "weather_data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
