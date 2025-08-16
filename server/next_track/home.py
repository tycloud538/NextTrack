from flask import Blueprint

home = Blueprint("home", __name__)


@home.route("/")
def home_page():
    """
    Home page route for the NextTrack application.
    """
    return "Welcome to NextTrack. Your goto place for music recommendations."
