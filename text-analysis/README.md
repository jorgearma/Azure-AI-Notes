# Azure Text Analytics - Análisis de Sentimiento y Lenguaje

Este script en Python utiliza el servicio de Azure Text Analytics para analizar archivos de texto almacenados en la carpeta `reviews`. A partir de estos archivos, detecta el idioma, analiza el sentimiento, extrae frases clave, reconoce entidades y obtiene entidades vinculadas a información adicional.

## Requisitos Previos

Antes de ejecutar el script, asegúrate de cumplir con los siguientes requisitos:

1. Tener una cuenta de Azure y un servicio de Text Analytics configurado.
2. Instalar las dependencias necesarias con:
   ```sh
   pip install azure-ai-textanalytics python-dotenv
   ```
3. Configurar las variables de entorno en un archivo `.env`:
   ```sh
   AI_SERVICE_ENDPOINT=<tu_endpoint_de_azure>
   AI_SERVICE_KEY=<tu_clave_de_azure>
   ```

## Estructura del Código

### Importación de Librerías
```python
from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
```
Se importan las librerías necesarias para manejar las variables de entorno y conectar con el servicio de Azure.

### Configuración del Cliente de Azure
```python
load_dotenv()
ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
ai_key = os.getenv('AI_SERVICE_KEY')
credential = AzureKeyCredential(ai_key)
ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)
```
Se cargan las credenciales del servicio desde el archivo `.env` y se configura el cliente de `TextAnalyticsClient`.

### Análisis de Archivos en la Carpeta `reviews`
```python
reviews_folder = 'reviews'
for file_name in os.listdir(reviews_folder):
    text = open(os.path.join(reviews_folder, file_name), encoding='utf8').read()
```
El código recorre todos los archivos de la carpeta `reviews` y lee su contenido.

### Detección de Idioma
```python
detectedLanguage = ai_client.detect_language(documents=[text])[0]
print('\nLanguage: {}'.format(detectedLanguage.primary_language.name))
```
Se detecta el idioma del texto y se imprime en la consola.

### Análisis de Sentimiento
```python
sentimentAnalysis = ai_client.analyze_sentiment(documents=[text])[0]
print("\nSentiment: {}".format(sentimentAnalysis.sentiment))
```
Se obtiene el sentimiento del texto (`positive`, `neutral` o `negative`).

### Extracción de Frases Clave
```python
phrases = ai_client.extract_key_phrases(documents=[text])[0].key_phrases
if len(phrases) > 0:
    print("\nKey Phrases:")
    for phrase in phrases:
        print('\t{}'.format(phrase))
```
Se extraen frases clave relevantes del texto.

### Reconocimiento de Entidades
```python
entities = ai_client.recognize_entities(documents=[text])[0].entities
if len(entities) > 0:
    print("\nEntities")
    for entity in entities:
        print('\t{} ({})'.format(entity.text, entity.category))
```
Se identifican entidades dentro del texto y su categoría.

### Obtención de Entidades Vinculadas
```python
entities = ai_client.recognize_linked_entities(documents=[text])[0].entities
if len(entities) > 0:
    print("\nLinks")
    for linked_entity in entities:
        print('\t{} ({})'.format(linked_entity.name, linked_entity.url))
```
Se obtienen entidades con enlaces a información adicional.

## Manejo de Excepciones
```python
except Exception as ex:
    print(ex)
```
Si ocurre algún error durante la ejecución, se imprime en la consola.

## Ejecución del Script
```python
if __name__ == "__main__":
    main()
```
Permite ejecutar el script de forma independiente.



