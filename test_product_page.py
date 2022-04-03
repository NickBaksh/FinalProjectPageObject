from .pages.product_page import ProductPage
import time


def test_add_to_basket_and_get_code(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.get_code()
    time.sleep(300)
    page.assert_added_book_have_the_same_name()
    page.assert_same_price_in_basket_and_on_the_page()