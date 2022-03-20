from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BASKET_SELECTOR)
        button_basket.click()

    def return_name_price(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAMEBOOK_SELECTOR)
        price_book = self.browser.find_element(*ProductPageLocators.PRICEBOOK_SELECTOR)
        return (name_book.text, price_book.text)

    def should_be_basket(self, namebook,
                         pricebook):  # Проверка - товар добавлен в корзину, его имя и цена соответствуют
        name_book_masseng = (self.browser.find_element(*ProductPageLocators.NAMEBOOK_SELECTOR_MASSENG)).text
        price_book_masseng = (self.browser.find_element(*ProductPageLocators.PRICEBOOK_SELECTOR_MASSENG)).text
        assert name_book_masseng == namebook and price_book_masseng == pricebook, "book is not true name and price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be is_disappeared"
