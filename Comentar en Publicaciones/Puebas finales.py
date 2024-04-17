from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Inicialización del navegador
driver = webdriver.Chrome()

# Crear directorio para guardar capturas de pantalla
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Función para comentar en una publicación en RedSocialPet
def comment_on_post(comment_text):
    try:
        driver.get("http://localhost:5173/")
        driver.implicitly_wait(10)
        driver.save_screenshot("screenshots/comment_on_post_step1.png")
        
        # Seleccionar una publicación para comentar
        comment_field = driver.find_element(By.NAME, "comment")
        comment_field.send_keys(comment_text)
        comment_field.submit()
        
        driver.save_screenshot("screenshots/comment_on_post_step2.png")
        return f"Se ha dejado el comentario '{comment_text}' en la publicación."
    except Exception as e:
        return f"Error al intentar dejar un comentario en la publicación: {e}"

# Función para eliminar un comentario en RedSocialPet
def delete_comment():
    try:
        # Seleccionar el comentario para eliminarlo
        delete_button = driver.find_element(By.XPATH, "//button[@aria-label='Delete Comment']")
        delete_button.click()
        
        driver.save_screenshot("screenshots/delete_comment.png")
        return "El comentario ha sido eliminado correctamente."
    except Exception as e:
        return f"Error al intentar eliminar el comentario: {e}"

# Ejecutar las funciones y almacenar los resultados
results = {}
results[21] = comment_on_post("¡Hermosa mascota!")
results[22] = delete_comment()

# Capturar una captura de pantalla del resultado obtenido
driver.save_screenshot("screenshots/final_result.png")

# Cerrar el navegador
driver.quit()
