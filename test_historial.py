import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_historial_en_youtube():
    try:
        # Configuración del navegador
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

        # Iniciar sesión en YouTube
        login_url = "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Des-419%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&ec=65620&flowEntry=ServiceLogin&flowName=GlifWebSignIn&hl=es-419&ifkv=AXo7B7Xqe8g5PJlziWVpBsNVpPAPwJ16DOmbT92rE1kbWicY3Zy7WoNKS7vw-Gzi--0LtycXuIbc&passive=true&service=youtube&uilel=3&dsh=S1309189610%3A1691713244040797"
        driver.get(login_url)

        username = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        username.send_keys("dobav83634@viperace.com")
        username.send_keys(Keys.RETURN)

        password_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input"))
        )
        password_input = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input"))
        )
        password_input.send_keys("bartolomeo89@")
        password_input.send_keys(Keys.RETURN)

        WebDriverWait(driver, 15).until(EC.url_contains("https://www.youtube.com/"))

        ver_mas_tarde_url = "https://www.youtube.com/feed/history"
        driver.get(ver_mas_tarde_url)

        # Captura de pantalla del historial
        screenshot_path = os.path.join(os.getcwd(), "success_watched.png")
        driver.save_screenshot(screenshot_path)

    finally:
        pass

if __name__ == "__main__":
    pytest.main()



