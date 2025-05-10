from playwright_practice.POM.Products import ProductsPage
from playwright_practice.conftest import user_credentials


class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, userName, userPassword):
        self.page.goto("https://rahulshettyacademy.com/client")
        self.page.locator("#userEmail").fill(userName)
        self.page.locator("#userPassword").fill(userPassword)
        self.page.locator("#login").click()
        productsPage = ProductsPage(self.page)
        return productsPage
