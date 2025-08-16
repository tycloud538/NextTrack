from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from next_track.db import db
from next_track.models import Recording, RecordingTag
from next_track.lib.recommendations.base import Base


class CollaborativeFiltering(Base):
    """
    Collaborative filtering recommendation model that recommends tracks based on user ratings and popularity.
    """

    def recommend_tracks(self, num_tracks=40):
        print("self.artist_credit_ids()", self.artist_credit_ids())

        artist_tracks = db.session.scalars(
            select(Recording.id)
            # Find tracks that are relevant to the related artists
            .where(Recording.artist_credit_id.in_(self.artist_credit_ids()))
            .order_by(Recording.rank.desc())
            .limit(num_tracks // 2)
        )

        # print('artist_tracks', [*artist_tracks])

        tag_tracks = db.session.scalars(
            select(Recording.id)
            .join(RecordingTag.recording)
            # Find tracks that have the relevant tags, but not the related
            .where(RecordingTag.tag_id.in_(self.tag_ids()))
            .where(~Recording.artist_credit_id.in_(self.artist_credit_ids()))
            .order_by(Recording.rank.desc())
            .limit(num_tracks // 2)
        )

        # print('tag_tracks', [*tag_tracks])

        return [*artist_tracks, *tag_tracks]
