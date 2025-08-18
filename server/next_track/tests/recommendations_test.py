def test_recommend_track(client):
    tags = [1]
    track_history = [1]
    response = client.post(
        f"/tracks/recommendations", json={"track_history": track_history, "tags": tags}
    )
    recommendation = response.json["recommendation"]

    assert response.status_code == 200
    assert recommendation
    assert recommendation["id"]
    assert recommendation["name"]
    assert recommendation["artist"]
    assert recommendation["artist"]["id"]
    assert recommendation["artist"]["name"]
    assert recommendation["rating"]
    assert isinstance(recommendation["tags"], list)
    assert isinstance(recommendation["urls"], list)
