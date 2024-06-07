import csv
from random import *
import os

BICICLETAS_CSV = "bicicletas.csv"

def tomar_ruta_actual(archivo):
    ruta_actual = os.path.dirname(__file__)
    return os.path.join(ruta_actual, archivo)

def cargar_archivo_csv(archivo: str):
    lista = []
    with open(tomar_ruta_actual(f"{archivo}.csv"), 'r', encoding='utf-8') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            fila['id_bike'] = int(fila['id_bike'])
            fila['nombre'] = fila['nombre']
            fila['tipo'] = fila['tipo']
            fila['tiempo'] = int(fila['tiempo'])
            lista.append(fila)
    return lista

def guardar_bicicletas_csv(archivo:str, lista:list):
    with open(archivo, 'w', encoding='utf-8', newline='') as archivo_csv:
        campos = ['id_bike', 'nombre', 'tipo', 'tiempo']
        writer = csv.DictWriter(archivo_csv, fieldnames=campos)
        writer.writeheader()
        writer.writerows(lista)
        
