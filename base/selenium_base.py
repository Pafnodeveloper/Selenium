from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 0.3)

    def get_current_url(self):
        return self.driver.current_url

    def is_visible(self, find_by, locator):
        return self.wait.until(ec.visibility_of_element_located((find_by, locator)))

    def is_present(self, find_by, locator):
        return self.wait.until_not(ec.presence_of_element_located((find_by, locator)))

    def is_not_present(self, find_by, locator):
        return self.wait.until(ec.visibility_of_element_located((find_by, locator)))

    def is_clickable(self, find_by, locator):
        return self.wait.until(ec.element_to_be_clickable((find_by, locator)))

    def are_visible(self, find_by, locator):
        return self.wait.until(ec.visibility_of_all_elements_located((find_by, locator)))

    def are_present(self, find_by, locator):
        return self.wait.until_not(ec.presence_of_all_elements_located((find_by, locator)))

    def should_have_same_text(self, txt1, txt2):
        assert txt1 == txt2, f"{txt1} is not equal {txt2}"
