from selenium.webdriver import Keys
from .locators import BasePageLocators, BasePictureLocators
from .locators import BaseLocator
from .base_page import BasePage


class MainPage(BasePage):
    def check_visible_search_panel(self):
        assert self.check_visible_element(*BasePageLocators.SEARCH_BAR_FIND), 'Search field not found'

    def send_data_for_search_panel(self):
        element = self.found_element(*BasePageLocators.SEARCH_BAR_FIND)
        element.send_keys(BaseLocator.SEARCH_DATA)

    def suggest_element_visible(self):
        assert self.check_visible_element(*BasePageLocators.SUGGEST_PANEL), 'Suggest panel not found'

    def press_enter_switch_page_result(self):
        element = self.found_element(*BasePageLocators.SEARCH_BAR_FIND)
        element.send_keys(Keys.RETURN)
        assert self.check_visible_element(*BasePageLocators.RESULT_LIST), 'Switch - Result list not visible'

    def check_one_link_takes_needs_url_website(self):
        link_element = self.found_element(*BasePageLocators.SELECTOR_SEARCH_LIST_URL)
        link_element = link_element.get_attribute('href').strip(' ')
        assert BaseLocator.REFERENCE_URL in link_element, 'Link not found'

    def check_link_picture_is_present(self):
        assert self.check_visible_element(*BasePictureLocators.PICTURE_LINK), 'Picture link not found'

    def go_to_picture_page(self):
        self.found_element(*BasePictureLocators.PICTURE_LINK).click()
        self.switch_on_page(tab_number=1)





