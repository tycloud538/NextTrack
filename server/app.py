from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Welcome to NextTrack. Your goto place for music recommendations."


@app.route("/track/recommendation", methods=["POST", "GET"])
def track_recommendation():
    recommendation = {
        "recommendation": "Your next track is: Not like us - Kendrick Lamar"
    }

    if request.method == "POST":
        return {**request.json, **recommendation}
    return recommendation
