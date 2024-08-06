from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Inicialización del navegador
driver = webdriver.Chrome()

# Crear directorio para guardar capturas de pantalla
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Función para dar "Me Gusta" a una publicación en RedSocialPet
def like_post():
    try:
        driver.get("http://localhost:5173/")
        driver.implicitly_wait(10)
        driver.save_screenshot("screenshots/like_post_step1.png")
        
        # Seleccionar una publicación para dar "Me Gusta"
        like_button = driver.find_element(By.XPATH, "//button[@aria-label='Like']")
        like_button.click()
        
        driver.save_screenshot("screenshots/like_post_step2.png")
        return "Se dio 'Me Gusta' a la publicación correctamente."
    except Exception as e:
        return f"Error al intentar dar 'Me Gusta' a la publicación: {e}"

# Función para retirar "Me Gusta" de una publicación en RedSocialPet
def unlike_post():
    try:
        # Seleccionar la publicación para retirar "Me Gusta"
        unlike_button = driver.find_element(By.XPATH, "//button[@aria-label='Unlike']")
        unlike_button.click()
        
        driver.save_screenshot("screenshots/unlike_post.png")
        return "Se retiró 'Me Gusta' de la publicación correctamente."
    except Exception as e:
        return f"Error al intentar retirar 'Me Gusta' de la publicación: {e}"

# Ejecutar las funciones y almacenar los resultados
results = {}
results[18] = like_post()
results[19] = unlike_post()

# Capturar una captura de pantalla del resultado obtenido
driver.save_screenshot("screenshots/final_result.png")

# Cerrar el navegador
driver.quit()
