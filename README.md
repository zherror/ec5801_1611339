## Tarea 4 (Fecha de entrega: 12/06/2026):

# Comunicación Inter-Hilos con Colas Seguras

El objetivo de esta tarea es diseñar e implementar un sistema de mensajería robusto que permita el intercambio de datos entre hilos, de forma segura haciendo uso del módulo queue de Python.

**Gestión de Colas**

Deben desarrollar un gestor de colas como una clase central llamada Messages_Manager la cual debe permitir crear y eliminar colas en tiempo de ejecución.

- **Creación de Colas:** Implementar el método create. Este método debe generar una instancia de Queue recibiendo el máximo valor de parámetros que la cola podrá y asociarla a un identificador único (nombre) en un diccionario interno.

- **Asociación de Callbacks:** El método de creación debe permitir asignar una función con el tipo genérico Callable en un segundo diccionario interno, asociando por el identificador único (nombre).

- **Eliminación Segura:** Implementar el método delete para remover colas del sistema y liberar los recursos asociados, asegurando que posteriormente no se pueda acceder a los identificadores utilizados con anterioridad.

**Sincronización y Exclusión Mutua (Mutex)**

Se debe garantizar la integridad de las estructuras de datos compartidas dicts mediante el uso de bloqueos locks.

- **Protección de Recursos:** Usando los objetos de tipo Lock se debe asegurar que todas las operaciones de lectura y escritura sobre los diccionarios internos estén protegidas.

**Intercambio de Mensajes**

Se debe implementar los mecanismos de envío, recepción y procesamiento automático de mensajes de forma que pueda seguir el flujo principal de ejecución.

- **Envío de Datos:** Crear el método send que deposite información en una cola específica basándose en su nombre. Esta operación debe ser segura para hilos y bloqueante en caso de que la cola este totalmente llena.

- **Recepción No Bloqueante:** Implementar el método receive para extraer datos de una cola. Se debe configurar para que sea una operación de tipo no bloqueante, manejando adecuadamente los casos donde la cola esté vacía para evitar errores.

**Polling**

- **Mecanismo de Polling:** Desarrollar un método poll. Este método debe iterar sobre todas las colas activas y, si detecta datos entrantes debe recibirlos, para posteriormente ejecutar automáticamente el callback asociado a cada cola.

**Restricciones y Entrega**

- **Prohibición de IA:** No se permite el uso de herramientas de inteligencia artificial para la resolución de la tarea.

- **Librerías Permitidas:** Solo se pueden utilizar módulos estándar de Python, específicamente `logging`, `threading`, y `queue`.

- **Registro de Eventos:** El gestor debe incluir un sistema de `logging` interno que registre la creación, envío, recepción y errores del sistema.