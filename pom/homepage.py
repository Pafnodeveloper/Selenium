from base.selenium_base import SeleniumBase
from locators.locators import HomePageLocators


class HomePage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def get_logo(self):
        return self.is_visible(*HomePageLocators.LOGO)

    def get_all_available_menu(self):
        return self.are_visible(*HomePageLocators.DROPDOWNS)

    def get_text(self, elements):
        texts = [el.text for el in elements]
        return texts

    def go_to_your_basket(self):
        checkout_btn = self.is_visible(*HomePageLocators.CHECKOUT)
        checkout_btn.click()

    def open_product(self):
        product = self.is_visible(*HomePageLocators.PRODUCT)
        product.click()

    def get_product_name(self):
        product = self.is_visible(*HomePageLocators.PRODUCT_NAME)
        return product.text
