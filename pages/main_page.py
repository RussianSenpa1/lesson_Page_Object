from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):  #Переход на страницу логина
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()


    def should_be_login_link(self):   #Проверка есть ли кнопка логина на странице
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
