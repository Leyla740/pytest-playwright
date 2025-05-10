import pytest
from playwright.sync_api import Playwright


@pytest.fixture()
def api_new_context(playwright: Playwright):
    request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
    yield request_context
    request_context.dispose()



