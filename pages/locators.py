from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_LINK = (By.XPATH, "//a[contains(@href, 'basket')]")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    PRODUCT_PRICE_ACTUAL = (By.CSS_SELECTOR, "div.product_main > p")
    PRODUCT_TITLE_ACTUAL = (By.CSS_SELECTOR, "div.product_main > h1")
    ADD_BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "#messages strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages p strong")
