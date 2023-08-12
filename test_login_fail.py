import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Función para tomar captura de pantalla
def take_screenshot(driver, screenshot_name):
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)
    driver.save_screenshot(screenshot_path)

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_login_fallido(driver):
    
        login_url = "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Des-419%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&ec=65620&flowEntry=ServiceLogin&flowName=GlifWebSignIn&hl=es-419&ifkv=AXo7B7Xqe8g5PJlziWVpBsNVpPAPwJ16DOmbT92rE1kbWicY3Zy7WoNKS7vw-Gzi--0LtycXuIbc&passive=true&service=youtube&uilel=3&dsh=S1309189610%3A1691713244040797"
        driver.get(login_url)

        username = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        username.send_keys("dobav83634@viperace.com")
        username.send_keys(Keys.RETURN)
        
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input"))
        )
        password_input.send_keys("bartolomeo89@23")
        password_input.send_keys(Keys.RETURN)
        
        # Esperar a que aparezca un mensaje de error
        error_message = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[2]/div[2]/span')))
        
        # Tomar captura de pantalla del mensaje de error
        take_screenshot(driver, "failed_login_error.png")
        
        driver.quit()

