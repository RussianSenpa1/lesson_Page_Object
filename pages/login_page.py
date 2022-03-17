from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_url(self):
        assert "login" in self.url, "URL is not Login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_SELECTOR), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_SELECTOR), "Register form is not presented"