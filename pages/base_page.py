import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_clickable_element(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))

    def find_all_elements(self, locator):
        self.find_clickable_element(locator)
        return self.driver.find_elements(*locator)

    def wait_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 200).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Ждать предзагрузки страницы')
    def wait_invisibility_preload(self):
        self.wait_invisibility_element(PRELOAD_OVERLAY)

    @allure.step('Получить URL страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получить TITLE страницы')
    def get_current_title_page(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/head/title")))
        return self.driver.title

    @allure.step('Переключить вкладку браузера')
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])