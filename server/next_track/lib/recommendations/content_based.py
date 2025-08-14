from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from next_track.db import db
from next_track.models import Recording, RecordingTag


class ContentBasedModel:
    def __init__(self, track_history, tags):
        self.track_history = track_history
        self.tags = tags

    def recommend_tracks(self, num_tracks=100):
        query = (
            select(Recording)
            # Loads associated artist in same query
            .options(joinedload(Recording.artist_credit))
            .join(RecordingTag.recording)
            .order_by(Recording.rank.desc())
            .limit(num_tracks)
        )

        tracks = db.session.scalars(query)

        return tracks
