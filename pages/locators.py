from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_BAR_FIND = (By.XPATH, '//*[@id="text"]')              # Search element Xpath.
    SUGGEST_PANEL = (By.XPATH, '/html/body/div[2]')
    RESULT_LIST = (By.ID, 'search-result')
    SELECTOR_SEARCH_LIST_URL = (By.CSS_SELECTOR, 'a[href*="tensor.ru"]')


class BaseLocator:
    BASE_URL = 'https://yandex.ru/'
    SEARCH_DATA = 'Тензор'
    REFERENCE_URL = 'tensor.ru'
    REFERENCE_SWITCH_URL = 'https://yandex.ru/images/'


class BasePictureLocators:
    PICTURE_LINK = (By.LINK_TEXT, 'Картинки')
    LINK_ON_FIRST_CATEGORY = (By.XPATH, '//div[2]/div/div/div/div/a')
    SEARCH_INPUT_FIELD = (By.XPATH, '/html/head/title')
    FIRST_PHOTO_IN_CATEGORY = (By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div')
    PHOTO_FRAME = (By.XPATH, '/html/body/div[12]/div[2]/div/div/div/div[3]')
    NEXT_BUTTON = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_next.CircleButton_type.MediaViewer-Button')
    BACK_BUTTON = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_prev.CircleButton_type.MediaViewer-Button')
    PAGE_LINK = (By.CSS_SELECTOR, '/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/div/img')


