from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_should_see_login_link(browser):         #Проверка есть ли кнопка логина на странице
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_url(browser):  # Проверка есть ли login в url
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,
                    link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()  # Проверка есть ли login в url

def test_guest_should_see_login_form(browser):  #Проверка присутствия формы логина
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()

def test_guest_should_see_register_form(browser):  #Проверка присутствия формы регистрации
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_register_form()