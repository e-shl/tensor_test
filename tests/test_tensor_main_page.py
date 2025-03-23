import allure

from pages.tensor_page import TensorPage
from urls import *

class TestTensorMainPage:

    @allure.title('Проверить, что есть блок "Сила в людях"')
    def test_strong_people_on_tensor_page(self, driver):
        tensor_page = TensorPage(driver)
        tensor_page.open_tensor_from_saby()
        assert tensor_page.check_adout_strong_people()

    @allure.title('Проверить, что открылась страницы ' + TENSOR_ABOUT_URL)
    def test_click_strong_people_is_opened_about_url(self, driver):
        tensor_page = TensorPage(driver)
        tensor_page.open_tensor_from_saby()
        tensor_page.click_adout_strong_people()
        assert tensor_page.get_current_url() == TENSOR_ABOUT_URL

    @allure.title('Проверить, что в разделе "Работаем" у фотографий одинаковые высота (height) и ширина (width)')
    def test_photos_works_is_height_and_width_similar(self, driver):
        tensor_page = TensorPage(driver)
        tensor_page.open_tensor_from_saby()
        tensor_page.click_adout_strong_people()
        images_works_sizes = set()
        for el in tensor_page.find_all_works_images():
            images_works_sizes.add(str(el.size))
        assert len(images_works_sizes) == 1