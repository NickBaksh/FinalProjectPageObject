from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING_LINK), f"Go to shopping link is not presented"

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_WITH_PRODUCT), f"Basket is not empty"
