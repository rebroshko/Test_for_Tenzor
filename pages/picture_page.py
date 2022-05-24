import time
import urllib
import requests
from .locators import BaseLocator, BasePictureLocators
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains


class PicturePage(BasePage):
    def check_correct_switch(self):
        self.check_where_place(BaseLocator.REFERENCE_SWITCH_URL, 'Error switch to picture page - error link')

    def go_to_first_category(self):
        assert self.check_visible_element(*BasePictureLocators.LINK_ON_FIRST_CATEGORY), 'First category not found'
        link_on_first_cat, text_is_name_cat = self.get_name_first_category_and_switch()
        return link_on_first_cat, text_is_name_cat

    def get_name_first_category_and_switch(self):
        value = self.found_element(*BasePictureLocators.LINK_ON_FIRST_CATEGORY)  # First found element
        link_on_first_cat = value.get_attribute('href')  # Link on first category
        text_is_name_cat = value.get_attribute('text')  # First category name
        return link_on_first_cat, text_is_name_cat

    def go_check_equal_search_data_and_cat_name(self, text_is_name_cat):
        search_data_cat_name = self.get_text_from_search_field()
        assert text_is_name_cat == search_data_cat_name, 'Category name and search field data dont equal'

    def get_text_from_search_field(self):
        assert self.check_visible_element(*BasePictureLocators.SEARCH_INPUT_FIELD), 'Not found input field'
        search_data_cat_name = self.found_element(*BasePictureLocators.SEARCH_INPUT_FIELD).get_attribute('text')
        print(f'ТУТ ДОЛЖНА БЫТЬ СТРОКА {search_data_cat_name}')
        time.sleep(5)
        return search_data_cat_name

    def open_first_photo(self):
        assert self.check_visible_element(*BasePictureLocators.FIRST_PHOTO_IN_CATEGORY), 'First photo not found'
        self.found_element(*BasePictureLocators.FIRST_PHOTO_IN_CATEGORY).click()         # Open first photo

    def check_picture_has_opened_full(self):
        assert self.found_element(*BasePictureLocators.PHOTO_FRAME), "Picture not open full"

    def get_slide_to_next_photo(self):
        self.mouse_move()
        assert self.check_visible_element(*BasePictureLocators.NEXT_BUTTON), 'Next button not found'
        button = self.found_element(*BasePictureLocators.NEXT_BUTTON)
        button.click()

    def get_slide_to_back_photo(self):
        self.mouse_move()
        assert self.check_visible_element(*BasePictureLocators.BACK_BUTTON), 'Back button not found'
        self.found_element(*BasePictureLocators.BACK_BUTTON).click()

    def check_picture_change(self):
        pass

    def download_page(self):
        assert self.check_visible_element(*BasePictureLocators.PICTURE_LINK), 'Not found url for save page'
        url = self.found_element(*BasePictureLocators.PICTURE_LINK).get_attribute('href')
        print(url)

