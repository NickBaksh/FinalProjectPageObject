from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    """
    Метод для перехода к странице авторизации
    """
    def go_to_login_page(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), f"Login link is not presented"
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    '''
    Метод для проверки присутствия элемента на странице
    '''
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    '''
    Метод для проверки отсутствия элемента на странице
    '''
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    '''
    Метод для проверки того, что переданный элемент исчезает со страницы в течение 4 секунд
    '''
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    '''
    Метод для открытия окна браузера с передаваемым url
    '''
    def open(self):
        self.browser.get(self.url)

    '''
    Метод, который проверяет наличие кнопки для перехода в корзину и осуществляет переход в корзину
    '''
    def open_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_BUTTON), f"'Go to basket' button is not presented"
        link = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        link.click()

    '''
    Метод, который проверяет наличие кнопки для перехода на страницу авторизации
    '''
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    '''
    Метод, который проверяет, что пользователь авторизован
    '''
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    '''
    Метод для решения задачки и получения промокода
    '''
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
