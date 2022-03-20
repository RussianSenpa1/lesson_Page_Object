from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,
                    link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу

    name_book, price_book = page.return_name_price()
    page.go_to_product_page()  # выполняем метод страницы — добавляем товар в корзину
    page.solve_quiz_and_get_code() # выполняем метод страницы — решаем пример, вставляем ответ
    page.should_be_basket(namebook = name_book, pricebook = price_book)







