from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from next_track.db import db
from next_track.models import Recording, RecordingTag


class ContentBasedModel:
    def __init__(self, track_history, tags):
        self.track_history = track_history
        self.tags = tags

    def listened_tracks(self):
        query = (
            select(Recording)
            .options(joinedload(Recording.artist_credit))
            .where(Recording.id.in_([track.id for track in self.track_history]))
        )
        return db.session.scalars(query)

    def listened_track_tags(self):
        query = (
            select(RecordingTag)
            .join(RecordingTag.recording)
            .where(Recording.id.in_([track.id for track in self.track_history]))
        )
        return [tag.id for tag in db.session.scalars(query)]

    def recommend_tracks(self, num_tracks=100):
        query = (
            select(Recording.id)
            .join(RecordingTag.recording)
            # Find tracks that have the relevant tags and artists, but not in track_history
            .where(
                ~Recording.id.in_(self.track_history)
                & (
                    RecordingTag.id.in_(self.tags)
                    | Recording.artist_credit.in_(
                        [track.artist_credit for track in self.listened_tracks()]
                    )
                    | RecordingTag.id.in_(self.listened_track_tags())
                )
            )
            # TODO: Have a better ranking algorithm here for content-based model
            .order_by(Recording.rank.desc())
            .limit(num_tracks)
        )

        tracks = db.session.scalars(query)

        return [track.id for track in tracks]
