from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Inicialización del navegador
driver = webdriver.Chrome()

# Crear directorio para guardar capturas de pantalla
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Función para seguir a otros usuarios en RedSocialPet
def follow_user(username):
    try:
        driver.get("http://localhost:5173/")
        driver.implicitly_wait(10)
        driver.save_screenshot("screenshots/follow_user_step1.png")
        
        # Navegar al perfil del usuario que se va a seguir
        user_profile_link = driver.find_element(By.XPATH, f"//a[contains(text(), '{username}')]")
        user_profile_link.click()
        
        # Seguir al usuario
        follow_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Follow')]")
        follow_button.click()
        
        driver.save_screenshot("screenshots/follow_user_step2.png")
        return f"Se ha seguido al usuario {username}."
    except Exception as e:
        return f"Error al intentar seguir al usuario {username}: {e}"

# Función para verificar si las actualizaciones de los usuarios seguidos aparecen en el feed de noticias
def check_followed_users_updates():
    try:
        # Navegar al feed de noticias
        driver.get("http://localhost:5173/")
        driver.save_screenshot("screenshots/feed.png")
        
        # Comprobar si hay actualizaciones de los usuarios seguidos
        driver.find_element(By.CLASS_NAME, "post")
        return "Las actualizaciones de los usuarios seguidos aparecen en el feed de noticias."
    except Exception as e:
        return f"No hay actualizaciones de usuarios seguidos en el feed de noticias: {e}"

# Función para verificar que el sistema muestre sugerencias de usuarios para seguir
def check_user_suggestions():
    try:
        # Navegar a la página de sugerencias de usuarios
        driver.get("http://localhost:5173/suggestions")
        driver.save_screenshot("screenshots/user_suggestions.png")
        
        # Comprobar si hay sugerencias de usuarios para seguir
        driver.find_element(By.CLASS_NAME, "user-suggestion")
        return "El sistema muestra sugerencias de usuarios para seguir."
    except Exception as e:
        return f"No hay sugerencias de usuarios para seguir: {e}"

# Ejecutar las funciones y almacenar los resultados
results = {}
results[10] = follow_user("example_user")
results[11] = check_followed_users_updates()
results[12] = check_user_suggestions()

# Capturar una captura de pantalla del resultado obtenido
driver.save_screenshot("screenshots/final_result.png")

# Cerrar el navegador
driver.quit()
