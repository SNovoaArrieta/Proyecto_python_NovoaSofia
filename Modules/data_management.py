import json
import os

def load_data(file_path):
     # Verifica si el archivo existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo {file_path} no existe.")
    
        # Lee el archivo JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(file_path, data):
       # Guarda los datos en un archivo JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    