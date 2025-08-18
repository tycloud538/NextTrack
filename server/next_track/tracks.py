from flask import Blueprint, request

from next_track.lib.metadata import get_recording_metadata
from next_track.lib.tracks import search_tracks, get_track_recommendation

tracks = Blueprint("tracks", __name__)


@tracks.route("/tracks")
def get_tracks():
    """
    Controller to search for tracks based on a search term.
    """
    search = request.args.get("search", "")

    tracks = search_tracks(term=search)

    return {
        "tracks": [
            {
                "id": track.id,
                "name": track.name,
                "artist": {
                    "id": track.artist_credit.id,
                    "name": track.artist_credit.name,
                },
                "rank": track.rank,
            }
            for track in tracks
        ]
    }


@tracks.route("/tracks/recommendations", methods=["POST"])
def recommend_track():
    """
    Controller to recommend a track based on user history and relevant tags.
    """
    track_history = request.json.get("track_history", [])
    print("TCL ~ track_history:", track_history)
    tags = request.json.get("tags", [])
    print("TCL ~ tags:", tags)

    track = get_track_recommendation(track_history=track_history, tags=tags)

    return {
        "recommendation": {
            "id": track.id,
            "name": track.name,
            "artist": {"id": track.artist_credit.id, "name": track.artist_credit.name},
            **get_recording_metadata(track.id),
        }
    }
