from pages.drivers import Drivers
from pages.saucedemo_page import SaucedemoPage
import pytest


@pytest.fixture
def browser():
    """
    Pre-condition and post-condition code and checks for every test
    :return:
    """
    # Create a browser instance
    driver = Drivers('--ignore-certificate-errors').chrome()
    saucedemo_page = SaucedemoPage(driver=driver)
    yield saucedemo_page
    driver.quit()

def test_logout(browser):
    """
    Test to validate logout feature and flow
    :param browser:
    :return:
    """
    #Open the login page
    browser.go()
    assert browser.swaglabs_login_logo.text() == 'Swag Labs'

    # Login with valid credentials
    browser.username_input.input_text("standard_user")
    browser.password_input.input_text("secret_sauce")
    browser.login_button.click()

    assert "Products" in browser.page_title.text()

    browser.burger_menu_button.click()
    browser.logout_sidebar_link.click()
    assert browser.login_button is not None


def test_logout_redirection(browser):
    """

    :param browser:
    :return:
    """
    #Open the login page
    browser.go()
    assert browser.swaglabs_login_logo.text() == 'Swag Labs'

    # Login with valid credentials
    browser.username_input.input_text("standard_user")
    browser.password_input.input_text("secret_sauce")
    browser.login_button.click()

    assert "Products" in browser.page_title.text()

    browser.burger_menu_button.click()
    browser.logout_sidebar_link.click()

    assert browser.swaglabs_login_logo.text() == 'Swag Labs'
    assert browser.login_button.is_displayed()