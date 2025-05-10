import pytest
from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import browser

@pytest.fixture
def user_credentials(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture
def BrowserInvocation(playwright:Playwright, request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(args=["--start-maximized"], headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(args=["--start-maximized"], headless=False)
    elif browser_name == "safari":
        browser = playwright.webkit.launch(args=["--start-maximized"], headless=False)

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()


