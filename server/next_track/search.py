from flask import Blueprint, request
from sqlalchemy import func
from sqlalchemy.orm import joinedload

from next_track.db import db
from next_track.models import Tag, Recording, ArtistCredit

search = Blueprint("search", __name__)


@search.route("/tags")
def tags():
    search = request.args.get("search", "").strip()
    query = db.session.query(Tag)

    # perform full-text search if search term is provided
    if search:
        search_terms = " & ".join([f"{term}:*" for term in search.split()])
        query = query.where(
            func.to_tsvector("english", Tag.name).op("@@")(
                func.to_tsquery(search_terms, postgresql_regconfig="english")
            )
        )

    # return tags ordered by rank
    tags = query.order_by(Tag.rank.desc()).limit(100)

    return {"tags": [{"id": tag.id, "name": tag.name} for tag in tags]}


@search.route("/tracks")
def tracks():
    search = request.args.get("search", "")
    query = db.session.query(Recording).options(joinedload(Recording.artist_credit))

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
    tracks = query.order_by(Recording.rank.desc()).limit(100)

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
