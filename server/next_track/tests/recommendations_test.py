def test_recommend_diverse_tracks(client):
    tags = [1]
    track_history = [1]
    artist_ids = set()

    for _ in range(20):
        response = client.post(
            f"/tracks/recommendations",
            json={"track_history": track_history, "tags": tags},
        )
        recommendation = response.json["recommendation"]

        assert response.status_code == 200
        assert recommendation
        assert recommendation["id"]
        assert recommendation["artist"]["id"]

        artist_ids.add(recommendation["artist"]["id"])

    print(f"Number of unique artists: {len(artist_ids)}")
    assert len(artist_ids) >= 10


########## RESULTS ###########
# Number of unique artists: 13
# Number of unique artists: 17
# Number of unique artists: 14
# Number of unique artists: 16
# Number of unique artists: 13
