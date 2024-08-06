from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Inicialización del navegador
driver = webdriver.Chrome()

# Crear directorio para guardar capturas de pantalla
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Función para buscar perfiles de mascotas y usuarios en RedSocialPet
def search_profiles(query):
    try:
        driver.get("http://localhost:5173/")
        driver.implicitly_wait(10)
        driver.save_screenshot("screenshots/search_step1.png")
        
        # Ingresar la consulta de búsqueda en el campo de búsqueda
        search_field = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_field.send_keys(query)
        
        # Enviar la consulta de búsqueda
        search_field.submit()
        
        driver.save_screenshot("screenshots/search_step2.png")
        return f"Búsqueda de '{query}' realizada exitosamente."
    except Exception as e:
        return f"Error durante la búsqueda de '{query}': {e}"

# Ejecutar la función y almacenar el resultado
results = {}
results[13] = search_profiles("nombre123")

# Capturar una captura de pantalla del resultado obtenido
driver.save_screenshot("screenshots/final_result.png")

# Cerrar el navegador
driver.quit()