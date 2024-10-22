from logging import exception

from asgiref.timeout import timeout

from pages.drivers import Drivers
from pages.saucedemo_page import SaucedemoPage
from selenium.common.exceptions import TimeoutException
import pytest


@pytest.fixture
def browser():
    """
    Pre and post condition code and checks for every test
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
    # Add  items to the cart
    saucedemo_page.add_to_cart_item_5.click()
    saucedemo_page.add_to_cart_item_4.click()

    # Navigate to the shopping cart page
    saucedemo_page.shopping_cart_button.click()

    # click checkout
    saucedemo_page.checkout_button.click()

    yield saucedemo_page
    driver.quit()

def test_checkout(browser):

    """
    Test checkout feature with valid input values
    :param browser:
    :return:
    """
    browser.first_name_input_text.input_text("Meghana")
    browser.last_name_input_text.input_text("Rao")
    browser.postal_code_input_text.input_text("3064")
    browser.continue_button.click()
    assert  browser.page_title.text()  == "Checkout: Overview"

    browser.finish_button.click()

    assert browser.order_complete.text() == "Thank you for your order!"

def test_invalid_data(browser):
    """
    Test checkout feature with invalid input values
    :param browser:
    :return:
    """

    #checkout with empty fields

    browser.first_name_input_text.input_text("")
    browser.last_name_input_text.input_text("")
    browser.postal_code_input_text.input_text("")
    browser.continue_button.click()

    assert browser.login_error.is_displayed()

    assert browser.login_error.text() == "Error: First Name is required"

    # checkout with invalid postal code
    browser.first_name_input_text.input_text("Meghana")
    browser.last_name_input_text.input_text("Rao")
    browser.postal_code_input_text.input_text(" ")
    browser.continue_button.click()
    # Check for the error message with invalid/ empty postal code
    try:
        assert browser.login_error.is_displayed()
    except TimeoutException:
        pytest.fail("Checkout was allowed even with invalid postal code !!")

    assert browser.login_error.text() == "Error: Postal Code is required"


def test_total_summary(browser):
    """
    Test to check the total cost of all the items in cart matches with the summary in checkout page
    :param browser:
    :return:
    """
    browser.first_name_input_text.input_text("Meghana")
    browser.last_name_input_text.input_text("Rao")
    browser.postal_code_input_text.input_text("3064")
    browser.continue_button.click()
    assert  browser.page_title.text()  == "Checkout: Overview"

    # Locate item prices and total summary price on the checkout page

    item_prices = browser.item_price_inventory.getItems()

    total_summary = browser.summary_sub_total.text()

    # Extract total summary price value
    total_summary_price = float(total_summary.split('$')[1])

    # Calculate expected total price
    item_prices_values = [float(price.text.replace('$', '')) for price in item_prices]
    expected_total = sum(item_prices_values)

    # Verify that the total summary price matches the expected total
    assert total_summary_price == expected_total, f"Expected total price ${expected_total}, but got ${total_summary_price}"


def test_empty_cart_checkout(browser):
    """
    Test to verify the checkout process when no items in the cart
    :param browser:
    :return:
    """
    #removing 2 items added aws part of precondition

    # Navigate to the shopping cart page
    browser.shopping_cart_button.click()
    assert browser.page_title.text() == 'Your Cart', 'Your cart page is not displayed'

    browser.remove_item_5.click()
    browser.remove_item_4.click()
    # Assuming the application prevents checkout with an empty cart and shows a message and the button to be inactive
    assert not browser.checkout_button.is_enabled(), "Checkout button is enabled even though cart is empty"

