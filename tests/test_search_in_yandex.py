import pytest
from pages.main_page import MainPage


@pytest.mark.usefixtures('browser')
def test_yandex_search_output(browser):
    link = 'https://yandex.ru/'
    page = MainPage(browser, link)          # initial Page Object
    page.open()                             # open_yandex_page
    page.check_visible_search_panel()
    page.send_data_for_search_panel()
    page.suggest_element_visible()
    page.press_enter_switch_page_result()

