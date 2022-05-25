import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def get_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--log-level=DEBUG')
    return options


@pytest.fixture(scope='function')
def browser(get_chrome_options):
    options = get_chrome_options
    path_driver = Service()  # Driver Chrome path
    browser = webdriver.Chrome(service=path_driver, options=options)
    yield browser
    browser.quit()
