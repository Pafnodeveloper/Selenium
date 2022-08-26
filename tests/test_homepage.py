import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pom.homepage import HomePage


@pytest.mark.usefixtures("setup")
class TestHomepage:

    def test_homepage(self):
        home_page = HomePage(self.driver)
        web_el = home_page.get_logo()
        assert web_el.text == "Your Store"

        elems = home_page.get_all_available_menu()
        for idx in range(len(elems)):
            home_page.get_all_available_menu()[idx].click()
