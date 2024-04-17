from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Inicialización del navegador
driver = webdriver.Chrome()

# Crear directorio para guardar capturas de pantalla
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Función para realizar el registro de usuario en RedSocialPet
def register_user(email, username, full_name, password):
    try:
        driver.get("http://localhost:5173/")
        driver.implicitly_wait(10)
        
        # Abrir el formulario de registro
        registration_button = driver.find_element(By.CLASS_NAME, "css-8mezga")
        time.sleep(3)
        driver.save_screenshot("Registro de Usuario/screenshots/registration_step1.png")
        registration_button.click()
        
        # Completar el formulario de registro
        email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        email_field.send_keys(email)
        username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username_field.send_keys(username)
        full_name_field = driver.find_element(By.XPATH, "//input[@placeholder='Full Name']")
        full_name_field.send_keys(full_name)
        password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_field.send_keys(password)
        
        time.sleep(3)
        driver.save_screenshot("Registro de Usuario/screenshots/registration_step2.png")
        # Enviar el formulario
        password_field.submit()
        
        time.sleep(3)
        # Cerrar sesión
        logout_button = driver.find_element(By.XPATH, "//button[contains(text(),'Logout')]")
        logout_button.click()
        
        return "Registro de usuario exitoso."
    except Exception as e:
        return f"Error durante el registro de usuario: {e}"

# Función para realizar el inicio de sesión en RedSocialPet
def login_user(email, password):
    try:
        driver.get("http://localhost:5173/")
        driver.implicitly_wait(10)
        time.sleep(5)
        driver.save_screenshot("Registro de Usuario/screenshots/login_step1.png")
        
        # Completar el formulario de inicio de sesión
        email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        email_field.send_keys(email)
        password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_field.send_keys(password)
        password_field.submit()
        
        driver.save_screenshot("Registro de Usuario/screenshots/login_step2.png")
        return "Inicio de sesión exitoso."
    except Exception as e:
        return f"Error durante el inicio de sesión: {e}"

# Ejecutar las funciones y almacenar los resultados
results = {}
results[1] = register_user("test1@example.com", "test1_user", "Test1 User", "password123")
results[2] = login_user("test1@example.com", "password123")

# Capturar una captura de pantalla del resultado obtenido
driver.save_screenshot("Registro de Usuario/screenshots/final_result.png")


# Crear el contenido del informe HTML con la plantilla específica
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Caso de Prueba - [Nombre del Caso de Prueba]</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Caso de Prueba - Verificación de Registro </h1>
        <h2>Descripción:</h2>
        <p>Este caso de prueba verifica que un usuario nuevo pueda completar el proceso de registro en la plataforma RedSocialPet. El proceso incluye ingresar datos como nombre de usuario, correo electrónico, contraseña, y aceptar los términos y condiciones.</p>
        
        <h2>Resultado Real:</h2>
        <p>{results[2]}</p>
        
        <h2>Resultado Esperado:</h2>
        <p>El usuario debe poder registrarse proporcionando todos los datos requeridos y recibir un correo electrónico de confirmación que valide que el proceso se ha completado correctamente.</p>
        
        <h2>Prioridad:</h2>
        <p>[Alta]</p>
        
        <h2>ID de Prueba:</h2>
        <p>[RSPT1001]</p>
        
        <h2>Criterios de Aceptación:</h2>
        <ul>
            <li>[El formulario de registro debe aceptar el nombre de usuario, correo electrónico y contraseña.]</li>
            <li>[Todos los campos deben ser validados para evitar entradas inválidas.]</li>
        </ul>
        
        <h2>Criterios de Rechazo:</h2>
        <ul>
            <li>El usuario no puede registrarse con un correo electrónico que ya está en uso.</li>
            <li>El registro falla si no se aceptan los términos y condiciones.</li>
        </ul>
        
        <h2>Fecha:</h2>
        <p>[fecha 17/4/24]</p>
        
        <h2>Herramienta:</h2>
        <p>Selenium</p>
    </div>
</body>
</html>
"""

# Guardar el informe en un archivo HTML
with open("informe_ejecucion.html", "w") as file:
    file.write(html_content)

# Cerrar el navegador
driver.quit()

print("Informe de ejecución generado con éxito.")