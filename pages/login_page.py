import time

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_url(self):
        assert "login" in self.url, "URL is not Login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_SELECTOR), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_SELECTOR), "Register form is not presented"

    def register_new_user(self, email, password):

        mail = self.browser.find_element(*LoginPageLocators.EMAIL_SELECTOR)
        mail.send_keys(str(email))
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        password1.send_keys(str(password))
        password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        password2.send_keys(str(password))
        register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register.click()

