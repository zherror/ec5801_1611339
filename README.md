## Tarea 3 (Fecha de entrega: 05/06/2026):

**Importación de Módulos Necesarios**

```
import logging

import threading

import time

from typing import Callable, Any, Dict, Optional
```

**Registro de Eventos (Logging) en Python**

Objetivo: Familiarizarte con la biblioteca logging de Python, que viene instalada por defecto, y comprender sus diferentes niveles y modos de funcionamiento.

*Tarea:*

1. Crea un script de Python (.py) dedicado exclusivamente a probar el módulo logging.

2. Asegúrate de implementar y demostrar el uso de los distintos niveles de registro (o severidad) de mensajes: DEBUG, INFO, WARNING, y ERROR.


--- 

**Gestión Avanzada de Hilos (Threading)**

Objetivo: Aplicar tus conocimientos sobre concurrencia para diseñar e implementar una clase robusta que actúe como un Gestor de Hilos utilizando la biblioteca threading.

Requisitos de la Clase Gestora:

1. Límite de Concurrencia: En la inicialización (init), la clase debe recibir un número entero que defina la cantidad total de hilos que pueden ejecutarse de manera concurrente, esto se conoce como Backlog.

2. Registro de Hilos: Se debe implementar el método Thread_Allocate.

3. Este método permitirá registrar un hilo, asignándole un nombre y el Callable (la función) que ejecutará.

4. Debe aceptar argumentos posicionales y/o de palabra clave variádicos (*args y **kwargs) para la función a ejecutar.

5. La información del hilo debe almacenarse en una estructura de datos interna (por ejemplo, un diccionario).

6. Registro de Callbacks: Se debe implementar el método Thread_Callback_Register. Este método permitirá asociar funciones callback a los hilos ya registrados pero no en ejecución:

7. Callback_Start: Función que se invoca justo al momento de iniciar la ejecución del hilo.

8. Callback_End: Función que se invoca justo al momento de finalizar la ejecución del hilo.

9. Inicio de Ejecución: Se debe implementar el método Thread_Start. Este método recibirá el nombre de un hilo registrado y comenzará su ejecución, respetando y gestionando los límites de concurrencia establecidos.


---

**Sincronización con Eventos (Threading.Event)**

Objetivo: Ampliar la funcionalidad del Gestor de Hilos implementado, utilizando la clase Event de la biblioteca threading para garantizar la sincronización adecuada.

Requisitos de Ampliación:

1. Evento de Terminación: Integra un objeto Event de terminación para cada uno de los hilos gestionados.

2. Finalización Síncrona: Después de iniciar la función principal, asegúrate de realizar el correspondiente join() para cada hilo.

3. Propósito: Esta implementación busca hacer síncrona la finalización de la ejecución del hilo (a través del evento y el join()) antes de que el resto del código principal del programa continúe su flujo.

4. Detención de Hilos por Nombre: Implementa el método Thread_End en el Gestor de Hilos. Este método debe recibir el nombre de un hilo y, utilizando el objeto Event de terminación, señalar la detención de la ejecución para que el hilo pueda finalizar de forma controlada.