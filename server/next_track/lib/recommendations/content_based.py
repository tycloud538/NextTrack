from sqlalchemy import select

from next_track.db import db
from next_track.models import Recording, RecordingTag
from next_track.lib.recommendations.base import Base


class ContentBasedModel(Base):
    """
    Content-based recommendation model that recommends tracks based on user history and relevant tags.
    """

    def recommend_tracks(self, num_tracks=1):
        query = (
            select(Recording.id)
            .join(RecordingTag.recording)
            # Find tracks that have the relevant tags and artists, but not in tracks
            .where(~Recording.id.in_(self.track_ids()))
            .where(
                RecordingTag.tag_id.in_(self.tag_ids())
                | Recording.artist_credit_id.in_(self.artist_credit_ids())
            )
            # TODO: Have a better ranking algorithm here for content-based model
            # .order_by(Recording.rank.desc())
            .limit(num_tracks)
        )

        return db.session.scalars(query)
