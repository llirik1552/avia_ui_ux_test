import pytest
import allure
from pages.api_page import ApiPage
from config import API_SUGGESTED_URL, API_HOTELS_SEARCH


@pytest.fixture
def api_suggested_page():
    return ApiPage(API_SUGGESTED_URL)


@pytest.fixture
def api_search_hotels():
    return ApiPage(API_HOTELS_SEARCH)


@allure.epic("API")
@allure.feature("Поиск города")
@allure.title("поиск города по коду '{term}'")
@pytest.mark.positive
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.parametrize("locale, term, name", [
    ("ru_RU", "KUF", "Самара"),
    ("ru_RU", "LED", "Санкт-Петербург"),
    ("en_EN", "BUE", "Buenos Aires"),
])
def test_register_with_ru_email(api_suggested_page, locale, term, name):
    with allure.step("Отправляем запрос на регистрацию с email  в домене ru"):
        response = api_suggested_page.get_city_by_term(locale, term)
    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200, "Ожидается статус код 200"
        print(response)
    with allure.step("Проверяем название города"):
        assert response.json()[0]["name"] == name, \
            f"Ожидается название города '{name}'"


@allure.epic("API")
@allure.feature("Поиск города")
@allure.title("проверка поиска города с пустым кодом")
@pytest.mark.negative
@pytest.mark.api
def test_search_city_with_empty_code(api_suggested_page):
    with allure.step("Отправляем запрос на поиск города с пустым кодом"):
        response = api_suggested_page.get_city_by_term("ru_RU", "")
    with allure.step("Проверяем статус-код для пустого кода"):
        assert response.status_code == 400, "Ожидается статус код 400"
        print(response)


@allure.epic("API")
@allure.feature("Поиск отеля")
@allure.title("Поиск отеля на дату '23 июля 2025 года'")
@pytest.mark.api
def test_search_ticket_on_date(api_search_hotels):
    test_date_start = "2025-07-23"  # Дата начала бронирования
    test_date_end = "2025-07-30"  # Дата окончания
    with (allure.step(f"Отправляем запрос на поиск билетов на дату "
                     f"{test_date_start} - {test_date_end}")):
        response = api_search_hotels.search_hotels_by_date(test_date_start,
                                                           test_date_end)
    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200, "Ожидается статус код 200"
        print(response)
    with allure.step("Проверяем наличие данных о отелях"):
        assert len(response.json()) > 0, "Ожидаются результаты поиска отелей"


@allure.epic("API")
@allure.feature("Поиск отеля для детей без взрослых")
@allure.title("Поиск отеля на дату '23 июля 2025 года'")
@pytest.mark.api
def test_search_ticket_childless(api_search_hotels):
    test_date_start = "2025-07-23"  # Дата начала бронирования
    test_date_end = "2025-07-30"  # Дата окончания
    with allure.step(f"Отправляем запрос на поиск билетов "
                     f"на дату {test_date_start} - {test_date_end}"):
        response = api_search_hotels.search_hotels_childless(test_date_start,
                                                             test_date_end)
    with allure.step("Проверяем статус-код"):
        assert response.status_code == 400, "Ожидается статус код 400"
        print(response)
