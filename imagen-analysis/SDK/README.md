# Azure AI Vision - Análisis de Imágenes

Este repositorio contiene un ejemplo y explicacion del SDK en python de azure IA para analisis de imagen

## 📌 Importaciones

```python
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
```

### 📜 Descripción

Se importan las siguientes clases:

- **ImageAnalysisClient**: Cliente para interactuar con el servicio de análisis de imágenes de Azure.
- **VisualFeatures**: Enumeración que permite seleccionar qué características de la imagen analizar (descripción, OCR, etiquetas, etc.).
- **AzureKeyCredential**: Se usa para autenticar la API de Azure con una clave de acceso.

---

## 🔑 Inicialización del Cliente

```python
import os

client = ImageAnalysisClient(
    endpoint=os.environ["ENDPOINT"],
    credential=AzureKeyCredential(os.environ["KEY"])
)
```

### ℹ️ Explicación

- Se crea una instancia del cliente **ImageAnalysisClient**.
- Se obtienen las credenciales desde las variables de entorno (`ENDPOINT` y `KEY`).
- Se utiliza **AzureKeyCredential** para la autenticación.

---

## 🖼️ Análisis de la Imagen

```python
result = client.analyze(
    image_url="<url>",
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
    gender_neutral_caption=True,
    language="en",
)
```
# Enumeración VisualFeatures

Las características visuales disponibles se incluyen en la enumeración **VisualFeatures**:

- **VisualFeatures.TAGS**: Identifica etiquetas sobre la imagen, incluidos objetos, paisajes, configuración y acciones.
- **VisualFeatures.OBJECTS**: Devuelve el cuadro delimitador para cada objeto detectado.
- **VisualFeatures.CAPTION**: Genera un título de la imagen en lenguaje natural.
- **VisualFeatures.DENSE_CAPTIONS**: Genera subtítulos más detallados para los objetos detectados.
- **VisualFeatures.PEOPLE**: Devuelve el *Bounding Box* para las personas detectadas.
- **VisualFeatures.SMART_CROPS**: Devuelve el cuadro delimitador de la relación de aspecto especificada para el área de interés.
- **VisualFeatures.READ**: Extrae texto legible.


### 📜 Explicación de los parámetros

- `image_url="<url>"`: URL de la imagen a analizar.
- `visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ]`:
  - **CAPTION**: Genera una descripción en lenguaje natural sobre la imagen.
  - **READ**: Extrae el texto presente en la imagen (OCR).
- `gender_neutral_caption=True`: Evita sesgos de género en las descripciones generadas.
- `language="en"`: Especifica que el idioma de salida sea inglés.

---



### 📌 Requisitos
- Tener una cuenta en **Azure** con el servicio **AI Vision** habilitado.
- Configurar correctamente las variables de entorno **ENDPOINT** y **KEY**.
- Instalar los paquetes necesarios ejecutando:

```sh
pip install azure-ai-vision azure-core
```

### 📜 Documentación oficial
Para más información, consulta la [documentación de Azure AI Vision](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/).

---



