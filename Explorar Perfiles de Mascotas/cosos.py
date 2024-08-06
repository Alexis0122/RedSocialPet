from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Inicialización del navegador
driver = webdriver.Chrome()

# Crear directorio para guardar capturas de pantalla
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Función para explorar perfiles de mascotas sugeridos en RedSocialPet
def explore_pet_profiles():
    try:
        driver.get("http://localhost:5173/")
        driver.implicitly_wait(10)
        driver.save_screenshot("screenshots/explore_profiles_step1.png")
        
        # Seleccionar un perfil de mascota sugerido
        suggested_profile = driver.find_element(By.XPATH, "//div[@class='suggested-profile']/a")
        suggested_profile.click()
        
        driver.save_screenshot("screenshots/explore_profiles_step2.png")
        return "Exploración de perfiles de mascotas sugeridos exitosa."
    except Exception as e:
        return f"Error durante la exploración de perfiles de mascotas sugeridos: {e}"

# Función para seguir fácilmente los perfiles de mascotas que interesen
def follow_explored_profile():
    try:
        # Seguir al perfil de mascota explorado
        follow_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Follow')]")
        follow_button.click()
        
        driver.save_screenshot("screenshots/follow_explored_profile.png")
        return "Perfil de mascota seguido correctamente."
    except Exception as e:
        return f"Error al intentar seguir el perfil de mascota explorado: {e}"

# Función para verificar la información detallada y las fotos de las mascotas exploradas
def check_explored_profile_details():
    try:
        # Comprobar la información detallada y las fotos del perfil de mascota explorado
        driver.find_element(By.CLASS_NAME, "pet-details")
        driver.save_screenshot("screenshots/explored_profile_details.png")
        return "Información detallada y fotos del perfil de mascota explorado verificadas."
    except Exception as e:
        return f"No se encontró la información detallada del perfil de mascota explorado: {e}"

# Ejecutar las funciones y almacenar los resultados
results = {}
results[15] = explore_pet_profiles()
results[16] = follow_explored_profile()
results[17] = check_explored_profile_details()

# Capturar una captura de pantalla del resultado obtenido
driver.save_screenshot("screenshots/final_result.png")

# Cerrar el navegador
driver.quit()