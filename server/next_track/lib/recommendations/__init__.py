import random

from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from next_track.db import db
from next_track.models import Recording, RecordingTag, Tag
from next_track.lib.recommendations.context_based_filtering import (
    ContextBasedFiltering,
)
from next_track.lib.recommendations.content_based import ContentBasedModel
from next_track.lib.recommendations.diversity_module import DiversityModule


def get_all_tracks_and_tag_ids(track_history, relevant_tags):
    """
    Get all tracks and tags based on user history and relevant tags.
    """
    # Get all tracks from user's listening history
    tracks = db.session.scalars(
        select(Recording).where(Recording.id.in_(track_history))
    )

    # Get the user-selected tags and 15 top tags from track history
    tag_ids = db.session.scalars(
        select(Tag.id).where(
            Tag.id.in_(relevant_tags)
            | Tag.id.in_(
                (
                    select(Tag.id)
                    .join(RecordingTag.tag)
                    .where(RecordingTag.recording_id.in_(track_history))
                    .order_by(Tag.rank.desc())
                    .limit(15)
                ).scalar_subquery()
            )
        )
    )

    # Need to deconstruct scalar results to preserve models in-memory
    return [track for track in tracks], [tag_id for tag_id in tag_ids]


def get_content_driven_recommendation(track_history, tags):
    """
    Get a content-driven track recommendation based on user history and relevant tags.
    """
    tracks, tag_ids = get_all_tracks_and_tag_ids(track_history, tags)

    content_based_model = ContentBasedModel(tracks, tag_ids)
    tracks_1 = content_based_model.recommend_tracks()

    context_based_filtering = ContextBasedFiltering(tracks, tags)
    tracks_2 = context_based_filtering.recommend_tracks()

    diversity_module = DiversityModule(tracks, tag_ids)
    tracks_3 = diversity_module.recommend_tracks()

    return choose_random_track(
        [
            *tracks_1,
            *tracks_2,
            *tracks_3,
        ]
    )


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


def choose_random_track(track_ids):
    """
    Fetch a random track from a list of track IDs.
    """
    track_id = random.choice(track_ids)

    query = (
        select(Recording)
        # Loads associated artist in same query
        .options(joinedload(Recording.artist_credit))
        .where(Recording.id == track_id)
        .limit(1)
    )

    track = db.session.scalar(query)

    return track
