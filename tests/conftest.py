import pytest
from selenium import webdriver
from selenium.webdriver.common.options import ArgOptions as chrome_options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def get_options():
    options = chrome_options()
    options.add_argument("chrome")
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    return options


@pytest.fixture
def get_webdriver(get_options):
    options = get_options
    # driver = webdriver.Chrome(ChromeDriverManager(version="104.0.5112.79").install())
    driver = webdriver.Chrome(executable_path="D:/Programs/PP/Selenium/chromedriver.exe", options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = "http://www.tutorialsninja.com/demo/"
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
