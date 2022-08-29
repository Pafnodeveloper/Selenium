from selenium.webdriver.common.by import By


class HomePageLocators:
    CHECKOUT = (By.CSS_SELECTOR, "[title='Checkout']")
    LOGO = (By.ID, "logo")
    DROPDOWNS = (By.CSS_SELECTOR, ".nav > li")
    PRODUCT = (By.CSS_SELECTOR, ".product-layout a")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-layout h4 > a")


class ShopingCartLocators:
    URL = "http://tutorialsninja.com/demo/index.php?route=checkout/cart"


class ProductLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "[id=button-cart]")
    BASKET = (By.CSS_SELECTOR, "#cart > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".text-left > a")
