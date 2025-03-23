import os
import time

import allure

from locators.saby_download_page_locators import *
from pages.base_page import BasePage
from urls import *


class SabyDownloadPage(BasePage):

    @allure.step('Открыть saby')
    def open_base_saby(self):
        self.driver.get(BASE_SABY)
        self.wait_invisibility_preload()

    @allure.step('Кликнуть на ссылку Скачать локальные версии')
    def click_local_versions(self):
        self.find_clickable_element(LOCALS_VERSIONS).click()

    @allure.step('Кликнуть на вкладку Saby Plugin')
    def click_tab_plugin(self):
        self.find_clickable_element(SABY_PLUGIN).click()

    @allure.step('Кликнуть на вкладку Windows')
    def click_tab_os_windows(self):
        self.find_clickable_element(SABY_DOWNLOAD_OS_WINDOWS).click()

    @allure.step('Кликнуть Скчать Веб-установщик')
    def click_download_web_installer(self):
        self.find_clickable_element(SABY_PLUGIN_WEB_INSTALLER).click()

    @allure.step('Получить размер Веб-установщика из saby')
    def get_web_installer_size_from_saby(self):
        return self.find_clickable_element(SABY_PLUGIN_WEB_INSTALLER).text

    @allure.step('Получить путь до скаченного файла Веб-установщик')
    def get_file_patch_web_installer(self):
        return f"{os.getcwd()}/{self.find_clickable_element(SABY_PLUGIN_WEB_INSTALLER).get_attribute("href").split("/")[-1]}"

    @allure.step('Получить размер скаченного Веб-установщика')
    def get_web_installer_size_from_downloads(self, file_patch_web_installer):
        return f" {str(os.path.getsize(file_patch_web_installer) / 1024 / 1024)[:5]} МБ"

    @allure.step('Ждать появления файла Веб-установщика')
    def wait_web_installer_downloaded(self, file_patch_web_installer):
        time_to_wait = 30
        time_counter = 0
        while not os.path.exists(file_patch_web_installer):
            time.sleep(1)
            time_counter += 1
            if time_counter > time_to_wait: break