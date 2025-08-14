from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from next_track.db import db
from next_track.models import Recording


def get_track_recommendation(track_history, tags):
    """
    Get a track recommendation based on the user's history and tags.
    """
    if not track_history and not tags:
        # If no history or tags, return a random track
        return get_random_track()

    return get_content_driven_recommendation(track_history, tags)


def get_content_driven_recommendation(_track_history, _tags):
    return get_random_track()


def get_random_track():
    """
    Get a random track recommendation.
    """
    query = (
        select(Recording)
        # Loads associated artist in same query
        .options(joinedload(Recording.artist_credit))
        # Finds a random track by randomly filtering for an id
        .where(
            Recording.id
            >= func.random() * select(func.max(Recording.id)).scalar_subquery()
        )
        # The track should ideally have some user ratings available
        .where(Recording.rank > 0)
        .order_by(Recording.id)
        .limit(1)
    )

    track = db.session.scalar(query)

    return track
