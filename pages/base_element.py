from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def is_displayed(self):
        return self.web_element.is_displayed()

    def getItems(self):
        return self.driver.find_elements(self.locator.by, self.locator.value)

    def exists(self):
        return self.web_element.exists()

    def is_enabled(self):
        return self.web_element.is_enabled()

    def click(self):
        self.web_element.click()
        return None

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    def text(self):
        text = self.web_element.text
        return text

    def current_url(self):
        return self.web_element.current_url()
        # return None


