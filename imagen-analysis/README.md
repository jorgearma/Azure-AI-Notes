# README - Análisis de Imágenes con Azure AI Vision

## Descripción General
Este script utiliza el servicio de **Azure AI Vision** para analizar una imagen e identificar:
- **Descripción general** de la imagen (caption)
- **Etiquetas** relacionadas con los objetos presentes
- **Objetos detectados** y sus coordenadas
- **Personas detectadas** en la imagen
- **Descripciones densas** (detalles adicionales sobre partes de la imagen)

El script carga las credenciales desde un archivo `.env`, obtiene una imagen local y la analiza usando la API de Azure. Finalmente, genera imágenes con anotaciones sobre los objetos y personas detectadas.

---
## Flujo del Código
1. **Carga de variables de entorno:**
   - Se usa `dotenv` para cargar la clave y el endpoint de Azure desde un archivo `.env`.
   
2. **Carga de la imagen:**
   - Por defecto usa `images/street.jpg`, pero se puede pasar otra imagen como argumento.
   
3. **Autenticación con Azure AI Vision:**
   - Se inicializa un cliente con `ImageAnalysisClient`.
   
4. **Análisis de la imagen:**
   - Se usa `cv_client.analyze()` con las siguientes características:
     - `VisualFeatures.CAPTION` → Descripción de la imagen.
     - `VisualFeatures.DENSE_CAPTIONS` → Descripciones detalladas.
     - `VisualFeatures.TAGS` → Etiquetas relevantes.
     - `VisualFeatures.OBJECTS` → Objetos detectados.
     - `VisualFeatures.PEOPLE` → Personas detectadas.
   
5. **Procesamiento de resultados:**
   - Se imprimen los captions, tags y objetos detectados.
   - Se generan imágenes anotadas con bounding boxes alrededor de objetos y personas.
   
6. **Salida del programa:**
   - Se guardan imágenes con anotaciones (`objects.jpg`, `people.jpg`).

---
## Conceptos Clave
### `dotenv` y Variables de Entorno
Usamos `dotenv` para no exponer las claves en el código:
```python
load_dotenv()
ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
ai_key = os.getenv('AI_SERVICE_KEY')
```

### Cliente de Azure AI Vision
Se crea una instancia de `ImageAnalysisClient` con las credenciales de Azure:
```python
cv_client = ImageAnalysisClient(
    endpoint=ai_endpoint,
    credential=AzureKeyCredential(ai_key)
)
```

### Análisis de Imagen
El método `analyze()` devuelve un objeto con los resultados del análisis.
```python
result = cv_client.analyze(
    image_data=image_data,
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.OBJECTS, ...]
)
```

### Detección y Dibujado de Bounding Boxes
Usamos **PIL** para dibujar rectángulos en la imagen:
```python
r = detected_object.bounding_box
bounding_box = ((r.x, r.y), (r.x + r.width, r.y + r.height))
draw.rectangle(bounding_box, outline='cyan', width=3)
```

---
## ¿Cómo Ejecutarlo?
1. Instalar dependencias:
   ```sh
   pip install python-dotenv azure-ai-vision-imageanalysis pillow matplotlib
   ```

2. Crear un archivo `.env` con:
   ```sh
   AI_SERVICE_ENDPOINT=<tu_endpoint>
   AI_SERVICE_KEY=<tu_clave>
   ```

3. Ejecutar el script con:
   ```sh
   python script.py [opcional: ruta/a/imagen.jpg]
   ```

---
## Posibles Mejoras
- Manejo de errores más robusto.
- Permitir URLs en lugar de solo imágenes locales.
- Mostrar imágenes anotadas en una ventana en lugar de solo guardarlas.

Este README está pensado para entender mejor el código y repasar los conceptos clave mientras lo estudias.

