import random

from sqlalchemy import select

from next_track.db import db
from next_track.models import Recording, RecordingTag
from next_track.lib.recommendations.base import Base


class ContentBasedModel(Base):
    """
    Content-based recommendation model that recommends tracks based on user history and relevant tags.
    """

    def recommend_tracks(self, num_tracks=25):
        # Introduce an element of randomness (6 possible sets)
        random_rank = random.randint(0, 1)
        offsets = range(0, 12, 2)
        random_ranks = [random_rank + offset for offset in offsets]

        # Find tracks that are most related to the user's preferences
        track_ids = db.session.scalars(
            select(Recording.id)
            .join(RecordingTag.recording)
            .where(RecordingTag.tag_id.in_(self.tag_ids))
            .where(Recording.artist_credit_id.in_(self.artist_credit_ids))
            .where(Recording.random_rank.in_(random_ranks))
            .limit(num_tracks)
        )

        return [*track_ids]
