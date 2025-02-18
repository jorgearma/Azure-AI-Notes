
# Análisis de Sentimiento con Azure Cognitive Services

Este tutorial describe cómo ejecutar un contenedor de Docker para realizar análisis de sentimientos utilizando el servicio de **Azure Cognitive Services** y cómo interactuar con él usando `curl`.

## 1. Ejecutar el Contenedor de Docker

El siguiente comando ejecuta el contenedor que corre el servicio de análisis de sentimientos de Azure:

```bash
sudo docker run --rm -it -p 5000:5000 --memory 8g --cpus 1 \
  mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment:latest \
  Eula=accept \
  Billing=https://juancho.cognitiveservices.azure.com/ \
  ApiKey=3wAP0tnQtS6H5ycAcKzjcBaT8tqLEeSE9RAkgq351kVPrEb8ujZNJQQJ99BBACi5YpzXJ3w3AAAEACOGdAm 


  Explicación de los parámetros:


--rm:   Elimina el contenedor una vez que se detenga.
-it:     Mantiene la interacción con la terminal.
-p  5000:5000: Expone el puerto 5000 del contenedor a la máquina local.
--memory 8g --cpus 1: Limita los recursos del contenedor.
mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment:latest: Imagen de Docker para el servicio de análisis de sentimiento.
Eula=accept: Acepta el acuerdo de licencia.
Billing: URL de tu recurso de Azure Cognitive Services.
ApiKey: Clave de API para autenticar el servicio.



curl -X POST "http://localhost:5000/text/analytics/v3.0/sentiment" \
  -H "Content-Type: application/json" \
  --data-ascii "{'documents':[{'id':1,'text':'love you '}]}"


Explicación de la solicitud:
-X POST: Realiza una solicitud HTTP POST.
-H "Content-Type: application/json": Especifica que el cuerpo de la solicitud es JSON.
--data-ascii: Envía el texto a analizar en formato JSON.




