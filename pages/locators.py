from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#ogin_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#egister_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "<h1>")
    SUCCESS_ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages strong")
    MESSAGE_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")