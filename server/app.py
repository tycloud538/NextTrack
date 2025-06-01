from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome to NextTrack. Your goto place for music recommendations."

@app.route("/track/recommendation", methods=['POST', 'GET'])
def track_recommendation():
    return { "recommendation": "Your next track is: Not like us - Kendrick Lamar" }