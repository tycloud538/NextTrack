from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from next_track.db import db
from next_track.models import Recording, RecordingTag
from next_track.lib.recommendations.base import Base


class CollaborativeFiltering(Base):
    def recommend_tracks(self, num_tracks=20):
        query = (
            select(Recording.id)
            .join(RecordingTag.recording)
            # Find tracks that have the relevant tags and artists, but not in track_history
            .where(
                (
                    RecordingTag.tag_id.in_(self.tag_ids())
                    | Recording.artist_credit_id.in_(self.artist_credit_ids())
                )
            )
            .order_by(Recording.rank.desc())
            .limit(num_tracks)
        )

        return db.session.scalars(query)
