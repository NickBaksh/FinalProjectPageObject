from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    REGISTRATION_PASSWORD = (By.XPATH, "//input[@name='registration-password1']")
    REGISTRATION_PASSWORD_CONFIRMATION = (By.XPATH, "//input[@name='registration-password2']")
    REGISTRATION_SUBMIT_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    SUCCESS_ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages strong")
    MESSAGE_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    CONTINUE_SHOPPING_LINK = (By.CSS_SELECTOR, "div#content_inner p a")
    BASKET_WITH_PRODUCT = (By.CSS_SELECTOR, "#basket_formset")