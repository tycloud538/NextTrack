from flask import Blueprint

home = Blueprint("home", __name__)


@home.route("/")
def home_page():
    return "Welcome to NextTrack. Your goto place for music recommendations."
