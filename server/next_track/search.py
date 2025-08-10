from flask import Blueprint, request
from sqlalchemy import func, select
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
    search_term = request.args.get("search", "")

    return request.args
