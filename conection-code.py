def GetLanguage(text):
    try:
        # Construye el cuerpo de la solicitud JSON
        jsonBody = {
            "documents":[
                {"id": 1, "text": text}
            ]
        }

        # Muestra el JSON que se enviará a la API
        print(json.dumps(jsonBody, indent=2))

        # Construcción de la solicitud HTTP
        uri = ai_endpoint.rstrip('/').replace('https://', '')
        conn = http.client.HTTPSConnection(uri)

        # Encabezados de la solicitud con la clave de autenticación
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': ai_key
        }

        # Envía la solicitud a la API de Azure
        conn.request("POST", "/text/analytics/v3.1/languages?", str(jsonBody).encode('utf-8'), headers)

        # Recibe la respuesta de la API
        response = conn.getresponse()
        data = response.read().decode("UTF-8")

        # Si la respuesta es exitosa
        if response.status == 200:
            results = json.loads(data)
            print(json.dumps(results, indent=2))

            # Extrae y muestra el idioma detectado
            for document in results["documents"]:
                print("\nLanguage:", document["detectedLanguage"]["name"])
        else:
            # Si hay un error, muestra la respuesta completa
            print(data)

        conn.close()
    except Exception as ex:
        print(ex)
