from selenium.webdriver.common.by import By
from tests.conftest import driver


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element_xpath):
        element = self.driver.find_element(By.XPATH, element_xpath)
        return element

    def verify_element_and_text(self, element_xpath, text):
        element = self.find_element(element_xpath)
        if element.text == text:
            return True
        else:
            print(f"Element {element.text} is not equal to {text}")
            return False

    def verify_element_len_and_text_len(self, element_xpath, text):
        element = self.find_element(element_xpath)
        if len(element.text) == len(text):
            return True
        else:
            print(f"Element {element.text} is not equal to {text}")
            return False


    def is_element_on_page(self, element_xpath):
        try:
            self.driver.find_element(By.XPATH, element_xpath)
            return True
        except Exception:
            return False

    def click_element(self, element):
        element.click()

    def send_keys(self, element, value: str):
        element.send_keys(value)

    def implicitly_wait(self, value):
        self.driver.implicitly_wait(value)
