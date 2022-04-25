from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage, ProductPageLocators):
    """
    Находим кнопку 'Добавить в корзину' и нажимаем на нее
    """
    def product_add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    """
    Проверка того, что название и цена продукта отображаются на странице
    """
    def elements_should_be_presented(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), f"Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), f"Product price is not presented"

    """
    Проверка того, что без добавления товара в корзину сообщение об успешном добавлении товара не должно отображаться
    """
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), f"Success add to " \
                                                                                                f"basket message is " \
                                                                                                f"presented "

    """
    Проверка того, что сообщение об успешном добавлении товара в корзину исчезает со страницы
    """
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), f"Success add to basket message " \
                                                                                        f"is not dissapear"

    """
    Метод для решения задачки и получения проверочного кода
    """
    def get_code(self):
        self.solve_quiz_and_get_code()

    """
    Проверка того, что сообщение об успешном добавлении товара отображается после добавления товара в корзину
    """
    def successful_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), f"Success add to basket " \
                                                                                            f"message is not presented "

    """Проверка того, что название книги в сообщении об успешном добавлении в корзину и название книги на странице 
    товара совпадают """
    def assert_added_book_have_the_same_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text

        success_message_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE)
        success_message_product_name_text = success_message_product_name.text

        assert product_name_text == success_message_product_name_text, f"Incorrect product was added to the basket"

    """
    Проверка того, что цена товара на странице товара и цена в корзине совпадают
    """
    def assert_same_price_in_basket_and_on_the_page(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text

        basket_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE)
        basket_price_text = basket_price.text

        assert product_price_text == basket_price_text, f"Basket price and product price on the page are not the same"
