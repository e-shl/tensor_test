import allure
import pytest

from pages.saby_page import SabyPage
from tests_data import *


class TestSabyContactsPage:

    @allure.title('Проверить, что определился регион Республика Башкортостан и есть список партнеров')
    def test_auto_region_is_bashkortostan_have_contacts_items(self, driver):
        saby_page = SabyPage(driver)
        saby_page.open_all_contacts()
        assert saby_page.get_region_name() == RESPUBLIKA_BASHKORTOSTAN["TITLE"] and len(saby_page.find_all_contacts_items()) > 0

    @pytest.mark.parametrize('select_region', [KAMCHATSKIJ_KRAJ, HANTY_MANSIJSKIJ_AO])
    @allure.title('Проверить, что при смене региона изменяется список контактов и первый город региона')
    def test_change_region_changed_contacts_and_city(self, driver, select_region):
        saby_page = SabyPage(driver)
        saby_page.open_all_contacts()
        bashkortostan_contacts = saby_page.find_all_contacts_items()
        saby_page.click_change_region()
        saby_page.click_and_check_region(select_region)
        assert saby_page.find_all_contacts_items() != bashkortostan_contacts and saby_page.get_first_city_region() == select_region["FIRST_CITY"]

    @pytest.mark.parametrize('select_region', [KAMCHATSKIJ_KRAJ, HANTY_MANSIJSKIJ_AO])
    @allure.title('Проверить, что при смене регионов в URL указан новый регион')
    def test_change_region_changed_url(self, driver, select_region):
        saby_page = SabyPage(driver)
        saby_page.open_all_contacts()
        saby_page.click_change_region()
        saby_page.click_and_check_region(select_region)
        assert select_region["URL_CODE"] in saby_page.get_current_url()

    @pytest.mark.parametrize('select_region', [KAMCHATSKIJ_KRAJ, HANTY_MANSIJSKIJ_AO])
    @allure.title('Проверить, что при смене регионов в TITLE указан новый регион')
    def test_change_region_changed_title_page(self, driver, select_region):
        saby_page = SabyPage(driver)
        saby_page.open_all_contacts()
        saby_page.click_change_region()
        saby_page.click_and_check_region(select_region)
        assert select_region["TITLE"] in saby_page.get_current_title_page()
