from base.selenium_base import SeleniumBase
from locators.locators import ShopingCartLocators


class ShopingCartPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def should_have_url(self):
        url = self.driver.current_url
        assert url == ShopingCartLocators.URL, f"Shoping cart url is incorrect {url}"
