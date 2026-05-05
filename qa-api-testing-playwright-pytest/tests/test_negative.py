def test_user_not_found(api, page):
    response = api.get("users/9999")

    test_user_not_found.api_response = response

    #assert
    assert response.status == 200