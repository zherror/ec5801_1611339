

# Tarea 1:
# Clases
class Matriz:
    N:float# Columnas
    M:float # Filas
    matriz:list # Matriz

    def __init__(self, M, N, *arg:list):
        self.N = N
        self.M = M
        self.matriz = [] # La matriz será formada por listas dentro de una de lista, siendo la lista que guarda todas las listas dadas por las M filas y las listas internas dadas por las N columnas. 

        # Usando arg añadimos cada fila.
        for i in range(M):
            self.matriz.append(arg[i])
        
        # No hay verificación de si las filas (listas) recibidas cumplen con el valor dado, así que en caso de no coincidir da error.

    # Empezamos con las operaciones solicitadas para cada matriz.
    # Suma
    def __add__(self, other):
        # Usamos arg para pasar las filas de la matriz resultante de la suma y retornar la matriz completa. No es capaz de determinar si se cumplen los requisitos para realizar la operación, así que si no se cumple da error.
        arg = []
        for i in range(self.M):
            arg.append([])
            for j in range(self.N):
                arg[i].append(self.matriz[i][j] + other.matriz[i][j])    
        
        return Matriz(self.M, self.N, *arg)
        
    def __sub__(self, other):
        # Usamos arg para pasar las filas de la matriz resultante de la resta y retornar la matriz completa. No es capaz de determinar si se cumplen los requisitos para realizar la operación, así que si no se cumple da error.
        arg = []
        for i in range(self.M):
            arg.append([])
            for j in range(self.N):
                arg[i].append(self.matriz[i][j] - other.matriz[i][j])    
        
        return Matriz(self.M, self.N, *arg)

    def __mul__(self, other):
        # Usamos arg para pasar las filas de la matriz resultante de la multiplicación y retornar la matriz completa. No es capaz de determinar si se cumplen los requisitos para realizar la operación, así que si no se cumple da error. Usamos la formula para calcular cada elemento de la matriz resultante de la multiplicación: c_ij = suma de a_ik*b_kj.
        arg = []
        acu = 0
        for i in range(self.M):
            arg.append([])
            for j in range(other.N):
                for k in range(self.N):
                    acu += self.matriz[i][k] * other.matriz[k][j]
                
                arg[i].append(acu)
                acu = 0
        
        return Matriz(self.M, self.N, *arg)

    def __truediv__(self, other):
        # En este caso se busca que se prohiba la división, por lo que solo lanzamos un mensaje de error.
        pass

    #Imprimimos la matriz
    def show(self):
        for i in range(self.M):
            print("|", end = "\t")

            for j in range(self.N):
                print(self.matriz[i][j], end = "\t")
            
            print("|")
        print("")

# Herencia
# Se crea la clase para el punto
class Punto:
    __x:float
    __y:float
    __z:float

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
    
    # Para sumar y multiplicar con un escalar, aparte del escalar a usar, se pide varios argumentos para determinar que ejes se quiere sumar/multiplicar.
    # Función de suma de un escalar con uno o más ejes.
    def suma(self, k, *arg):
        for i in range(len(arg)):
            match arg[i]:
                case "x":
                    self.__x += k
                case "y":
                    self.__y += k
                case "z":
                    self.__z += k

    # Función de multiplicación de un escalar con uno o más ejes.
    def multi(self, k, *arg):
        for i in range(len(arg)):
            match arg[i]:
                case "x":
                    self.__x *= k
                case "y":
                    self.__y *= k
                case "z":
                    self.__z *= k

    # Función para imprimir el punto.
    def show(self):
        print("(", self.__x, ",", self.__y, ",", self.__z, ")")

# Definimos la clase vector, hijo de la clase punto.
class Vector(Punto):
    __X:float
    __Y:float
    __Z:float


    def __init__(self, x, y, z):
        self.__X = x
        self.__Y = y
        self.__Z = z
        # Usamos super() para poder usar el esquema del padre ya que de otro modo al usar sus funciones da error.
        super().__init__(x, y, z)

    def magnitud(self):
        return (self.__X**2 + self.__Y**2 + self.__Z**2)**0.5

# Poliformismo
# Importamos una lbrería nativa para simular el tiempo de clectura/escritura del disco.
import time

