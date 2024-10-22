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

def test_login_valid(browser):
    """
    test to verify login feature with valid user data
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

def test_login_invalid(browser):
    """
    Test to verify login feature with invalid username and password
    :param browser:
    :return:
    """

    #Open the login page
    browser.go()
    assert browser.swaglabs_login_logo.text() == 'Swag Labs'

    # Login with invalid credentials
    browser.username_input.input_text("invalid")
    browser.password_input.input_text("wrong")
    browser.login_button.click()

    # Check for the error message
    assert browser.login_error.text() == "Epic sadface: Username and password do not match any user in this service"

def test_login_empty_credentials(browser):
    """

    :param browser:
    :return:
    """
    #Open the login page
    browser.go()
    assert browser.swaglabs_login_logo.text() == 'Swag Labs'
    browser.login_button.click()

    # check for the error message
    assert browser.login_error.text() == "Epic sadface: Username is required"

def test_login_locked_out_user(browser):
    """
    Test to verify the flow if the user is locked out
    :param browser:
    :return:
    """
    #Open the login page
    browser.go()
    assert browser.swaglabs_login_logo.text() == 'Swag Labs'

    # Login with invalid credentials
    browser.username_input.input_text("locked_out_user")
    browser.password_input.input_text("secret_sauce")
    browser.login_button.click()

    # Check for the error message
    assert browser.login_error.text() == "Epic sadface: Sorry, this user has been locked out."
