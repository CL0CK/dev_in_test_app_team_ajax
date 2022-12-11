from framework.page import Page
from framework.login_consts import LoginConsts
from tests.conftest import driver


class LoginPage(Page):

    def __init__(self, driver: driver):
        super().__init__(driver)

    def click_first_login(self):
        element = self.find_element(LoginConsts.FIRST_LOGIN)
        self.click_element(element)

    def verify_email_value(self, value):
        return self.verify_element_and_text(LoginConsts.EMAIL, value)

    def verify_password_value(self, value):
        return self.verify_element_len_and_text_len(LoginConsts.PASSWORD, value)

    def click_second_login(self):
        element = self.find_element(LoginConsts.SECOND_LOGIN)
        self.click_element(element)

    def set_email(self, value):
        element = self.find_element(LoginConsts.EMAIL)
        self.send_keys(element, value)

    def set_password(self, value):
        element = self.find_element(LoginConsts.PASSWORD)
        self.send_keys(element, value)

    def login_to_application(self, email, password):
        self.implicitly_wait(5)
        self.click_first_login()
        self.set_email(email)
        self.set_password(password)
        self.click_second_login()

    def allow_location(self):
        self.switch_to_alert()
        element = self.find_element('Allow Ajax to access this device’s location?')
        self.click_element(element)
        # alert = self.switch_to_alert()
        # alert.accept()
