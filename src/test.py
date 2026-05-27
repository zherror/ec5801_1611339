# Librerías usadas para esta asignación
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from pathlib import Path

# Clase padre que permite cargar y escribir sobre un archivo, haciendo uso de las funciones que trae por defecto python.
class FILE_MANAGER:
    file_path:Path

    def __init__(self, file_path:Path):
        # Marca error en caso de que no exista el documento o path mencionado
        if not file_path.exists():
            print("\n======================================================")
            print("Archivo o carpeta no encontrados. Vuelva a intentarlo.")
            print("======================================================\n")
            
        self.file_path = file_path

    # Lee archivo
    def load_file(self):
        with open(self.file_path, "r") as f:
            return f.read()     

    # Escribe archivo
    def dump_file(self, data):
        with open(self.file_path, "w") as f:
            f.write(data)

# Creamos la clase hija de FILE_MANAGER que permite cargar los archivos en YAML
class YAML_MANAGER(FILE_MANAGER):
    file_path:Path

    def __init__(self, file_path):
        self.file_path = file_path
        super().__init__(file_path)

    def file_to_yaml(self):
        stream = self.load_file()
        print(stream)

if __name__ == "__main__":
    YAML_MANAGER(Path("./files/test.txt")).file_to_yaml()
