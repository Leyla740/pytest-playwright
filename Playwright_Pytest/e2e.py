import time

from playwright.sync_api import Playwright, Page, expect


# def test_playwrightDemo(playwright:Playwright_Pytest):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://playwright.com/")
def test_e2e(page:Page):

    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    iphone = page.locator("//div[@class='card h-100']").filter(has_text="iphone X")
    iphone.get_by_role("button").click()
    time.sleep(3)
    iphone = page.locator("//div[@class='card h-100']").filter(has_text="Blackberry")
    iphone.get_by_role("button").click()
    time.sleep(3)
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)




