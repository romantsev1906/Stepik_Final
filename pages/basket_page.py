from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_basket_description_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_DESCRIPTION_MESSAGE), \
            "Product description message is presented, but should not be"

    def should_be_basket_empty_message(self):
        basket_empty_message = self.get_elem_text_on_page(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert "Your basket is empty" in basket_empty_message or "Ваша корзина пуста" in basket_empty_message, \
               "The basket should be empty!"