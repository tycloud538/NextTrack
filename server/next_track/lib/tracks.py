from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from next_track.db import db
from next_track.models import Recording, ArtistCredit
from next_track.lib.recommendations import (
    get_content_driven_recommendation,
    get_random_track,
)


def search_tracks(term):
    """
    Search for tracks by a search term.
    """
    query = select(Recording).options(joinedload(Recording.artist_credit))

    # perform full-text search if search term is provided
    if term:
        search_terms = " & ".join(term.split())

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

    return tracks


def get_track_recommendation(track_history, tags):
    """
    Get a track recommendation based on the user's history and tags.
    """
    # If no history or tags, return a random track
    if not track_history and not tags:
        return get_random_track()

    # Else, provide a content-driven recommendation
    return get_content_driven_recommendation(track_history, tags)
