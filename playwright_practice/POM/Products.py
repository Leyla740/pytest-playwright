from playwright_practice.POM.Checkout import CheckoutPage


class ProductsPage:

    def __init__(self, page):
        self.page = page


    def products(self):
        zara_coat = self.page.locator("//div/div[@class='card']").filter(has_text="ZARA COAT 3")
        zara_coat.click()
        Iphone = self.page.locator("//div/div[@class='card']").filter(has_text="IPHONE 13 PRO")
        Iphone.click()
        checkoutPage = CheckoutPage(self.page)
        return checkoutPage
