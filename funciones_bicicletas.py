from manipulacion_csv import guardar_bicicletas_csv
from random import *
import json

def mostrar_lista(lista: list)->None:
    """Funcion para mostrar lista

    Args:
        lista (list): lista a mostrar
    """
    print("**\t\t\tListas de Competidore\t\t\t**\n")
    print("ID   |Nombre         |Tipo      |Tiempo")
    print("------------------------------------------")
    for i in range(len(lista)):
        mostrar_fila(lista[i])
    print()

def mostrar_fila(dicto: dict):
    """
    Funciona para mostar elementos en diccionarios
    Args:
        dicto (dict): diccionario
    """
    print(f"{dicto["id_bike"]:<5}|{dicto["nombre"]:15}|{dicto["tipo"]:10}|{dicto["tiempo"]:5}")
        
        
def asignar_tiempos(lista:list)-> list:
    """
    Funcion para asignar tiempos a lista

    Args:
        lista (list): lista de corredores

    Returns:
        lista: lista modificada
    """
    for ele in lista:
        ele["tiempo"] = randint(50,120)
    return lista

def menor_tiempo(lista:list):
    """Encuentra el menor tiempo en la lista de bicicletas.
    Args:
    lista: list of dicts, la lista de diccionarios con los datos de las bicicletas
    Returns:
       int, el menor tiempo encontrado
    """
    menor = lista[0]["tiempo"]
    for ele in lista:
        if ele["tiempo"] < menor:
            menor = ele["tiempo"]
    return menor

def ganador_carrera(lista:list)-> list:
    """
    Funcion que ubica ganador o ganadores de la carrera

    Args:
        lista (list): Lista de bicicletas

    Returns:
        list: lista de ganadores
    """
    if not lista:
        print("No hay datos.")
        
    tiempo_minimo = menor_tiempo(lista)
    
    ganadores = []
    for ele in lista:
        if ele["tiempo"] == tiempo_minimo:
            ganadores.append(ele)
            if len(ganadores) > 1:
                print(f"\t\t\t¡Hubo un empate!\t\t\t")
    return ganadores

def filtrar_por_tipo(list:list, tipo:str):
    """
        Filtra las bicicletas por tipo y guarda en un archivo CSV.
    Args:
        lista (list): la lista de diccionarios con los datos de las bicicletas
        tipo (str): El tipo de bicicleta a filtrar
    """
    bicicletas_filtradas = []
    for ele in list:
        if ele['tipo'] == tipo.upper():
            bicicletas_filtradas.append(ele)
    
    if not bicicletas_filtradas:
        print(f"No hay bicicletas del tipo {tipo}.")
        return
    guardar_bicicletas_csv(f"{tipo.lower()}.csv",bicicletas_filtradas)

def informar_promedio(lista):
    """
        Informa el promedio de tiempo por cada tipo de bicicleta.
    Args:
        lista(list): la lista de diccionarios con los datos de las bicicletas
    """
    if not lista:
        print("Lista vacia.")
        return
    
    tiempos_por_tipo = {}
    for ele in lista:
        tipo = ele['tipo']
        tiempo = ele['tiempo']
        if tipo not in tiempos_por_tipo:
            tiempos_por_tipo[tipo] = []
        tiempos_por_tipo[tipo].append(tiempo)
    
    for tipo, tiempos in tiempos_por_tipo.items():
        promedio = sum(tiempos) / len(tiempos)
        print(f"Tipo: {tipo} y su promedio de tiempo: {promedio:.2f}")
        
def swap_lista(lista:list, i:int, j: int)->None:
    """
    Funcion para intercambia posiciones de la lista

    Args:
        lista (list): Lista completa
        i (int): posicion I
        j (int): posicion J
    """
    lista[i], lista[j] = lista[j], lista[i]
    
        
def ordenar_bicicletas_doble_criterio(lista:list, campo:str,campo_2:str):
    """
    Funcion de ordenamiento segun 2 criterios

    Args:
        lista (list): lista da pasar
        campo (str): Primer Criterio
        campo_2 (str): Segundo Criterio
    """
    tam = len(lista)
    for i in range(tam-1):
        for j in range(i+1, tam):
            if lista[i][campo] == lista[j][campo]:
                if lista[i][campo_2] > lista[j][campo_2]:
                    swap_lista(lista, i, j)            
            else:
                if lista[i][campo] > lista[j][campo]:
                    swap_lista(lista, i , j)   

def guardar_archivo_json(lista:list, ruta:str):
    """
    Funcion que carga lista en archivo JSON

    Args:
        lista (list): Recibe la lista 
        ruta (str): Recibe nombre de la ruta sin la extension
    """
    with open(f"{ruta}.json", 'w', encoding='utf-8') as file:
        json.dump(lista, file, indent=4)



