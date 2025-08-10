from flask import Blueprint, request
from sqlalchemy import func, select
from sqlalchemy.orm import joinedload

from next_track.db import db
from next_track.models import (
    LinkRecordingURL,
    Recording,
    RecordingMeta,
    RecordingTag,
    Tag,
    URL,
)

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
        .order_by(Tag.rank.desc())
        .all()
    )

    recording_meta = (
        db.session.query(RecordingMeta).where(RecordingMeta.id == recording_id).first()
    )

    return {
        "rating": recording_meta.rating,
        "tags": [tag.name for tag in tags],
        "urls": [url.url for url in urls],
    }


@recommendation.route("/tracks/recommendation", methods=["POST"])
def recommend_track():
    print(request.json)

    track = (
        db.session.query(Recording)
        # Loads associated artist in same query
        .options(joinedload(Recording.artist_credit))
        # Finds a random track by randomly filtering for an id
        .where(Recording.id >= func.random() * select(func.max(Recording.id)))
        # The track should ideally have some user ratings available
        .where(Recording.rank > 0)
        .order_by(Recording.id)
        .first()
    )

    return {
        "id": track.id,
        "name": track.name,
        "artist": {
            "id": track.artist_credit.id,
            "name": track.artist_credit.name
        },
        **get_recording_metadata(track.id),
    }
