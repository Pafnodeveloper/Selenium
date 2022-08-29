from base.selenium_base import SeleniumBase
from locators.locators import ProductLocators


class ProductPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart(self):
        btn = self.is_clickable(*ProductLocators.ADD_TO_BASKET)
        btn.click()

    def check_cart(self):
        cart = self.is_clickable(*ProductLocators.BASKET)
        cart.click()

    def get_cart_product_name(self):
        product_in_cart = self.is_visible(*ProductLocators.PRODUCT_NAME)
        return product_in_cart.text
