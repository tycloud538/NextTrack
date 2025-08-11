from next_track.db import db
from next_track.models import (
    LinkRecordingURL,
    RecordingMeta,
    RecordingTag,
    Tag,
    URL,
)


def get_recording_metadata(recording_id):
    urls = (
        db.session.query(URL)
        .join(LinkRecordingURL.entity1)
        .where(LinkRecordingURL.entity0_id == recording_id)
        .all()
    )

    tags = (
        db.session.query(Tag)
        .join(RecordingTag.tag)
        .where(RecordingTag.recording_id == recording_id)
        .order_by(Tag.rank.desc())
        .all()
    )

    recording_meta = (
        db.session.query(RecordingMeta).where(RecordingMeta.id == recording_id).first()
    )

    return {
        "rating": recording_meta.rating,
        "tags": [tag.name for tag in tags],
        "urls": [url.url for url in urls],
    }

