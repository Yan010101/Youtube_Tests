import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_comentarios_en_video_youtube():
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

        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input"))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input"))
        )
        password_input.send_keys("bartolomeo89@")
        password_input.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(EC.url_contains("https://www.youtube.com/"))

        # Abrir el video en YouTube
        video_url = "https://www.youtube.com/watch?v=leIK1aUOF-Q&list=WL&index=1"
        driver.get(video_url)

        # Esperar a que se cargue completamente la página
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "comments")))
        
        # Captura de pantalla después de enviar el comentario
        screenshot_path = os.path.join(os.getcwd(), "success_video_charged.png")
        driver.save_screenshot(screenshot_path)

        # Encontrar la caja de comentarios
        comentarios_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#contenteditable-root[contenteditable='true']"))
        )

        # Hacer scroll hasta la caja de comentarios
        driver.execute_script("arguments[0].scrollIntoView();", comentarios_section)
        driver.execute_script("window.scrollBy(0, -150);")  # Ajusta el desplazamiento para mejorar la visibilidad

        # Enfocar la caja de comentarios
        comentarios_section.click()

        # Ingresar un comentario
        comentarios_section.send_keys("¡Este es un comentario de prueba!")

        # Enviar el comentario
        comentarios_section.send_keys(Keys.RETURN)

        # Captura de pantalla después de enviar el comentario
        screenshot_path = os.path.join(os.getcwd(), "success_comment.png")
        driver.save_screenshot(screenshot_path)

        # Esperar unos segundos para que el comentario se realice
        time.sleep(5)

    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main(["-v", "test_comment.py"])









