from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from next_track.db import db
from next_track.models import Recording, RecordingTag
from next_track.lib.recommendations.base import Base


class DiversityModule(Base):
    """
    Diversity module that recommends tracks aiming to maximize artist diversity.
    """

    def __init__(self, tracks, tags, artist_ids=[]):
        super().__init__(tracks, tags)
        self.artist_ids = artist_ids

    def recommend_tracks(self, num_tracks=40):
        query = (
            select(Recording.id, Recording.artist_credit_id)
            .join(RecordingTag.recording)
            # Find tracks that have the relevant tags and artists, but not in track_history
            .where(~Recording.artist_credit_id.in_(self.artist_ids))
            .where(RecordingTag.tag_id.in_(self.tag_ids()))
            # TODO: Have a better ranking algorithm here, to ensure better diversity
            .order_by(Recording.rank.desc())
            .limit(num_tracks)
        )

        return db.session.scalars(query)
