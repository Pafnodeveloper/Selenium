from base.selenium_base import SeleniumBase


class HomePage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.__logo = "#logo"
        self.__nav_dropdowns = ".nav > li"

    def get_logo(self):
        return self.is_visible("css", self.__logo)

    def get_all_available_menu(self):
        return self.are_visible("css", self.__nav_dropdowns)

    def get_text(self, elements):
        texts = [el.text for el in elements]
        return texts
