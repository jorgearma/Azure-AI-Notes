Clases principales
MediaType (Enum):

Define el tipo de contenido que se va a analizar: texto (Text) o imagen (Image).

Category (Enum):

Define las categorías de contenido que se pueden analizar:

Hate: Contenido de odio.

SelfHarm: Contenido relacionado con autolesiones.

Sexual: Contenido sexual.

Violence: Contenido violento.

Action (Enum):

Define las acciones que se pueden tomar después del análisis:

Accept: Aceptar el contenido.

Reject: Rechazar el contenido.

DetectionError (Excepción):

Maneja errores que pueden ocurrir durante la detección de contenido.

Decision (Clase):

Representa la decisión tomada después de analizar el contenido. Contiene:

suggested_action: La acción sugerida (Aceptar o Rechazar).

action_by_category: Un diccionario que indica la acción para cada categoría.

ContentSafety (Clase principal):

Esta clase contiene la lógica para interactuar con el Azure Content Safety API. Incluye métodos para:

Construir la URL de la API.

Construir los encabezados de la solicitud.

Construir el cuerpo de la solicitud.

Realizar la detección de contenido.

Tomar decisiones basadas en los resultados.

