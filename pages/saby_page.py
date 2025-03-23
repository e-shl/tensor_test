import time

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.saby_page_locators import *
from pages.base_page import BasePage
from tests_data import *
from urls import *


class SabyPage(BasePage):

    @allure.step('Открыть saby')
    def open_base_saby(self):
        self.driver.get(BASE_SABY)
        self.wait_invisibility_preload()

    @allure.step('Кликнуть на Меню "Контакты" в хедере')
    def click_button_header_contacts(self):
        self.find_clickable_element(BUTTON_HEADER_CONTACTS).click()

    @allure.step('Кликнуть ссылку на "все Контакты"')
    def click_link_all_contacts(self):
        self.find_clickable_element(LINK_ALL_CONTACTS).click()
        self.wait_invisibility_preload()

    @allure.step('Кликнуть баннер "клиент tensor"')
    def click_client_tensor(self):
        self.find_clickable_element(BANNER_CLIENT_TENSOR).click()


    @allure.step('Открыть все контакты saby')
    def open_all_contacts(self):
        self.open_base_saby()
        self.click_button_header_contacts()
        self.click_link_all_contacts()
        self.wait_invisibility_preload()

    @allure.step('Получить текущий регион')
    def get_region_name(self):
        return self.find_clickable_element(TEXT_REGION_CONTACT).text

    @allure.step('Открыть Выберите свой регион')
    def click_region_name(self):
        self.find_clickable_element(TEXT_REGION_CONTACT).click()
        time.sleep(1)

    @allure.step('Выбрать Камчатский край')
    def click_and_check_region(self, select_region):
        self.find_clickable_element(select_region["SELECTOR"]).click()
        return WebDriverWait(self.driver, 200).until(expected_conditions.text_to_be_present_in_element(TEXT_REGION_CONTACT, select_region["TITLE"]))

    @allure.step('Ищем все контакты')
    def find_all_contacts_items(self):
        return self.find_all_elements(CONTACT_ITEM)