from flask import Blueprint, request
from mbdata.models import LinkRecordingURL, RecordingMeta, RecordingTag, Tag, Track, URL
from sqlalchemy import func, select
from sqlalchemy.orm import joinedload

from next_track.db import db

recommendation = Blueprint("recommendation", __name__)


def get_recording_metadata(recording_id):
    urls = (
        db.session.query(URL)
        .join(LinkRecordingURL.entity1)
        .where(LinkRecordingURL.entity0_id == recording_id)
        .all()
    )

    tags = (
        db.session.query(Tag)
        .join(RecordingTag.tag)
        .where(RecordingTag.recording_id == recording_id)
        .all()
    )

    recording_meta = (
        db.session.query(RecordingMeta).where(RecordingMeta.id == recording_id).first()
    )

    return {
        "rating": recording_meta.rating,
        "rating_count": recording_meta.rating_count,
        "tags": [tag.name for tag in tags],
        "urls": [url.url for url in urls],
    }


def get_recommendation(params={}):
    print(params)

    track = (
        db.session.query(Track)
        # Loads associated artist in same query
        .options(joinedload(Track.artist_credit))
        .join(RecordingMeta, RecordingMeta.id == Track.recording_id)
        # Finds a random track by randomly filtering for an id
        .where(Track.id >= func.random() * select(func.max(Track.id)))
        # The track should ideally have some user ratings available
        .where(RecordingMeta.rating_count >= 1)
        .order_by(Track.id)
        .first()
    )

    return {
        f"recommendation": "Your next track is: {} - {}".format(
            track.name, track.artist_credit.name
        ),
        "track_id": track.id,
        **get_recording_metadata(track.recording_id),
    }


@recommendation.route("/track/recommendation", methods=["POST"])
def recommend_track():
    return get_recommendation(request.json)
