import os
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BaseLocator


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        self.check_where_place(BaseLocator.BASE_URL, 'Error initial start yandex page')

    def check_where_place(self, reference, error_text):
        self.browser.get(self.url)
        check_url = self.browser.current_url.strip(' ')
        assert reference in check_url, error_text

    def check_visible_element(self, how_found, selector):
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((how_found, selector)))
            return True
        except:
            return False

    def found_element(self, how_found, selector):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((how_found, selector)))

    def switch_on_page(self, tab_number):
        self.browser.switch_to.window(self.browser.window_handles[tab_number])

    def mouse_move(self):
        x, y = pyautogui.size()
        x = x/2
        y = y/2
        pyautogui.moveTo(x, y, 2, pyautogui.easeInOutQuad)

    def del_temporary_img(self, file_name):
        os.remove(file_name)
