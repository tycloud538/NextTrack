def test_get_tags(client):
    response = client.get('/tags')
    tags = response.json["tags"]

    assert response.status_code == 200
    assert tags
    assert len(tags) == 100


def test_get_tags_with_search(client):
    search_term = 'roc'

    response = client.get(f'/tags?search={search_term}')
    tags = response.json["tags"]

    assert response.status_code == 200
    assert tags
    assert len(tags) == 100
    assert all(search_term in tag['name'].lower() for tag in tags)

def test_get_tags_with_invalid_search(client):
    search_term = 'invalid_search_term'

    response = client.get(f'/tags?search={search_term}')
    tags = response.json["tags"]

    assert response.status_code == 200
    assert isinstance(tags, list)
    assert len(tags) == 0