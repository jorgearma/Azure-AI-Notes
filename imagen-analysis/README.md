# Azure AI Vision - Análisis de Imágenes

Este repositorio contiene un ejemplo de código para utilizar el servicio de Azure AI Vision para analizar imágenes de manera programática.

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

> ⚠️ **Nota:** Asegúrate de configurar correctamente las variables de entorno antes de ejecutar el código.

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

### 📜 Explicación de los parámetros

- `image_url="<url>"`: URL de la imagen a analizar.
- `visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ]`:
  - **CAPTION**: Genera una descripción en lenguaje natural sobre la imagen.
  - **READ**: Extrae el texto presente en la imagen (OCR).
- `gender_neutral_caption=True`: Evita sesgos de género en las descripciones generadas.
- `language="en"`: Especifica que el idioma de salida sea inglés.

---

## 🔍 Resumen

Este código utiliza el servicio **Azure AI Vision** para analizar una imagen remota y obtener:

✅ Una descripción textual de la imagen.
✅ Extracción de texto (OCR) presente en la imagen.

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

🚀 **Ahora puedes comenzar a analizar imágenes con Azure AI Vision!**

