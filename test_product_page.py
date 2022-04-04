import pytest
from .pages.product_page import ProductPage

c = []
for num in range(10):
    c.append(num)


@pytest.mark.parametrize('promo', c)
def test_add_to_basket_and_get_code(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.get_code()
    page.elements_should_be_presented()
    page.assert_added_book_have_the_same_name()
    page.assert_same_price_in_basket_and_on_the_page()