class Base:
    def __init__(self, tracks, tags):
        self.tracks = tracks
        self.tags = tags

    def artist_credit_ids(self):
        return [track.artist_credit_id for track in self.tracks]

    def track_ids(self):
        return [track.id for track in self.tracks]

    def tag_ids(self):
        return [tag.id for tag in self.tags]
