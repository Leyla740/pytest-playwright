import pytest
from playwright.sync_api import Playwright


@pytest.fixture()
def api_new_context(playwright: Playwright):
    request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
    yield request_context
    request_context.dispose()

@pytest.fixture()
def get_token(api_new_context):
    data = {
        "userEmail": "jabbarova.leyla@gmail.com",
        "userPassword": "T0gether@"
    }
    response = api_new_context.post("/api/ecom/auth/login", data=data)
    assert response.ok
    response_body = response.json()
    print(response_body["token"])
    token = response_body["token"]
    return token #or response_body["token"]


