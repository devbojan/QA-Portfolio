def test_get_users(api):
    response = api.get("users")

    test_get_users.api_response = response

    assert response.status == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0