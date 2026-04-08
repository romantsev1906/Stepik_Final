import pytest
import time
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
product_any_link  = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", "1@2QWE_hjk45")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_any_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_any_link)
        page.open()
        page.should_be_btn_basket()
        page.add_product_to_basket()
        page.should_be_the_same_name()
        page.should_be_the_same_price()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                       marks=pytest.mark.xfail(reason="fixing this bug right now (promo=offer7)")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_btn_basket()
    page.add_product_to_basket()
    page.should_be_the_same_name()
    page.should_be_the_same_price()

@pytest.mark.xfail(reason="fixing this bug right now (Test 1)")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now (Test 3)")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_product_to_basket()
    page.should_dissapear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_any_link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
    page = ProductPage(browser, product_any_link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_any_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_description_message()
    basket_page.should_be_basket_empty_message()
