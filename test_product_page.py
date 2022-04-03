from .pages.product_page import ProductPage


def test_add_to_basket_and_get_code(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.product_add_to_basket()
    page.get_code()
    page.assert_added_book_have_the_same_name()
    page.assert_same_price_in_basket_and_on_the_page()