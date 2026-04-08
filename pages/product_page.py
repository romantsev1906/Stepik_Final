from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        btn_basket = self.browser.find_element(*ProductPageLocators.BTN_BASKET)
        btn_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_btn_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_BASKET), "Button 'Add to Basket ' is not presented"

    def should_be_the_same_name(self):
        product_name = self.get_elem_text_on_page(*ProductPageLocators.PRODUCT_NAME)
        product_name_basket = self.get_elem_text_on_page(*ProductPageLocators.PRODUCT_NAME_BASKET)
        assert product_name_basket == product_name, "Wrong NAME product added to basket!"

    def should_be_the_same_price(self):
        product_price = self.get_elem_text_on_page(*ProductPageLocators.PRODUCT_PRICE)
        product_price_basket = self.get_elem_text_on_page(*ProductPageLocators.PRODUCT_PRICE_BASKET)
        assert product_price_basket == product_price, "Wrong PRICE product added to basket!"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is dissapear, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"