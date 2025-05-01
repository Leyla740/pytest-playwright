import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope='function')
def BrowserInstance(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == "chrome":
        service_obj_ch = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_obj_ch)
    elif browser_name == "firefox":
        service_obj_f = FirefoxService(FirefoxDriverManager().install())
        driver = webdriver.Firefox(service=service_obj_f)
    yield driver
    driver.quit()
