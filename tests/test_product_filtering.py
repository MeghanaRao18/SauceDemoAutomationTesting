from pages.drivers import Drivers
from pages.saucedemo_page import SaucedemoPage
import pytest
from selenium.webdriver.common.by import By


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

    #check if filter option exists
    try:
        assert saucedemo_page.filter.is_displayed()
    except Exception as e:
        pytest.fail(f"filter option  is not found or not visible. Error: {e}")

    yield saucedemo_page
    driver.quit()

def test_filtering_name(browser):
    """
    Test to validate filtering functionality by name
    :param browser:
    :return:
    """
    browser.filter.click()
    browser.filter_name_za.click()  # Sort Z-A
    products = browser.item_name_inventory.getItems()

    assert products[0].text == "Test.allTheThings() T-Shirt (Red)"  # Check first item
    product_names = [p.text for p in products]
    #print(product_names)
    assert product_names == sorted(product_names,reverse=True) #Check all item

    #test filtering sort A-Z
    products = []
    browser.filter.click()
    browser.filter_name_az.click()  # Sort A-Z
    products = browser.item_name_inventory.getItems()
    assert products[0].text == "Sauce Labs Backpack"  # Check first item
    product_names = [p.text for p in products]
    assert product_names == sorted(product_names,reverse=False) #check all item

def test_filtering_by_price(browser):
    """
    Test to validate filtering by price option
    :param browser:
    :return:
    """
    browser.filter.click()

    #check products pricing low to high
    browser.filter_price_low_to_high.click()
    products = browser.item_price_inventory.getItems()

    product_prices = [float(p.text.replace('$', '')) for p in products]
    assert product_prices == sorted(product_prices)

    #check products pricing high to low
    products = []
    browser.filter_price_high_to_low.click()
    products = browser.item_price_inventory.getItems()
    product_prices = [float(p.text.replace('$', '')) for p in products]
    assert product_prices == sorted(product_prices,reverse=True)
    

