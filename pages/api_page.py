import allure
import requests
from faker import Faker
from config import API_HEADERS


class ApiPage:
    def __init__(self, url):
        self.url = None
        self.base_url = url
        self.fake = Faker()
        self.headers = API_HEADERS

    @allure.step("Отправка запроса на поиск города по коду '{term}'")
    def get_city_by_term(self, locale, term):
        """Метод для поиска города по коду аэропорта"""
        url = f"{self.base_url}/v2/code_to_places.json"

        params = {
            "locale": locale,
            "term": term
        }
        return requests.get(url, headers=self.headers, params=params)

    @allure.step("Поиск билетов по дате '{date_start}' - '{date_end}'")
    def search_hotels_by_date(self, date_start, date_end):

        body = {
    "location_id": "2416",
    "location_type": "city",
    "gate_id": "ostrovok",
    "checkin": date_start,
    "checkout": date_end,
    "guests": {
        "adults": 1,
        "children": []
    },
    "locale": "ru_RU"
    }
        response = requests.post(self.base_url,
                                 headers=self.headers, json=body)
        print(response.json())
        return response

    @allure.step("Поиск отеля для детей без "
                 "взрослых '{date_start}' - '{date_end}'")
    def search_hotels_childless(self, date_start, date_end):

        body = {

    "location_id": "2416",
    "location_type": "city",
    "gate_id": "ostrovok",
    "checkin": date_start,
    "checkout": date_end,
    "guests": {
        "adults": 0,
        "children": [1]
    },
    "locale": "ru_RU"
    }
        response = requests.post(self.base_url,
                                 headers=self.headers, json=body)
        print(response.json())
        return response
