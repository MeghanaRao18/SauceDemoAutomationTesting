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
    #Open the login page
    saucedemo_page.go()
    assert saucedemo_page.swaglabs_login_logo.text() == 'Swag Labs'

    # Login with valid credentials
    saucedemo_page.username_input.input_text("standard_user")
    saucedemo_page.password_input.input_text("secret_sauce")
    saucedemo_page.login_button.click()

    yield saucedemo_page
    driver.quit()

def test_product_search(browser):
    """
    Test to validate search feature
    :param browser:
    :return:
    """
    #check if search button exists
    try:
        assert browser.search_button.is_displayed()
    except Exception as e:
        pytest.fail(f"Search button is not found or not visible. Error: {e}")

    # check if search input field exists
    try:
        assert browser.search_input.exists()
    except Exception as e:
        pytest.fail(f"Search input field is not found or not visible. Error: {e}")
    # enter item to search and test
    browser.search_input.input_text("Sauce Labs Fleece Jacket")
    browser.search_button.click()
    product_name = browser.item_name_inventory.text()
    assert  product_name == "Sauce Labs Fleece Jacket"


def test_search_no_results(browser):
    """
    Test to validate search option with no results
    :param browser:
    :return:
    """
    # check if search button exists
    try:
        assert browser.search_button.is_displayed()
    except Exception as e:
        pytest.fail(f"Search button is not found or not visible. Error: {e}")

    # check if search input field exists
    try:
        assert browser.search_input.exists()
    except Exception as e:
        pytest.fail(f"Search input field is not found or not visible. Error: {e}")

    # enter item that does not exist
    browser.search_input.input_text("Nonexistent")
    browser.search_button.click()
    assert browser.no_result_search.is_displayed()
