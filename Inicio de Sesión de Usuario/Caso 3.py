from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Inicialización del navegador
driver = webdriver.Chrome()

# Crear directorio para guardar capturas de pantalla
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Función para realizar el inicio de sesión en RedSocialPet
def login_user(email, password):
    try:
        driver.get("http://localhost:5173/")
        driver.implicitly_wait(10)
        time.sleep(5)
        driver.save_screenshot("screenshots/login_step1.png")
        
        # Completar el formulario de inicio de sesión
        email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        email_field.send_keys(email)
        password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_field.send_keys(password)
        
        # Esperar un momento para que la página se actualice después de ingresar los datos
        time.sleep(2)
        
        # Hacer clic en el botón de inicio de sesión
        login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]")
        login_button.click()
        
        # Esperar a que se cargue la página de inicio de sesión
        time.sleep(5)
        
        driver.save_screenshot("screenshots/login_step2.png")
        return "Inicio de sesión exitoso."
    except Exception as e:
        return f"Error durante el inicio de sesión: {e}"
    
# Función para realizar el inicio de sesión en RedSocialPet
def Error_login_user():
    try:
        time.sleep(3)
        driver.get("http://localhost:5173/")
        driver.implicitly_wait(10)
        driver.save_screenshot("screenshots/login_step1.png")
        
        # Completar el formulario de inicio de sesión
        email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        email_field.send_keys("email")
        password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_field.send_keys("password")
        
        Login_button = driver.find_element(By.CLASS_NAME, "chakra-button css-m3i9ma")
        Login_button.click()

        time.sleep(5)
        driver.save_screenshot("screenshots/error_login_step2.png")
        return "Error de sesión exitoso."
    except Exception as e:
        return f"inicio de sesión Correctamente: {e}"


# Ejecutar la función y almacenar el resultado
results = {}
results[0] = login_user("test@example.com", "password123")

time.sleep(2)
# Cerrar el navegador
driver.quit()
