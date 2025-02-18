## Clases principales

### MediaType (Enum)
Define el tipo de contenido que se va a analizar: 

- `Text`: Texto.
- `Image`: Imagen.

### Category (Enum)
Define las categorías de contenido que se pueden analizar:

- `Hate`: Contenido de odio.
- `SelfHarm`: Contenido relacionado con autolesiones.
- `Sexual`: Contenido sexual.
- `Violence`: Contenido violento.

### Action (Enum)
Define las acciones que se pueden tomar después del análisis:

- `Accept`: Aceptar el contenido.
- `Reject`: Rechazar el contenido.

### DetectionError (Excepción)
Maneja errores que pueden ocurrir durante la detección de contenido.

### Decision (Clase)
Representa la decisión tomada después de analizar el contenido. Contiene:

- `suggested_action`: La acción sugerida (Aceptar o Rechazar).
- `action_by_category`: Un diccionario que indica la acción para cada categoría.

### ContentSafety (Clase principal)
Esta clase contiene la lógica para interactuar con el Azure Content Safety API. Incluye métodos para:

1. **Construir la URL de la API.**
2. **Construir los encabezados de la solicitud.**
3. **Construir el cuerpo de la solicitud.**
4. **Realizar la detección de contenido.**
5. **Tomar decisiones basadas en los resultados.**


