from Playwright_API.POM.Dashboard import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, userName, password):
        self.page.get_by_placeholder("email@example.com").fill(userName)
        self.page.locator("#userPassword").fill(password)
        self.page.get_by_role("button", name="Login").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage