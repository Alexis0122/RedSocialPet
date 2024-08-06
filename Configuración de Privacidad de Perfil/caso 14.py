from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Inicialización del navegador
driver = webdriver.Chrome()

# Crear directorio para guardar capturas de pantalla
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Función para configurar la privacidad del perfil en RedSocialPet
def configure_privacy_settings():
    try:
        driver.get("http://localhost:5173/settings")
        driver.implicitly_wait(10)
        driver.save_screenshot("screenshots/privacy_settings_step1.png")
        
        # Seleccionar la opción de configuración de privacidad
        privacy_option = driver.find_element(By.XPATH, "//button[contains(text(), 'Privacy Settings')]")
        privacy_option.click()
        
        # Configurar las preferencias de privacidad
        # Aquí puedes simular la interacción con los controles de privacidad, por ejemplo, cambiar quién puede ver tu perfil, publicaciones, etc.
        # Puedes modificar esta parte del código de acuerdo a tus necesidades específicas
        
        driver.save_screenshot("screenshots/privacy_settings_step2.png")
        return "Configuración de privacidad aplicada correctamente."
    except Exception as e:
        return f"Error durante la configuración de privacidad: {e}"

# Ejecutar la función y almacenar el resultado
results = {}
results[14] = configure_privacy_settings()

# Capturar una captura de pantalla del resultado obtenido
driver.save_screenshot("screenshots/final_result.png")

# Cerrar el navegador
driver.quit()
