import json

import pytest
from playwright.sync_api import Playwright, expect

from playwright_practice.POM.Login import LoginPage
from playwright_practice.POM.Products import ProductsPage

with open("data.json", "r") as f:
    data = json.load(f)
    user_data = data["user_credentials"]

@pytest.mark.parametrize("user_credentials", user_data)
def test_browser_set_up(BrowserInvocation, user_credentials):
    userName = user_credentials["userEmail"]
    userPassword = user_credentials["userPassword"]
    loginPage = LoginPage(BrowserInvocation)
    #login
    productsPage = loginPage.login(userName, userPassword)
    # select products
    checkoutPage = productsPage.products()
    # check out
    checkoutPage.checkout()






