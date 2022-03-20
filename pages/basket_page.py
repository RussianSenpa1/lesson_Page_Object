from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_not_be_success_message(self):  # Проверка - овара нет а корзине
        assert self.is_not_element_present(
            *BasePageLocators.BOOK_SELECTOR), "Success message is presented, but should not be"

    def should_be_text_massege(self):  # Проверка - есть ли текст о том, что корзина пуста
        assert self.browser.find_element(*BasePageLocators.TEXT_SELECTOR), "not text"
