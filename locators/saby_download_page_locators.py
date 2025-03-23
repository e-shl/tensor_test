from selenium.webdriver.common.by import By

# В Footer'e "Скачать локальные версии"
LOCALS_VERSIONS = (By.XPATH, '//*[@href="/download"]')
# Вкладка Saby Plugin (активный и не активный overlay)
SABY_PLUGIN = (By.XPATH, '//*[@class="controls-TabButton__caption" and text()="Saby Plugin"]/ancestor::div[contains(@class,"controls-ListView__item")]')
# Вкладка ОС Windows (активный и не активный overlay)
SABY_DOWNLOAD_OS_WINDOWS = (By.XPATH, '//*[contains(@class,"ws-SwitchableArea__item") and not(contains(@class,"ws-hidden")) ]//*[contains(@class,"sbis_ru-DownloadNew-innerTabs__title") and text()="Windows"]/ancestor::div[contains(@class,"controls-ListView__item")]')
# Кнопка Скачать Веб-установщик
SABY_PLUGIN_WEB_INSTALLER = (By.XPATH, '//*[contains(@class,"sbis_ru-DownloadNew-block") and contains(.,"Веб-установщик")]//*[contains(@class,"sbis_ru-DownloadNew-loadLink__link")]')