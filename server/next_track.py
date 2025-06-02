from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix

from recommendation import get_recommendation

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

# SELECT * FROM musicbrainz.track WHERE id >= RANDOM() *
#     ( SELECT MAX (id) FROM musicbrainz.track )
# ORDER BY id LIMIT 1;

@app.route("/")
def hello_world():
    return "Welcome to NextTrack. Your goto place for music recommendations."


@app.route("/track/recommendation", methods=["POST", "GET"])
def track_recommendation():
    recommendation = get_recommendation(request.json)

    if request.method == "POST":
        return {**request.json, **recommendation}
    return recommendation
