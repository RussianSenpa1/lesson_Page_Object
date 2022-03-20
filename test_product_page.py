import faker
import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    name_book, price_book = page.return_name_price()  # Получаем имя и цену товара (до добавления в корзину)
    page.go_to_product_page()  # выполняем метод страницы — добавляем товар в корзину
    page.solve_quiz_and_get_code()  # выполняем метод страницы — решаем пример, вставляем ответ
    page.should_be_basket(namebook=name_book, pricebook=price_book)  # Есть ли товар в козине, имя и цена соответсвует?


@pytest.mark.skip
@pytest.mark.negative_tests
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):  # Проверка - Нет ли сообщения если добавить товар в корзину (должно быть)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.go_to_product_page()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):  # Есть ли сообщение о добавлении, если не добавлять в корзину
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.negative_tests
def test_message_disappeared_after_adding_product_to_basket(
        browser):  # Пропадает ли сообщение о добавления товара в корзину
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser,
                       link)
    page.open()
    page.go_to_product_page()  # выполняем метод страницы — добавляем товар в корзину
    page.should_not_be_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(
        browser):  # Проверка, есть ли кнопка перехода в логин,со страницы товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(
        browser):  # Проверка перехода на страницу логина со страницы товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(
        browser):  # Проверка есть ли в товар и сообщение о его отсутствии
    link = 'https://selenium1py.pythonanywhere.com/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_not_be_success_message()  # Проверка - нет товара
    page.should_be_text_massege()  # Проверка - есть сообщение


class TestUserAddToBasketFromProductPage():  # Класс для работы с функцией setup

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = faker.Faker().email()  # Создание рандомного Email
        password = "BloodTwix775"

        link = "http://selenium1py.pythonanywhere.com"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()  # Переход на старницу логина
        page.register_new_user(email, password)  # Заполнение полей регистрации и регистрация
        page.should_be_authorized_user()  # Проверка, зарегистрировался ли пользователь

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
        page = ProductPage(browser, link)
        page.open()  # открываем страницу

        name_book, price_book = page.return_name_price()
        page.go_to_product_page()  # выполняем метод страницы — добавляем товар в корзину
        page.solve_quiz_and_get_code()  # выполняем метод страницы — решаем пример, вставляем ответ
        page.should_be_basket(namebook=name_book, pricebook=price_book)
