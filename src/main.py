"""
UNIVERSIDAD SIMÓN BOLÍVAR
Departamento de Electrónica y Circuitos
Materia: EC5801 - Sistemas Embebidos 1
Trimestre: Abril - Julio 2026

Asignación: Tarea 4 - Comunicación Inter-Hilos con Colas Seguras
Autor: Gerónimo Velasco
"""

import logging

from threading import Thread, Event, Lock
from queue import Queue
from typing import Callable, Dict, Any

import time
from time import sleep

# Configuración básica del logging
logging.basicConfig(
    level=logging.INFO,  
    format='%(levelname)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S',  
    handlers=[
        logging.FileHandler("registro.log"), 
        logging.StreamHandler() 
    ]
)

# Gestor de Colas
class Messages_Manager:
    # Se crea diccionarios para almacenar las colas y sus callbacks, además una lista con los <name> bloqueados debido a que ya fueron utilizados y el lock.
    queues:dict
    callbacks:dict
    blocked:list[str]
    lock = Lock()

    # Función de inicio de la clase sin nada especial.
    def __init__(self):
        self.queues = {}
        self.callbacks = {}
        self.blocked = []

    # Método que crea las colas, recibe el <name>, el tamaño máximo de elementos que almacena la cola y el callback. Da error si la cola ya existe o si se utiliza un <name> que ya fue utilizado.
    def create(self, name:str, max_size:int, callback:Callable):
        with self.lock:
            if name in list(self.queues.keys()) or name in self.blocked:
                logging.error(f"La cola ya existe o el <name> = {name} ya fue usado.")
            else:
                self.queues[name] = Queue(maxsize=max_size)
                self.callbacks[name] = callback

                logging.info(f"Se creo la cola {name} correctamente.")

    # Método para eliminar las colas, primero revisa si existe la cola que se quiera eliminar para eliminarla y agregar su <name> a la lista de los identidicadores ya usado, o en caso contrario avisa de que no existe la cola que se desea eliminar.
    def delete(self, name:str):
        with self.lock:
            if name in list(self.queues.keys()):
                self.queues[name].shutdown()
                self.queues.pop(name)
                self.blocked.append(name)

                logging.info(f"Se elimino la cola {name} correctamente.")
            else:
                logging.error(f"La cola {name} no existe.")

    # Método que envia datos a la cola, revisando si la cola esta llena o no existe para dar error. 
    def send(self, name:str, data:Any):
        with self.lock:
            if name not in list(self.queues.keys()):
                logging.error(f"El <name> = {name} no existe.")
            else:
                self.queues[name].put(data, block=True)
                logging.info(f"Se envió el dato correctamente a la cola {name}.")

    # Método que recibe/saca los datos de la cola, igualmente saltando un aviso de error si ya no hay más datos en la cola o si está no existe.
    def receive(self, name:str):
        with self.lock:
            if name not in list(self.queues.keys()):
                logging.error(f"El <name> = {name} no existe.")
            elif self.queues[name].empty() == True:
                logging.error(f"La cola {name} está vacia.")
            else:
                logging.warning(f"Una vez extraido el dato de la cola, ya no está en la misma y no es recuperable.")
                data = self.queues[name].get(block=False)
                logging.info(f"Se recibió el dato correctamente de la cola {name}.")
                return data
            
    # Es un poll para revisar todos los datos en las colas y enviarlos a sus respectivos callbacks y ser ejecutados.
    def poll(self):
        logging.info("Inició el poll...")
        for name in list(self.queues.keys()):
            while not self.queues[name].empty():
                self.callbacks[name](self.receive(name))

        logging.info("Terminó el poll.")

# Función de prueba 1.
def test_1(data:str):
    print(f"Tenemos la cadena de caracteres: {data}")    

# Función de prueba 2.
def test_2(data:int):
    print(f"Tenemos el número entero: {data}")

if __name__ == "__main__":
    # Se crea la clase gestora de colas.
    k = Messages_Manager()
    # Se prueba si se crea correctamente la cola.
    k.create("Casa", 3, test_1)
    # Se prueba si da error en caso de repetición del <name>.
    k.create("Casa", 7, test_2)
    # Se borra la cola creada anteriormente.
    k.delete("Casa")
    # Se trata de borrar nuevamente para ver si funciona el error correctamente.
    k.delete("Casa")
    # Se procede a crear dos colas.
    k.create("Pera", 3, test_1)
    k.create("Toronja", 7, test_2)
    # Se envia datos a la cola Pera.
    k.send("Pera", 79)
    # Se imprime el dato enviado usando el método receive().
    print("Se imprime el dato almacenado en la cola", k.receive("Pera"))
    # Se prueban los errores para el método receive().
    print("Se trata de imprimir otro dato en la cola", k.receive("Pera"))
    print("Se trata de imprimir otro dato en la cola", k.receive("Manzana"))
    # Se pasan nuevos datos a las colas
    k.send("Pera", "Lore")
    k.send("Pera", "Ipsum")
    k.send("Pera", "Paralelepipedo")
    k.send("Toronja", 12)
    k.send("Toronja", 76)
    k.send("Toronja", 18)
    # Se procede a ejecutar el método poll para ver si funciona correctamente.
    k.poll()
