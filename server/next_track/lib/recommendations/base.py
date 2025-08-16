class Base:
    """
    Base class for recommendation models.
    """

    def __init__(self, tracks, tag_ids):
        self.tracks = tracks

        self.artist_credit_ids = [track.artist_credit_id for track in tracks]
        self.track_ids = [track.id for track in tracks]
        self.tag_ids = tag_ids
