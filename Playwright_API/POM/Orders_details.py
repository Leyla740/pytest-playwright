from playwright.sync_api import expect


class OrderDetails:

    def __init__(self, page):
        self.page = page

    def assert_order_details(self, order_id):
        expect(self.page.locator(".tagline")).to_be_visible()
        print(order_id)
        print(self.page.locator(".tagline").text_content())