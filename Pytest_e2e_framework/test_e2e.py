from Playwright_Pytest.POM.Login_Page import LoginPage


def test_e2e_fr (BrowserInstance):
    driver = BrowserInstance
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    # login page
    login = LoginPage(driver)
    # Select product and add to cart
    shop_page = login.loginPage()
    shop_page.add_product_to_cart("Blackberry")
    check_out = shop_page.go_to_cart()
    # check_out.handle_alert()
    check_out.check_out()
    check_out.country_input('Uni')
    check_out.success_validation()
