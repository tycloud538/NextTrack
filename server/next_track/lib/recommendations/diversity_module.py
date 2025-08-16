from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from next_track.db import db
from next_track.models import Recording, RecordingTag
from next_track.lib.recommendations.base import Base


class DiversityModule(Base):
    """
    Diversity module that recommends tracks aiming to maximize artist diversity.
    """
    def recommend_tracks(self, num_tracks=40):
        # Find tracks that have the relevant tags, but not the relevant artists
        # Randomly sample tracks to ensure diversity
        track_ids = db.session.scalars(
            select(Recording.id)
            .join(RecordingTag.recording)
            .where(~Recording.artist_credit_id.in_(self.artist_credit_ids))
            .where(RecordingTag.tag_id.in_(self.tag_ids))
            .limit(num_tracks)
        )

        return [*track_ids]
