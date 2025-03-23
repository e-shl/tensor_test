from selenium.webdriver.common.by import By

# Подробнее о "Сила в людях"
ABOUT_BLOCK_STRONG_PEOPLE = (By.XPATH, '//*[contains(@class,"tensor_ru-Index__block4-content") and contains(.,"Сила в людях")]//a[text()="Подробнее"]')
# Изображения блоков раздела "Работаем"
IMAGES_WORKS = (By.XPATH, '//*[@class="tensor_ru-About__block3-image-wrapper"]/img')