# NextTrack, a Music Recommendation App

## Installation

1. Ensure that `postgresql`, `node`, `npm`, and `python3` are installed.

2. Setup a locally running Postgres instance using the Musicbrainz Postgres data dump: https://metabrainz.org/datasets/postgres-dumps#musicbrainz

   - One possible option is to use `mbslave` (https://github.com/acoustid/mbslave)

3. Install `/client` dependencies with `npm install`

4. Create a new virtual environment in `/server` with `python -m venv`

5. Activate the virtual environment in `/server` with `.venv/bin/activate`

6. Install `/server` dependencies with `pip install -r requirements.txt`

## Running the app

1. Ensure that Postgres database is running.

2. In `/client`, start the app with `npm run dev`

3. In `/server`, start the server with `flask run`
