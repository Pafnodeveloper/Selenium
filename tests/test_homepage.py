import pytest
from pom.homepage import HomePage
from pom.product_page import ProductPage
from pom.shoping_cart_page import ShopingCartPage


@pytest.mark.usefixtures("setup")
class TestHomepage:

    def test_homepage(self):
        home_page = HomePage(self.driver)
        web_el = home_page.get_logo()
        assert web_el.text == "Your Store"

        elems = home_page.get_all_available_menu()
        for idx in range(len(elems)):
            home_page.get_all_available_menu()[idx].click()

    def test_switch_to_your_basket(self):
        home_page = HomePage(self.driver)
        home_page.go_to_your_basket()
        shoping_cart_page = ShopingCartPage(self.driver)
        shoping_cart_page.should_have_url()

    def test_add_to_cart(self):
        home_page = HomePage(self.driver)
        product_name = home_page.get_product_name()
        home_page.open_product()
        product_page = ProductPage(self.driver)
        product_page.add_to_cart()
        product_page.check_cart()
        product_name_in_cart = product_page.get_cart_product_name()
        product_page.should_have_same_text(product_name, product_name_in_cart)
