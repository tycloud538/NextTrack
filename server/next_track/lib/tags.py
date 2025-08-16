from sqlalchemy import select, func

from next_track.db import db
from next_track.models import Tag


def search_tags(term):
    query = select(Tag)

    # perform full-text search if search term is provided
    if term:
        search_terms = " & ".join([f"{t}:*" for t in term.split()])
        query = query.where(
            func.to_tsvector("english", Tag.name).op("@@")(
                func.to_tsquery(search_terms, postgresql_regconfig="english")
            )
        )

    # return tags ordered by rank
    query = query.order_by(Tag.rank.desc()).limit(100)

    tags = db.session.scalars(query)

    return tags
