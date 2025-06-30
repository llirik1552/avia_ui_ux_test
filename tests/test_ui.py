import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from config import MAIN_URL, MAIN_PAGE_TITLE, TIME_START_BUTTON_SELECTOR


@pytest.fixture
def main_page():
    driver = webdriver.Chrome()
    page = MainPage(driver, MAIN_URL)
    yield page
    driver.quit()


@allure.epic("UI")
@allure.feature("Smoke")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    with allure.step("Заголовок главной страницы"):
        assert main_page.check_page_title(MAIN_PAGE_TITLE)


@allure.epic("UI")
@allure.feature("Smoke")
@allure.title("Проверка перехода на страницу отелей")
@pytest.mark.smoke
def test_navigate_to_hotels_page(main_page):
    with allure.step("Переход на главную страницу"):
        main_page.check_page_title(MAIN_PAGE_TITLE)

    with allure.step("Нажатие кнопки 'Отели'"):
        main_page.click_hotels_button()

    with allure.step("Проверка URL страницы"):
        current_url = main_page.get_current_url()
        assert "hotels" in current_url


@allure.epic("UI")
@allure.feature("Smoke")
@allure.title("Проверка поля ввода даты")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    with allure.step("Поле даты начала"):
        assert main_page.check_time_start(TIME_START_BUTTON_SELECTOR)


@allure.epic("UI")
@allure.feature("Smoke")
@allure.title("Проверка перехода на страницу путеводителя")
@pytest.mark.smoke
def test_navigate_to_guides_page(main_page):
    with allure.step("Переход на главную страницу"):
        main_page.check_page_title(MAIN_PAGE_TITLE)

    with allure.step("Нажатие кнопки 'Короче'"):
        main_page.click_guides_button()

    with allure.step("Проверка URL страницы"):
        current_url = main_page.get_current_url()
        assert "guides" in current_url


@allure.epic("UI")
@allure.feature("Smoke")
@allure.title("Проверка перехода на страницу Избранное")
@pytest.mark.smoke
def test_navigate_to_favorite_page(main_page):
    with allure.step("Переход на главную страницу"):
        main_page.check_page_title(MAIN_PAGE_TITLE)

    with allure.step("Нажатие кнопки 'Избранное'"):
        main_page.click_favorites_button()

    with allure.step("Проверка URL страницы"):
        current_url = main_page.get_current_url()
        assert "favorites" in current_url


@allure.epic("UI")
@allure.feature("Smoke")
@allure.title("Проверка перехода на страницу Поддержка")
@pytest.mark.smoke
def test_navigate_to_faq_page(main_page):
    with allure.step("Переход на главную страницу"):
        main_page.check_page_title(MAIN_PAGE_TITLE)

    with allure.step("Нажатие кнопки 'Поддержка'"):
        main_page.click_faq_button()

    with allure.step("Проверка URL страницы"):
        current_url = main_page.get_current_url()
        assert "faq" in current_url
