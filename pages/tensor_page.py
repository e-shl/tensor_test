import allure

from locators.tensor_page_locators import *
from pages.base_page import BasePage
from pages.saby_page import SabyPage


class TensorPage(BasePage):

    @allure.step('Проверить, что есть блок "Сила в людях"')
    def check_adout_strong_people(self):
        return self.find_clickable_element(ABOUT_BLOCK_STRONG_PEOPLE)

    @allure.step('Клик на "Подробнее" в блоке "Сила в людях"')
    def click_adout_strong_people(self):
        self.find_clickable_element(ABOUT_BLOCK_STRONG_PEOPLE).click()
        self.wait_invisibility_preload()

    @allure.step('Ищем все изображения раздела "Работаем"')
    def find_all_works_images(self):
        return self.find_all_elements(IMAGES_WORKS)

    @allure.step('Открыть страницу tensor из saby')
    def open_tensor_from_saby(self):
        saby_page = SabyPage(self.driver)
        saby_page.open_all_contacts()
        saby_page.click_client_tensor()
        self.switch_to_new_tab()
        self.wait_invisibility_preload()