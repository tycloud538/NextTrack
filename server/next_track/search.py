from flask import Blueprint

search = Blueprint("search", __name__)


@search.route("/tags")
def tags():
    return "Welcome to NextTrack. Your goto place for music recommendations."


@search.route("/tracks")
def tracks():
    return "Welcome to NextTrack. Your goto place for music recommendations."
