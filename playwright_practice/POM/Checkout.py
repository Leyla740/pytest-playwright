from playwright.sync_api import expect


class CheckoutPage:

    def __init__(self, page):
        self.page = page


    def checkout(self):
        self.page.locator("//button[@routerlink='/dashboard/cart']").click()
        expect(self.page.locator("//div/div[@class='cartSection']")).not_to_have_count(2)