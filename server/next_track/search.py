from flask import Blueprint, request

from next_track.models import Tag, Recording, ArtistCredit

search = Blueprint("search", __name__)


@search.route("/tags")
def tags():
    search_term = request.args.get("search", "")

    return request.args


@search.route("/tracks")
def tracks():
    search_term = request.args.get("search", "")

    return request.args
