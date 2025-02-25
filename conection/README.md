# Azure AI Text Analytics - Detección de Idioma

Este repositorio contiene scripts para la detección de idioma utilizando Azure AI Text Analytics. Se incluyen dos métodos de conexión:
1. **Conexión normal mediante solicitudes HTTP**
2. **Conexión utilizando el SDK de Azure**

## Requisitos previos
Antes de ejecutar los scripts, asegúrate de tener:
- Una cuenta en Azure con acceso al servicio de **Text Analytics**.
- La clave de suscripción y el endpoint del servicio.
- Un archivo `.env` en el directorio del proyecto con las siguientes variables:
  ```plaintext
  AI_SERVICE_ENDPOINT=<TU_ENDPOINT_AZURE>
  AI_SERVICE_KEY=<TU_CLAVE_DE_SUSCRIPCIÓN>
  ```
- Python 3.x instalado en tu sistema.
- Las librerías necesarias instaladas:
  ```sh
  pip install python-dotenv azure-ai-textanalytics
  ```

---

## Conexión Normal (HTTP Requests)

Este método envía solicitudes HTTP directamente a la API de Azure.

### **Archivo:** `conexión_http.py`

**Pasos principales:**
1. Carga las credenciales desde el archivo `.env`.
2. Construye la solicitud HTTP con los encabezados de autenticación.
3. Envía la solicitud a la API de Azure y procesa la respuesta.

### **Ejemplo de Uso:**
Ejecutar el script y escribir texto hasta ingresar "quit":
```sh
python conexión_http.py
```

---

## Conexión con el SDK de Azure

Este método utiliza la biblioteca oficial de Azure para una integración más sencilla y eficiente.

### **Archivo:** `conexión_sdk.py`

**Pasos principales:**
1. Carga las credenciales desde el archivo `.env`.
2. Usa `AzureKeyCredential` para la autenticación.
3. Crea un cliente de `TextAnalyticsClient`.
4. Llama a la función `detect_language()` para analizar el texto.

### **Ejemplo de Uso:**
Ejecutar el script e ingresar texto hasta escribir "quit":
```sh
python conexión_sdk.py
```

---

## Diferencias entre ambos métodos
| Característica         | HTTP Request                          | SDK de Azure                            |
|----------------------|---------------------------------|----------------------------------|
| Facilidad de uso   | Más complejo, requiere manejar manualmente la autenticación y las solicitudes HTTP. | Más sencillo, abstrae la gestión de solicitudes y autenticación. |
| Mantenimiento     | Requiere más código y gestión de errores manual. | Más robusto y con mejor manejo de errores. |
| Rendimiento       | Similar en pequeñas solicitudes, pero menos optimizado. | Mejor rendimiento para múltiples solicitudes simultáneas. |
| Flexibilidad       | Se puede usar con cualquier cliente HTTP. | Depende del SDK de Azure. |

---

## Notas finales
- Si solo necesitas probar el servicio rápidamente, el SDK de Azure es la mejor opción.
- Si deseas más control sobre las solicitudes y respuestas, usa la conexión HTTP manual.
- Revisa la [documentación oficial](https://learn.microsoft.com/en-us/azure/cognitive-services/text-analytics/) para más detalles sobre Text Analytics.



