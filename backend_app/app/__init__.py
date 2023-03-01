from flask import Flask
from config import Config
from app.extensions import db
from app.weather_data import bp as main_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    app.register_blueprint(main_bp)

    @app.route("/test/")
    def test_page():
        return "<h1>This is a test url</h1>"

    return app
