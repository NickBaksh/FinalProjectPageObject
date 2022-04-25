from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """
    Объединение проверок на наличие элементов страницы авторизации в один метод
    """
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    """
    Метод, который проверяет что текущий url соответствует странице авторизации
    """
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"User was redirected to a wrong page"
        assert True

    """
    Метод, который проверяет что на странице присутствует форма авторизации
    """
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), f"Login form is not presented"
        assert True

    """
    Метод, который проверяет что на странице присутствует форма регистрации
    """
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), f"Registration form is not presented"
        assert True

    """
    Метод, который заполняет обязательные поля при регистрации и регистрирует нового пользователя
    """
    def register_new_user(self, email, password):
        """
        В форме регистрации находим поле почтового адреса. И заполняем его значением из переменной 'email'
        """
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), f"Email input in registration form is not presented"
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)

        """
        Находим поле для ввода пароля. И заполняем его значением из переменной 'password' 
        """
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), f"Password input in registration form is not presented"
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field.send_keys(password)

        """
        Находим поле для подтверждения пароля. И заполняем его значением из переменной 'password' 
        """
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRMATION), f"Password confirmation input in registration form is not presented"
        password_confirmation_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRMATION)
        password_confirmation_field.send_keys(password)

        """
        Находим кнопку 'Зарегистрироваться' и нажимаем на нее 
        """
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), f"Submit registration button is not presented"
        submit_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        submit_registration.click()