import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from Playwright_API.POM.Login import LoginPage
from Playwright_API.test_api_base import APIUtils
# json -> utils to use data in test

with open("data.json") as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]

#envoke browser using playwright bc we need manipulate context in api testing
@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_new_page(playwright: Playwright, BrowserInstance, user_credentials):
    userName = user_credentials["userEmail"]
    password = user_credentials["userPassword"]
#create an order api post call
    api_utils = APIUtils()
    order_id = api_utils.create_order_api(playwright, user_credentials)
#login
    loginPage = LoginPage(BrowserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(userName, password)
#history order verify order id
    ordersHistory = dashboardPage.navigate()
    OrderDetailsPage = ordersHistory.select_order(order_id)
    OrderDetailsPage.assert_order_details(order_id)
    time.sleep(3)


