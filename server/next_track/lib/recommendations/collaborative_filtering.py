from sqlalchemy import select

from next_track.db import db
from next_track.models import Recording, RecordingTag
from next_track.lib.recommendations.base import Base


class CollaborativeFiltering(Base):
    """
    Collaborative filtering recommendation model that recommends tracks based on user ratings and popularity.
    """

    def recommend_tracks(self, num_tracks=30):
        # Find top tracks that are relevant to the artists
        artist_track_ids = db.session.scalars(
            select(Recording.id)
            .where(Recording.artist_credit_id.in_(self.artist_credit_ids))
            .order_by(Recording.rank.desc())
            .limit(num_tracks // 2)
        )

        # Find top tracks that have the relevant tags, but not the related artists
        tag_track_ids = db.session.scalars(
            select(Recording.id)
            .join(RecordingTag.recording)
            .where(RecordingTag.tag_id.in_(self.tag_ids))
            .where(~Recording.artist_credit_id.in_(self.artist_credit_ids))
            .order_by(Recording.rank.desc())
            .limit(num_tracks // 2)
        )

        return [*artist_track_ids, *tag_track_ids]
