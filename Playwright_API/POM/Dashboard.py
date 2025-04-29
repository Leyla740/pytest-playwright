from Playwright_API.POM.Orders_history import OrdersHistoryPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.get_by_role("button", name="ORDERS").click()
        ordersHistory = OrdersHistoryPage(self.page)
        return ordersHistory
