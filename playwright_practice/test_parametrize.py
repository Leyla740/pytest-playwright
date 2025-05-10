import pytest
from playwright.sync_api import Playwright, expect

@pytest.mark.parametrize(
  "user_credentials", [
    {
      "userEmail": "devop740@gmail.com",
      "userPassword": "T0gether@"
    },
    {
      "userEmail": "jabbarova.leyla@gmail.com",
      "userPassword": "T0gether@"
    }
  ]
)
def test_browser_set_up(BrowserInvocation, user_credentials):
    # login
    page = BrowserInvocation
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill(user_credentials["userEmail"])
    page.locator("#userPassword").fill(user_credentials["userPassword"])
    page.locator("#login").click()
    # select product
    zara_coat = page.locator("//div/div[@class='card']").filter(has_text="ZARA COAT 3")
    zara_coat.click()
    Iphone = page.locator("//div/div[@class='card']").filter(has_text="IPHONE 13 PRO")
    Iphone.click()
    # check out
    page.locator("//button[@routerlink='/dashboard/cart']").click()
    expect(page.locator("//div/div[@class='cartSection']")).not_to_have_count(2)