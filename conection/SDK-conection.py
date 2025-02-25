# Importación de las librerías necesarias
from dotenv import load_dotenv  # Para cargar las variables de entorno desde un archivo .env
import os  # Para acceder a las variables de entorno del sistema
from azure.core.credentials import AzureKeyCredential  # Para la autenticación con Azure
from azure.ai.textanalytics import TextAnalyticsClient  # Cliente de la API de Azure Text Analytics

# Función principal
def main():
    global ai_endpoint  # Definir la variable global para el endpoint
    global ai_key  # Definir la variable global para la clave API
    try:
        
        load_dotenv()  
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')  # 
        ai_key = os.getenv('AI_SERVICE_KEY')  

        # Solicitar la entrada del usuario (hasta que escriba "quit")
        userText = ''
        while userText.lower() != 'quit':  #
            userText = input('\nEnter some text ("quit" to stop)\n')  #
            if userText.lower() != 'quit':  
                language = GetLanguage(userText)  
                print('Language:', language)  

    except Exception as ex:  # Capturar cualquier excepción
        print(ex)  

# Función para detectar el idioma
def GetLanguage(text):
    # Crear el cliente de Azure Text Analytics usando el endpoint y la clave API
    credential = AzureKeyCredential(ai_key)  # Crear las credenciales de autenticación
    client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)  # Crear el cliente de la API de Azure Text Analytics
    
    # Llamar al servicio para detectar el idioma del texto proporcionado
    detectedLanguage = client.detect_language(documents=[text])[0]  

    # Retornar el nombre del idioma detectado
    return detectedLanguage.primary_language.name  # Extraer y devolver el nombre del idioma detectado

# Ejecutar la función principal
if __name__ == "__main__":
    main()
