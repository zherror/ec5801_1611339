# EC5801_1611339
Repositorio para los ejercicios de la materia Sistemas Embebidos I, de la Universidad Simón Bolívar.

+ Tarea 1 (Fecha de entrega: 15/05/2026):

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
	2. No pueden usar librerias que no vengan integrada en python (Nada que se instale con pip)

+ Tarea 2:
+ 
