from selenium.webdriver.common.by import By

# Меню "Контакты" в хедере
BUTTON_HEADER_CONTACTS = (By.XPATH, '//*[contains(@class,"sbisru-Header-ContactsMenu")]')
# Ссылка на "все Контакты"
LINK_ALL_CONTACTS = (By.XPATH, '//a[@href="/contacts"]')
# Баннер клиента Тензор
BANNER_CLIENT_TENSOR = (By.XPATH, '//*[@id="contacts_clients"]//*[contains(@class,"sbisru-Contacts__logo-tensor")]')
# Регион Контактов
TEXT_REGION_CONTACT = (By.XPATH, '//*[contains(@class,"sbisru-Contacts__underline")]//*[contains(@class,"sbis_ru-Region-Chooser__text ")]')
# Партнёр в списке Контактов
CONTACT_ITEM = (By.XPATH, '//*[contains(@class,"sbisru-Contacts-List__item")]')
# Камчатский край в меню Выберите свой регион
SELECT_KAMCHATSKIJ_KRAJ = (By.XPATH, '//*[contains(@class,"sbis_ru-Region-Panel__item")]//*[contains(text(),"Камчатский край")]')
# Республика Башкортостан в меню Выберите свой регион
SELECT_RESPUBLIKA_BASHKORTOSTAN = (By.XPATH, '//*[contains(@class,"sbis_ru-Region-Panel__item")]//*[contains(text(),"Республика Башкортостан")]')
# Республика Башкортостан в меню Выберите свой регион
SELECT_HANTY_MANSIJSKIJ_AO = (By.XPATH, '//*[contains(@class,"sbis_ru-Region-Panel__item")]//*[contains(text(),"Ханты-Мансийский АО")]')