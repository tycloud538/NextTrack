from flask import Blueprint, request
from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from next_track.db import db
from next_track.models import Recording, ArtistCredit
from next_track.lib.metadata import get_recording_metadata
from next_track.lib.recommendations import get_track_recommendation

tracks = Blueprint("tracks", __name__)


@tracks.route("/tracks")
def get_tracks():
    search = request.args.get("search", "")
    query = select(Recording).options(joinedload(Recording.artist_credit))

    # perform full-text search if search term is provided
    if search:
        search_terms = " & ".join(search.split())

        # also search for first 15 relevant artists
        artists = (
            db.session.query(ArtistCredit)
            .where(
                func.to_tsvector("english", ArtistCredit.name).op("@@")(
                    func.to_tsquery(search_terms, postgresql_regconfig="english")
                )
            )
            .order_by(ArtistCredit.rank.desc())
            .limit(15)
        )

        # search based both on song name and relevant artists
        query = query.where(
            (
                func.to_tsvector("english", Recording.name).op("@@")(
                    func.to_tsquery(search_terms, postgresql_regconfig="english")
                )
            )
            | (Recording.artist_credit_id.in_([artist.id for artist in artists]))
        )

    # return tracks ordered by rank
    query = query.order_by(Recording.rank.desc()).limit(100)

    tracks = db.session.scalars(query)

    return {
        "tracks": [
            {
                "id": track.id,
                "name": track.name,
                "artist": {
                    "id": track.artist_credit.id,
                    "name": track.artist_credit.name,
                },
                "rank": track.rank,
            }
            for track in tracks
        ]
    }


@tracks.route("/tracks/recommendations", methods=["POST"])
def recommend_track():
    payload = request.json

    track = get_track_recommendation(
        payload.get("track_history", []), payload.get("tags", [])
    )

    return {
        "recommendation": {
            "id": track.id,
            "name": track.name,
            "artist": {"id": track.artist_credit.id, "name": track.artist_credit.name},
            **get_recording_metadata(track.id),
        }
    }
