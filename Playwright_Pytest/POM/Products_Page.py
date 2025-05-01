from selenium.webdriver.common.by import By
from Playwright_Pytest.POM.Check_Out_Page import CheckOutPage



class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.products_list = (By.XPATH, "//div[@class='card h-100']")
        self.checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")


    def add_product_to_cart(self, product_name):
        products = self.driver.find_elements(*self.products_list)
        for product in products:
            if product.find_element(By.XPATH, "div/h4/a").text == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def go_to_cart(self):
        self.driver.find_element(*self.checkout).click()
        check_out = CheckOutPage(self.driver)
        return check_out