from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_SELECTOR = (By.ID, "login_form")
    REGISTER_SELECTOR = (By.ID, "register_form")
    EMAIL_SELECTOR = (By.NAME, "registration-email")
    PASSWORD1 = (By.NAME, "registration-password1")
    PASSWORD2 = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    BASKET_SELECTOR = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    NAMEBOOK_SELECTOR = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRICEBOOK_SELECTOR = (By.CLASS_NAME, "price_color")
    NAMEBOOK_SELECTOR_MASSENG = (
        By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']//strong")
    PRICEBOOK_SELECTOR_MASSENG = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default']")
    BOOK_SELECTOR = (By.CLASS_NAME, "basket-items")
    TEXT_SELECTOR = (By.XPATH, '//*[@id="content_inner"]/p')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
