from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_SELECTOR = (By.ID, "login_form")
    REGISTER_SELECTOR = (By.ID, "register_form")

class ProductPageLocators():
    BASKET_SELECTOR = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    NAMEBOOK_SELECTOR = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRICEBOOK_SELECTOR = (By.CLASS_NAME, "price_color")

    NAMEBOOK_SELECTOR_MASSENG = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']//strong")
    PRICEBOOK_SELECTOR_MASSENG = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//strong")