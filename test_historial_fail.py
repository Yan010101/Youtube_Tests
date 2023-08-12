import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_fallo_historial_en_youtube():
    try:
        # Configuración del navegador
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

        driver.get("https://www.youtube.com")

        ver_mas_tarde_url = "https://www.youtube.com/feed/history"
        driver.get(ver_mas_tarde_url)

        # Captura de pantalla del historial
        screenshot_path = os.path.join(os.getcwd(), "fail_watched.png")
        driver.save_screenshot(screenshot_path)

    finally:
        pass

if __name__ == "__main__":
    pytest.main()