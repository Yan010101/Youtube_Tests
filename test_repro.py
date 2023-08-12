import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.fixture
def driver():
    # Inicializar el driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def take_screenshot(driver, filename):
    driver.save_screenshot(filename)

def test_busqueda_y_reproduccion(driver):
    try:
        driver.get("https://www.youtube.com")

        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys("recommended video")  # Corregido el typo en la búsqueda
        search_box.send_keys(Keys.RETURN)

        # Esperar a que aparezcan los resultados de búsqueda
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.ID, "contents")))

        # Tomar screenshot en caso de éxito
        take_screenshot(driver, "success_videos.png")

        # Buscar y hacer clic en el primer enlace de video
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#contents a#thumbnail")))
            video_link = driver.find_element(By.CSS_SELECTOR, "#contents a#thumbnail")
            driver.execute_script("arguments[0].scrollIntoView();", video_link)
            video_link.click()

            # Esperar a que el reproductor de video sea interactable
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ytp-play-button")))

            # Reproducir el video
            video_player = driver.find_element(By.CSS_SELECTOR, ".ytp-play-button")
            video_player.click()
            time.sleep(5)  # Reproducir el video durante 5 segundos

            # Tomar screenshot en caso de éxito
            take_screenshot(driver, "success_reproduction.png")

        except TimeoutException:
            take_screenshot(driver, "error_screenshot.png")
            pytest.fail("Error: No se pudo encontrar o interactuar con el enlace del video")

    except Exception as e:
        take_screenshot(driver, "error_screenshot.png")
        pytest.fail(f"Error: {str(e)}")





    

