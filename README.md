# EC5801_1611339
Repositorio para los ejercicios de la materia Sistemas Embebidos I, de la Universidad Simón Bolívar.

## Tarea 1 (Fecha de entrega: 15/05/2026):

**Clases**

1. Deben desarrollar una clase que describa una matriz de orden N x M, donde N representa las columnas y M las Filas.
2. Para esta clase haciendo uso de sustitución de operaciones por polimorfismo deben implementar las operaciones matriciales de suma, resta, multiplicación y deshabilitar la división.
3. Deben generar un método para imprimir las matrices en consola de manera organizada.

**Herencia**

1. Deben desarrollar una clase padre que permita describir un punto en 3 dimensiones (X, Y, Z).
2. La clase de tipo punto debe tener sus coordenadas (X, Y, Z) privadas y para poder obtenerlas desde la clase hija hace falta utilizar una función de tipo GETTER.
3. El punto debe tener operaciones como suma de un escalar, multiplicación por un escalar en uno o varios de sus ejes, estas operaciones son públicas.
4. La clase hijo que consumirá la clase Punto será un Vector cuyo origen siempre será 0 y debe tener un único método publico que permita calcular la magnitud del vector.

**Polimorfismo**

1. Se debe crear tres clases distintas, una representara un disco duro, otra representara una memoria ram y por último una representara una memoria sram.
2. Para cada clase se tendrá un método de lectura y uno de escritura para un arreglo de tamaño N que representará su memoria interna. Se deberán modelar los retrasos de lectura y escritura para cada uno según su funcionamiento real (SRAM <- RAM <- Disco Duro).
3. Se deberán crear dos funciones polimórficas que deben aceptar las tres clases como si se tratase de un bus manejador de memoria.
4. Se tendrá un esquema de dos funciones una que se encarga de leer de una posición en memoria y otra que busca escribir en una posición de memoria.

**Restricciones**

1. No se puede usar IA de ningun tipo.
2. No pueden usar librerias que no vengan integrada en python (Nada que se instale con pip).

## Tarea 2 (Fecha de entrega: 02/06/2026):

**Manejo de Archivos**

1. Haciendo uso del manejador de archivos integrado en Python deben generar dos funciones que permitan hacer lo siguiente:
	+ Permitir Leer la información de un archivo sea de texto o binario.
	+ Permitir Escribir la información a un archivo de texto o binario.

2. En base a estas funciones generar una clase que las contenga como método. Haciendo una verificación de que la ruta es valida utilizando la clase de tipo Path.

**PyYAML**

1. Usando la clase para el manejador de archivos como clase padre, generar una clase hija que herede sus métodos. Estos métodos se utilizarán como la base del stream de datos para las funciones de la librería PyYAML.
	
2. Generar un método para la clase hija que permita abrir un archivo, pasar su stream de datos a la librería PyYAML y de esa forma sintetizar el diccionario asociado al archivo ‘.yaml‘.
	
3. El diccionario obtenido debe guardarse en un diccionario privado interno de la clase, siguiendo el siguiente esquema:

```
{
	name:{
		path: str,
		data: dict
	},
	...
}
```

4. Para obtener el valor del archivo se debe tener una función de tipo GETTER, que permita obtener los diccionarios correspondientes basados en el nombre asignado.
	
5. Se debe tener un método adicional que permita modificar un diccionario ya pre-existente usando su nombre como identificador.
	
6. Por último, debe existir un método que permita guardar los valores modificados de el diccionario modificado en el disco haciendo uso de los streams de datos y la librería PyYAML.

**Decoradores y Schemas**

1. Se les proveerá un archivo de Python llamado schema_validator.py, el cual contiene una fabrica de decoradores llamado schema_validator. El uso de este decorador para cualquier función viene definido de la siguiente manera:

```
@schema_validator(schema)
def función_1(*args):
	…
```
	
2. Un Schema es un validador para asegurarse que los datos de un diccionario contienen los tipos asignados y así evitar cualquier error al momento de utilizar los mismos. Ejemplo de un Schema:

```
{
	"key":int,
	"key_2":{
		"variable":str,
		"lista":list
	}
}
```
	
3. El schema que deben validar viene dado por el archivo .yaml a generar. Para esta tarea en particular este archivo aceptara N cantidad de elementos con los siguientes ítems: nombre, altura, peso, edad, lista de habilidades, descripcion.

**Restricciones**

1. No se puede usar IA de ningun tipo.
2. No pueden usar librerías ajenas a PyYAML.

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