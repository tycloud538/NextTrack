def test_get_tracks(client):
    response = client.get('/tracks')
    tracks = response.json["tracks"]

    assert response.status_code == 200
    assert tracks
    assert len(tracks) == 100


def test_get_tracks_with_search(client):
    search_term = 'weeknd'

    response = client.get(f'/tracks?search={search_term}')
    tracks = response.json["tracks"]

    assert response.status_code == 200
    assert tracks
    assert len(tracks) == 100
    assert all((search_term in track['name'].lower() or search_term in track['artist']['name'].lower()) for track in tracks)


def test_recommend_track(client):
    tags = [1]
    tracks = [1]
    response = client.post(f'/tracks/recommendations', json={"tracks": tracks})
    recommendation = response.json["recommendation"]

    assert response.status_code == 200
    assert recommendation
    assert recommendation['id']
    assert recommendation['name']
    assert recommendation['artist']
    assert recommendation['artist']['id']
    assert recommendation['artist']['name']
    assert recommendation['rating']
    assert isinstance(recommendation['tags'], list)
    assert isinstance(recommendation['urls'], list)