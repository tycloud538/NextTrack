from flask import Blueprint, request
from mbdata.models import Track
from sqlalchemy import func, select
from sqlalchemy.orm import joinedload

from next_track.db import db

recommendation = Blueprint("recommendation", __name__)


def get_recommendation(params={}):
    track = (
        db.session.query(Track)
        # Loads associated artist in same query
        .options(joinedload(Track.artist_credit))
        # Finds a random track by randomly filtering for an id
        .filter(Track.id >= func.random() * select(func.max(Track.id)))
        .order_by(Track.id)
        .first()
    )

    return {
        **params,
        f"recommendation": "Your next track is: {} - {}".format(
            track.name, track.artist_credit.name
        ),
    }


@recommendation.route("/track/recommendation", methods=["POST", "GET"])
def recommend_track():
    if request.method == "POST":
        return get_recommendation(request.json)

    return get_recommendation()
