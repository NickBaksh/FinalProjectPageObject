import pytest
from .pages.product_page import ProductPage


#@pytest.mark.parametrize('promo', ["1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
#def test_add_to_basket_and_get_code(browser, promo):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    #page = ProductPage(browser, link)
    #page.open()
    #page.product_add_to_basket()
    #page.get_code()
    #page.elements_should_be_presented()
    #page.assert_added_book_have_the_same_name()
    #page.assert_same_price_in_basket_and_on_the_page()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.should_dissapear_of_success_message()
