import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import (HOTELS_BUTTON_SELECTOR, GUIDES_BUTTON_SELECTOR,
                    FAVORITES_BUTTON_SELECTOR, FAQ_BUTTON_SELECTOR)


class MainPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.driver.get(url)
        self.driver.maximize_window()
        self.url = url  # Присваиваем атрибут base_url

    def _wait_for_elements(self, locator, multiple=False, timeout=10):
        if multiple:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))
        else:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))

    @allure.step("Проверка заголовка страницы")
    def check_page_title(self, expected_title):
        WebDriverWait(self.driver, 10).until(EC.title_is(expected_title))
        return True

    @allure.step("Открывает главную страницу")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Клик по кнопке Отели")
    def click_hotels_button(self):
        button = self.driver.find_element(By.XPATH, HOTELS_BUTTON_SELECTOR)
        self.driver.execute_script("arguments[0].click();", button)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("/hotels"))

    @allure.step("Возвращает текущий URL страницы")
    def get_current_url(self):
       return self.driver.current_url

    @allure.step("Проверка поля поиска билетов на дату начала")
    def check_time_start(self, expected_title):
        (WebDriverWait
         (self.driver, 10).until(By.CSS_SELECTOR. TIME_START_BUTTON_SELECTOR))
        return True

    @allure.step("Проверка заголовка Путеводитель")
    def click_guides_button(self):
        button = self.driver.find_element(By.XPATH, GUIDES_BUTTON_SELECTOR)
        self.driver.execute_script("arguments[0].click();", button)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("/guides"))

    @allure.step("Проверка заголовка Избранное")
    def click_favorites_button(self):
        button = self.driver.find_element(By.XPATH, FAVORITES_BUTTON_SELECTOR)
        self.driver.execute_script("arguments[0].click();", button)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("/favorites"))

    @allure.step("Проверка заголовка Поддержка")
    def click_faq_button(self):
        button = self.driver.find_element(By.XPATH, FAQ_BUTTON_SELECTOR)
        self.driver.execute_script("arguments[0].click();", button)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.url_contains("/faq"))
