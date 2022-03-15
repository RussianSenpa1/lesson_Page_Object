from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_SELECTOR = (By.ID, "login_form")
    REGISTER_SELECTOR = (By.ID, "register_form")
