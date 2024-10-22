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

def test_product_listing_page(browser):

    # check if all products are listed
    assert browser.page_title.text() == 'Products', 'Product page is not displayed'

    products = browser.item_name_inventory.getItems()
    assert len(products) > 0

def test_product_details_page(browser):

    """
    Test to verify each product detail page content
    :param browser:
    :return:
    """
    # check if all products are listed
    assert browser.page_title.text() == 'Products', 'Product page is not displayed'
    item_5_inventory = browser.item_5_title_link_inventory.text()

    #Navigate to the product detail page
    browser.item_5_title_link_inventory.click()
    assert browser.back_to_products_button.text() == 'Back to products', 'Product detail page not displayed'
    assert browser.item_5_title_link_detail.text() == item_5_inventory, 'Product name does not correspond'


def test_product_list_count(browser):

    # check if all products are listed
    assert browser.page_title.text() == 'Products', 'Product page is not displayed'

    products = browser.item_name_inventory.getItems()
    assert len(products) == 6  # Assuming 6 products are listed

def test_product_description(browser):
    """
    Test to verify the product description in product detail page
    :param browser:
    :return:
    """
    #select any item from the inventory list
    description = browser.item_desc_inventory.text()
    browser.item_name_inventory.click()

    # get the selected product detailed description
    product_detail = browser.item_title_link_detail_desc.text()
    print(product_detail)

    #check if it matches with the product  clicked from inventory
    assert description == product_detail
