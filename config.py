MAIN_URL = 'https://www.aviasales.ru/'
MAIN_PAGE_TITLE = ("Купить авиабилеты дёшево онлайн "
                   "| Авиасейлс — поиск самых дешевых билетов на самолет")

API_SUGGESTED_URL = 'https://suggest.aviasales.com'
API_SEARCH_URL = ''
API_TICKETS_URL = 'https://tickets-api.aviasales.ru'
API_HOTELS_SEARCH = 'https://hotels-api.aviasales.ru/v1/start'
API_TICKETS_NORTH_URL = 'https://tickets-api.eu-north-1.aviasales.ru'

API_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36'
}


HOTELS_PAGE_URL = \
    "https://www.aviasales.ru/hotels?adults=1&source=informing_hotel_tooltip_tabbar"
HOTELS_BUTTON_SELECTOR = '//div[contains(text(), "Отели")]'
TIME_START_BUTTON_SELECTOR = '.s__Ri8DaLigC3WqN5MS5LyK'
GUIDES_BUTTON_SELECTOR = '//div[contains(text(), "Короче")]'
FAVORITES_BUTTON_SELECTOR = '//div[contains(text(), "Избранное")]'
FAQ_BUTTON_SELECTOR = '//div[contains(text(), "Поддержка")]'
# HOTELS_PAGE_TITLE = ("/hotels")
