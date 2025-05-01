
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException



class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
        self.check_out_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_field = (By.XPATH, "//input[@id='country']")
        self.country = (By.XPATH, "//a[contains(text(),'America')]")
        self.agree_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.purchase_button = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
        self.success_message = (By.XPATH, "//strong[contains(text(), 'Success!')]")





    def check_out(self):
        self.driver.find_element(*self.check_out_button).click()

    def country_input(self, country_name):
        self.driver.find_element(*self.country_field).send_keys(country_name)
        WebDriverWait(self.driver, 8).until(
            EC.element_to_be_clickable((self.country))).click()
        self.driver.find_element(*self.agree_checkbox).click()
        self.driver.find_element(*self.purchase_button).click()

    def success_validation(self):
        success_msg = self.driver.find_element(*self.success_message).text
        assert success_msg == 'Success!'
        self.driver.get_screenshot_as_file('screenshot.png')