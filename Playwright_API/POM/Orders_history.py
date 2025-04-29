from Playwright_API.POM.Orders_details import OrderDetails


class OrdersHistoryPage:

    def __init__(self, page):
        self.page = page

    def select_order(self, order_id):
        order_id_list = self.page.locator("//tbody/tr").filter(has_text=order_id)
        order_id_list.get_by_role("button", name="View").click()
        OrderDetailsPage = OrderDetails(self.page)
        return OrderDetailsPage