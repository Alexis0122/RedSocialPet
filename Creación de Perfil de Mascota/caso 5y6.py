from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Inicialización del navegador
driver = webdriver.Chrome()

# Crear directorio para guardar capturas de pantalla
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Función para crear un perfil de mascota en RedSocialPet
def create_pet_profile(name, species, age):
    try:
        driver.get("http://localhost:5173/")
        driver.implicitly_wait(10)
        driver.save_screenshot("Creación de Perfil de Mascota/screenshots/create_profile_step1.png")
        
        # Navegar a la página de creación de perfil de mascota
        create_profile_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Profile')]")
        create_profile_button.click()
        
        # Completar el formulario de creación de perfil
        name_field = driver.find_element(By.NAME, "name")
        name_field.send_keys(name)
        species_field = driver.find_element(By.NAME, "species")
        species_field.send_keys(species)
        age_field = driver.find_element(By.NAME, "age")
        age_field.send_keys(age)
        
        # Enviar el formulario
        age_field.submit()
        
        driver.save_screenshot("Creación de Perfil de Mascota/screenshots/create_profile_step2.png")
        return "Perfil de mascota creado exitosamente."
    except Exception as e:
        return f"Error durante la creación del perfil de mascota: {e}"

# Función para cargar una foto de la mascota en el perfil
def upload_pet_photo(file_path):
    try:
        # Simular el proceso de carga de la foto de la mascota
        upload_button = driver.find_element(By.XPATH, "//input[@type='file']")
        upload_button.send_keys(file_path)
        
        driver.save_screenshot("Creación de Perfil de Mascota/screenshots/upload_photo.png")
        return "Foto de la mascota cargada exitosamente."
    except Exception as e:
        return f"Error durante la carga de la foto de la mascota: {e}"

# Ejecutar las funciones y almacenar los resultados
results = {}
results[1] = create_pet_profile("Teddy", "Cat", "3")
results[2] = upload_pet_photo("/path/to/your/photo.jpg")  # Reemplaza con la ruta de tu foto

# Capturar una captura de pantalla del resultado obtenido
driver.save_screenshot("Creación de Perfil de Mascota/screenshots/final_result.png")

# Cerrar el navegador
driver.quit()