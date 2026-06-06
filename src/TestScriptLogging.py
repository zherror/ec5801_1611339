"""
UNIVERSIDAD SIMÓN BOLÍVAR
Departamento de Electrónica y Circuitos
Materia: EC5801 - Sistemas Embebidos 1
Trimestre: Abril - Julio 2026

Asignación: Tarea 3 - Registro de Eventos (Logging) en Python
Autor: Gerónimo Velasco
"""

import logging

import threading

import time

from typing import Callable, Any, Dict, Optional

# Configuración del logging.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(name)s - %(levelname)s]: %(message)s\n',
)

# Se nombra el logger.
logger = logging.getLogger("Tester")

# Función que contiene usos para DEBUG, INFO, WARNING y ERROR.
# Se tiene una función que divide dos números a/b, tal que el DEBUG indique que se inició la función, WARNING de que en caso de que a o b sea 0 puede ser que ocurra un errror, INFO para indicar que se va a realizar la división y ERROR para indicar si hay error al dividir.
def TestScript(a, b):
    logger.debug("Inicializando función...")

    if a == 0 or b == 0:
        logger.warning("Existe riesgo de que la división no se pueda realizar.")

    logger.info("Calculando división.")

    try:
        division = a / b
    except ZeroDivisionError as e:
        logger.error("Ocurrió un error en el proceso.")

if __name__ == "__main__":
    a = 10
    b = 0

    TestScript(a, b)