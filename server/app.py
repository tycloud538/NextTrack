from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

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
