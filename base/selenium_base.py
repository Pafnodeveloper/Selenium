from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 0.3)

    def __get_selenium_by(self, find_by: str):
        find_by = find_by.lower()
        locating = {
            "id": By.ID,
            "xpath": By.XPATH,
            "link text": By.LINK_TEXT,
            "partial link text": By.PARTIAL_LINK_TEXT,
            "name": By.NAME,
            "tag": By.TAG_NAME,
            "class": By.CLASS_NAME,
            "css": By.CSS_SELECTOR,
        }
        return locating[find_by]

    def is_visible(self, find_by, locator):
        return self.wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)))

    def is_present(self, find_by, locator):
        return self.wait.until_not(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)))

    def is_not_present(self, find_by, locator):
        return self.wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)))

    def are_visible(self, find_by, locator):
        return self.wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)))

    def are_present(self, find_by, locator):
        return self.wait.until_not(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)))
