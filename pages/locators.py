from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_BASKET_BASE = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_DESCRIPTION_MESSAGE = (By.XPATH, "//h2[@class='col-sm-6 h3']")
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//*[@id='content_inner']/p")

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//*[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//*[@id='register_form']")
    INPUT_EMAIL = (By.XPATH, "//*[@id='id_registration-email']")
    INPUT_PASSWORD = (By.XPATH, "//*[@id='id_registration-password1']")
    INPUT_CONFIRM_PASSWORD = (By.XPATH, "//*[@id='id_registration-password2']")
    BTN_REGISTER_SUBMIT = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators():
    BTN_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_NAME = (By.XPATH, "//*[@class='active']")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    PRODUCT_NAME_BASKET = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRODUCT_PRICE_BASKET = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]")



