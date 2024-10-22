from pages.drivers import Drivers
from pages.saucedemo_page import SaucedemoPage
from selenium.common.exceptions import TimeoutException
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

def test_add_to_cart_inventory(browser):

    """
    This test add items to cart from product listing page and check the cart
    :param browser:
    :return:
    """
    # Add an item to the cart
    browser.add_to_cart_item_5.click()
    item = "Sauce Labs Fleece Jacket"

    # check if remove option available
    assert browser.remove_item_5.text() == 'Remove', 'Remove button is not displayed'

    # Navigate to the shopping cart page
    browser.shopping_cart_button.click()

    # check if remove option available
    assert browser.remove_item_5.text() == 'Remove', 'Remove button is not displayed'

    assert browser.page_title.text() == 'Your Cart', 'Your cart page is not displayed'
    cart_items = browser.item_name_inventory.getItems()

    item_names = [item.text for item in cart_items]
    assert item in item_names, 'Item  not added to cart page'



def test_add_to_cart_product_detail(browser):
    """
    This test adds the items to card from individual product detail page and verifies the cart contents
    :param browser:
    :return:
    """
    # select any item and goto product detail page
    item = browser.item_name_inventory.text()
    browser.item_name_inventory.click()


    # Add the above item to the cart from product detail page
    browser.add_to_cart_item.click()

    # check if remove option available
    assert browser.remove_item.text() == 'Remove', 'Remove button is not displayed'

    # Navigate to the shopping cart page
    browser.shopping_cart_button.click()
    assert browser.page_title.text() == 'Your Cart', 'Your cart page is not displayed'

    assert "1" in browser.shopping_cart_badge.text()
    cart_items = browser.item_name_inventory.getItems()

    item_names = [item.text for item in cart_items]
    assert item in item_names, 'Item  not added to cart page'


def test_cart_item_removal(browser):
    """
    This test verifies item removal from the cart
    :param browser:
    :return:
    """

    # Add one item to the cart
    browser.add_to_cart_item_5.click()
    item_name = "Sauce Labs Fleece Jacket"

    # check if remove option available
    assert browser.remove_item_5.text() == 'Remove', 'Remove button is not displayed'

    # Navigate to the shopping cart page
    browser.shopping_cart_button.click()
    assert browser.page_title.text() == 'Your Cart', 'Your cart page is not displayed'

    browser.remove_item_5.click()

    # on item removal check for cart items class, it should be empty
    try:
        cart_items = browser.shopping_cart_item.getItems()
        assert len(cart_items) == 0
    except TimeoutException:
        pytest.fail(" Failed to verify empty cart. empty cart items class not present")


    assert browser.shopping_cart_list.text() == "Your cart is empty", "Cart is not empty even after items removal"


def test_cart_empty_message(browser):
    """
    This test checks appropriate messaging in the cart page when there are no items in the cart
    :param browser:
    :return:
    """
    # Navigate to the shopping cart page
    browser.shopping_cart_button.click()
    assert browser.shopping_cart_list.text() == "Your cart is empty", "No appropriate cart empty message"


def test_cart_icon_badge(browser):
    """
    This test validates the item in cart count from the shopping cart badge
    :param browser:
    :return:
    """
    # Add an item to the cart
    browser.add_to_cart_item_5.click()
    item = "Sauce Labs Fleece Jacket"

    # check if remove option available
    assert browser.remove_item_5.text() == 'Remove', 'Remove button is not displayed'

    # get cart badge count
    try:
        count = browser.shopping_cart_badge.text()
    except TimeoutException:
        pytest.fail(" Failed to verify cart badge count. As Cart badge class not present")

    #check if count is incremented to 1
    assert count == "1"

    # remove item from cart
    browser.remove_item_5.click()

    # get cart badge count
    try:
        count = browser.shopping_cart_badge.text()
    except TimeoutException:
        pytest.fail("Failed to verify cart badge count. As cart badge class not present")

    assert count == "0" or count == ""


def test_update_item_quantity(browser):
    """
    This test validates the quantity update feature in the cart page

    :param browser:
    :return:
    """
    # Add  item to the cart
    browser.add_to_cart_item_5.click()

    # Navigate to the shopping cart page
    browser.shopping_cart_button.click()

    # Check if the element is an <input> field
    assert browser.quantity_input.web_element.tag_name == "input", "Failed to update item quantity. The quantity field is not an input element."

    # Check if the type of the input field is 'number' (if applicable)
    input_type = browser.quantity_input.web_element.get_attribute("type")
    assert input_type == "number", f"Expected input type 'number', but got '{input_type}'"

    # Check if the quantity field is interactable
    assert browser.quantity_input.is_enabled(), "Quantity input field is not enabled."

    # Update the quantity to a new value
    browser.quantity_input.web_element.clear()
    browser.quantity_input.web_element.send_keys("5")

    # Verify the new value
    updated_value = browser.quantity_input.web_element.get_attribute("value")
    assert updated_value == "5", f"Expected quantity to be '5', but got '{updated_value}'"