# Creamos las tres clases que representan las memorias
class DiscoDuro:
    memory:list

    def __init__(self, N:int):
        self.memory = []
        # Para simular la memoria vamos a crear una lista con N elementos, inicialmente todos 0.
        for i in range(N):
            self.memory.append(0)

    def escritura(self, p, data):
        print("Iniciando escritura (Disco Duro)...")
        # Usamos time.sleep() para simular el retardo en la lectura.
        time.sleep(5)
        self.memory[p] = data
        print("Escrito en 5s")
        
        
    def lectura(self, p):
        print("Iniciando lectura (Disco Duro)...")
        time.sleep(5)
        print(self.memory[p])
        print("Leido en 5s")

class RAM:
    memory:list

    def __init__(self, N:int):
        self.memory = []
        # Para simular la memoria vamos a crear una lista con N elementos, inicialmente todos 0.
        for i in range(N):
            self.memory.append(0)

    def escritura(self, p, data):
        print("Iniciando escritura (RAM)...")
        # Usamos time.sleep() para simular el retardo en la lectura.
        time.sleep(2)
        self.memory[p] = data
        print("Escrito en 2s")
        
        
    def lectura(self, p):
        print("Iniciando lectura (RAM)...")
        time.sleep(2)
        print(self.memory[p])
        print("Leido en 2s")

class SRAM:
    memory:list

    def __init__(self, N:int):
        self.memory = []
        # Para simular la memoria vamos a crear una lista con N elementos, inicialmente todos 0.
        for i in range(N):
            self.memory.append(0)

    def escritura(self, p, data):
        print("Iniciando escritura (SRAM)...")
        # Usamos time.sleep() para simular el retardo en la lectura.
        time.sleep(0.5)
        self.memory[p] = data
        print("Escrito en 500ms")
        
        
    def lectura(self, p):
        print("Iniciando lectura (SRAM)...")
        time.sleep(0.5)
        print(self.memory[p])
        print("Leido en 500ms")

# Creamos las funciones polimorficas que nos servirán para leer/escribir sin importar la clase de la memoria.
def escritura(dispositivo, p, data):
    dispositivo.escritura(p, data)

def lectura(dispositivo, p):
    dispositivo.lectura(p)

# Main de script de prueba para las actividades
if __name__ == "__main__":
    print("Iniciando!\n")

    #Prueba de la Actividad 1
    A = Matriz(3, 3, [1, 2, 7], [3, 4, 8], [5, 6, 9])
    print("Tenemos una matriz de", A.M, "filas y", A.N, "columnas, como se muestra a continuación:")
    A.show()

    print("Ahora vamos a probar las operaciones aritmeticas disponibles, sumamos A+A:")

    S = A+A
    S.show()

    print("Restamos A-A:")

    S = A-A
    S.show()
    
    print("Multiplicamos: ")
    S = A*A
    S.show()

    print("Tratamos de dividir, pero no funciona porque se busca deshabilitar la opción.")
    S = A/A
    #S.show() da error porque no hace nada A/A.

    #Prueba de la Actividad 2
    B = Punto(4, 2, 7)
    print("\n\nAhora tenemos un punto B = ", end = " ") 
    B.show()
    print("\nA continuación vamos a sumar 3 al eje \"x\" y \"z\" del punto B:")
    
    B.suma(3, "x", "z")
    B.show()

    print("\nY vamos a multiplicar por 2 su eje en y:")

    B.multi(2, "y")
    B.show()

    print("\nAhora tenemos un vector C =", end = " ")
    
    C = Vector(7, 4, 2)
    C.show()

    print("\nCalculamos su magnitud:", C.magnitud())

    #Prueba de la Actividad 3
    print("\n\nFinalmente, se simula un Disco Duro, RAM y SRAM, originalmente vacios.")
    D = DiscoDuro(5)
    print(D.memory)

    R = RAM(10)
    print(R.memory)

    Sr = SRAM(36)
    print(Sr.memory)

    print("\nPasando a llenarlos con algún dato cualquiera, para luego imprimirlos.\n")

    escritura(D, 1, "Dato 1")
    print("")
    lectura(D, 1)
    print("")

    escritura(R, 5, "Dato 2")
    print("")
    lectura(R, 5)
    print("")

    escritura(Sr, 17, "Dato 3")
    print("")
    lectura(Sr, 17)
    print("")