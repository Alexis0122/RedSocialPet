from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Inicialización del navegador
driver = webdriver.Chrome()

# Crear directorio para guardar capturas de pantalla
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Función para crear una publicación sobre mascotas en RedSocialPet
def create_pet_post(text, photo_path):
    try:
        driver.get("http://localhost:5173/")
        driver.implicitly_wait(10)
        driver.save_screenshot("screenshots/create_post_step1.png")
        
        # Navegar a la página de creación de publicación
        create_post_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Post')]")
        create_post_button.click()
        
        # Completar el formulario de creación de publicación
        text_field = driver.find_element(By.NAME, "text")
        text_field.send_keys(text)
        
        # Cargar foto si se proporciona una ruta de archivo
        if photo_path:
            upload_photo_button = driver.find_element(By.XPATH, "//input[@type='file']")
            upload_photo_button.send_keys(photo_path)
        
        # Enviar la publicación
        text_field.submit()
        
        driver.save_screenshot("screenshots/create_post_step2.png")
        return "Publicación sobre mascotas creada exitosamente."
    except Exception as e:
        return f"Error durante la creación de la publicación sobre mascotas: {e}"

# Función para interactuar con la publicación: dar "me gusta" y agregar comentarios
def interact_with_post():
    try:
        # Simular dar "me gusta" a la publicación
        like_button = driver.find_element(By.XPATH, "//button[@aria-label='Like']")
        like_button.click()
        
        # Simular agregar un comentario a la publicación
        comment_field = driver.find_element(By.NAME, "comment")
        comment_field.send_keys("¡Hermosa mascota!")
        comment_field.submit()
        
        driver.save_screenshot("screenshots/interact_with_post.png")
        return "Interacción con la publicación exitosa."
    except Exception as e:
        return f"Error durante la interacción con la publicación: {e}"

# Función para verificar que la publicación sea visible en el feed de noticias
def check_post_visibility():
    try:
        # Comprobar si la publicación está presente en el feed de noticias
        driver.find_element(By.CLASS_NAME, "post")
        driver.save_screenshot("screenshots/post_visibility.png")
        return "La publicación es visible en el feed de noticias."
    except Exception as e:
        return f"La publicación no es visible en el feed de noticias: {e}"

# Ejecutar las funciones y almacenar los resultados
results = {}
results[1] = create_pet_post("¡Conoce a mi adorable gatito!", "/path/to/your/photo.jpg")  # Reemplaza con la ruta de tu foto
results[2] = check_post_visibility()
results[3] = interact_with_post()

# Capturar una captura de pantalla del resultado obtenido
driver.save_screenshot("screenshots/final_result.png")

# Cerrar el navegador
driver.quit()
