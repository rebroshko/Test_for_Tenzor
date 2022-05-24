import time

import pytest
from pages.main_page import MainPage
from pages.picture_page import PicturePage


@pytest.mark.usefixtures('browser')
def test_picture_on_yandex(browser):
    link = 'https://yandex.ru/'
    page = MainPage(browser, link)          # initial Page Object
    page.open()                                # open_yandex_page
    page.check_link_picture_is_present()
    page.go_to_picture_page()
    picture_page = PicturePage(browser, browser.current_url)   # initial New Object - switch new page
    picture_page.check_correct_switch()
    link_on_first_cat, text_is_name_cat = picture_page.go_to_first_category()      # get new url for relocate in
    photo_category_page = PicturePage(browser, link_on_first_cat)                  # new place and text for next step
    photo_category_page.open()
    # photo_category_page.go_check_equal_search_data_and_cat_name(text_is_name_cat)
    photo_category_page.open_first_photo()
    photo_category_page.check_picture_has_opened_full()
    photo_category_page.download_page()
    photo_category_page.get_slide_to_next_photo()
    time.sleep(1)
    # photo_category_page.download_page()
    # photo_category_page.check_picture_change()
    photo_category_page.get_slide_to_back_photo()
    time.sleep(1)
    # photo_category_page.download_page()



    # Дописать логику для сравнения названия категории и данными в поле , нет данных из поля
    # Скачать фото - (отдельный модуль - создать папку - хешировать = хранить)
    # 6) Проверить, что название категории отображается в поле поиска
    # 10)	Проверить, что картинка сменилась
    # 12)	Проверить, что картинка осталась из шага


    # логирование
    # тестирование без окна

