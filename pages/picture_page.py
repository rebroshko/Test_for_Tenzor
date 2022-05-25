import time
import requests
from .locators import BaseLocator, BasePictureLocators
from .base_page import BasePage
from .logic_for_hashing import LogicForHashing
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains


class PicturePage(BasePage, LogicForHashing):
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
        #print(text_is_name_cat)
        print(search_data_cat_name)
        assert text_is_name_cat.strip(' ') == search_data_cat_name, 'Category name and search field data dont equal'

    def get_text_from_search_field(self):
        assert self.check_visible_element(*BasePictureLocators.SEARCH_INPUT_FIELD), 'Not found input field'
        search_data_cat_name_id = self.found_element(*BasePictureLocators.SEARCH_INPUT_FIELD)
        Chains = ActionChains(self.browser)
        Chains.double_click(search_data_cat_name_id).perform()
        time.sleep(0.1)
        Chains.click(search_data_cat_name_id)
        Chains.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        search_data_cat_name = pyperclip.paste()
        time.sleep(1)
        #Chains.click(BasePictureLocators.FRAME)
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
        container = self.HASH_CONTAINER
        assert container[0] != container[1], 'Error first and second page have equal hash'

    def download_page(self):
        file_name = 'temporary_img.jpg'
        url = self.get_page_url()
        self.logic_for_download_img(file_name, url)
        self.transform_img_in_hash(file_name)
        self.del_temporary_img(file_name)

    def get_page_url(self):
        assert self.check_visible_element(*BasePictureLocators.PAGE_LINK), 'Not found url for save page'
        url = self.found_element(*BasePictureLocators.PAGE_LINK).get_attribute('href')
        return url

    def logic_for_download_img(self, file_name, url):
        try:
            response = requests.get(url=url)
            with open(file_name, 'wb') as file:
                file.write(response.content)
        except Exception as _ex:
            raise 'Error download image'


