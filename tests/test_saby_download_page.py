import os

import allure

from pages.saby_download_page import SabyDownloadPage


class TestSabyDownloadPage:

    @allure.title('Проверить, что размер скачанного файла совпадает с указанным на сайте')
    def test_download_plugin_windows_is_size_equa_web(self, driver):
        saby_download_page = SabyDownloadPage(driver)
        saby_download_page.open_base_saby()
        saby_download_page.click_local_versions()
        saby_download_page.click_tab_plugin()
        saby_download_page.click_tab_os_windows()
        saby_download_page.click_download_web_installer()
        file_patch_web_installer = saby_download_page.get_file_patch_web_installer()
        saby_download_page.wait_web_installer_downloaded(file_patch_web_installer)
        web_installer_size = saby_download_page.get_web_installer_size_from_downloads(file_patch_web_installer)
        os.remove(file_patch_web_installer)
        assert web_installer_size in saby_download_page.get_web_installer_size_from_saby()