from selenium.webdriver.common.by import By

from Playwright_Pytest.POM.Products_Page import ProductPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # self.username_input = (By.XPATH, "//input[@id='username']")
        # self.password_input = (By.XPATH, "//input[@id='password']")
        self.button_click = (By.XPATH, "//a[normalize-space()='Shop']")


    def loginPage(self):
        # self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        # self.driver.find_element(*self.password_input).send_keys("learning")
        self.driver.find_element(* self.button_click).click()
        shop_page = ProductPage(self.driver)
        return shop_page