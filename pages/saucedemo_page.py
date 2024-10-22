from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator
from .base_page import BasePage

class SaucedemoPage(BasePage):

    url = 'https://www.saucedemo.com/'

# locator page_title used for each page verification
    @property
    def page_title(self):
        locator = Locator(By.CLASS_NAME, "title")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def swaglabs_login_logo(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="login_logo"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def username_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="user-name"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def password_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="password"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_button(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="login-button"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_error(self):
        locator = Locator(By.CSS_SELECTOR, 'h3[data-test="error"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def search_input(self):
        locator = Locator(By.CSS_SELECTOR, "input[placeholder='Search…']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def search_button(self):
        locator = Locator(By.CSS_SELECTOR, "button[type='submit']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def burger_menu_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="react-burger-menu-btn"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def logout_sidebar_link(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="logout_sidebar_link"]')
        return BaseElement(driver=self.driver, locator=locator)

    # sauce labs fleece jacket
    @property
    def item_5_title_link_inventory(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="item_5_title_link"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def item_name_inventory(self):
        locator = Locator(By.CLASS_NAME, "inventory_item_name")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def item_desc_inventory(self):
        locator = Locator(By.CLASS_NAME, "inventory_item_desc")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def item_price_inventory(self):
        locator = Locator(By.CLASS_NAME, "inventory_item_price")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def no_result_search(self):
        locator = Locator(By.CSS_SELECTOR, ".no-results")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def item_5_title_link_detail(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="inventory_details_name large_size"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def item_title_link_detail_desc(self):
        locator = Locator(By.CSS_SELECTOR, 'div[class="inventory_details_desc large_size"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def back_to_products_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="back-to-products"]')
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def add_to_cart_item_5(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-fleece-jacket"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def remove_item_5(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="remove-sauce-labs-fleece-jacket"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_to_cart_item_4(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-backpack"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def remove_item_4(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="remove-sauce-labs-backpack"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_to_cart_item(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="add-to-cart"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def remove_item(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="remove"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def removed_cart_item(self):
        locator = Locator(By.CLASS_NAME, "removed_cart_item")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def shopping_cart_button(self):
        locator = Locator(By.CLASS_NAME, "shopping_cart_link")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def shopping_cart_badge(self):
        locator = Locator(By.CLASS_NAME, "shopping_cart_badge")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def shopping_cart_list(self):
        locator = Locator(By.CLASS_NAME, "cart_list")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def shopping_cart_item(self):
        locator = Locator(By.CLASS_NAME, "cart_item")
        return BaseElement(driver=self.driver, locator=locator)


    @property
    def checkout_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="checkout"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def finish_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[id="finish"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def summary_sub_total(self):
        locator = Locator(By.CLASS_NAME, 'summary_subtotal_label')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def order_complete(self):
        locator = Locator(By.CLASS_NAME, 'complete-header')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def quantity_input(self):
        locator = Locator(By.CLASS_NAME, 'cart_quantity')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def first_name_input_text(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="first-name"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def last_name_input_text(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="last-name"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def postal_code_input_text(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="postal-code"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def continue_button(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="continue"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def filter(self):
        locator = Locator(By.CSS_SELECTOR, "select[data-test='product-sort-container']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def filter_name_az(self):
        locator = Locator(By.CSS_SELECTOR, "option[value='az']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def filter_name_za(self):
        locator = Locator(By.CSS_SELECTOR, "option[value='za']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def filter_price_low_to_high(self):
        locator = Locator(By.CSS_SELECTOR, "option[value='lohi']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def filter_price_high_to_low(self):
        locator = Locator(By.CSS_SELECTOR,"option[value='hilo']")
        return BaseElement(driver=self.driver, locator=locator)