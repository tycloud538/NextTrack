import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

from next_track.db import db
from next_track.home import home
from next_track.tags import tags
from next_track.tracks import tracks

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASEDIR, ".env"))


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_ECHO"] = True

    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.register_blueprint(home)
    app.register_blueprint(tags)
    app.register_blueprint(tracks)

    db.init_app(app)

    return app
