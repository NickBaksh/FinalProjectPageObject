from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage, ProductPageLocators):
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), f"Add to basket button is not presented"

    def product_add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def get_code(self):
        self.solve_quiz_and_get_code()

    def successful_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), f"Success add to basket " \
                                                                                            f"message is not presented "

    def assert_added_book_have_the_same_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text

        success_message_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE)
        success_message_product_name_text = success_message_product_name.text

        assert product_name_text == success_message_product_name_text, f"Incorrect product was added to the basket"

    def assert_same_price_in_basket_and_on_the_page(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text

        basket_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE)
        basket_price_text = basket_price.text

        assert product_price_text == basket_price_text, f"Basket price and product price on the page are not the same"
