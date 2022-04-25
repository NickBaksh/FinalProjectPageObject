from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"User was redirected to a wrong page"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), f"Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), f"Registration form is not presented"
        assert True

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), f"Email input in registration form is not presented"
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)

        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), f"Password input in registration form is not presented"
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field.send_keys(password)

        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRMATION), f"Password confirmation input in registration form is not presented"
        password_confirmation_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRMATION)
        password_confirmation_field.send_keys(password)

        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), f"Submit registration button is not presented"
        submit_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        submit_registration.click()