from manipulacion_csv import *

lista = cargar_archivo_csv("bicicletas")

def filtrar_lista(lista:list):
    """
    Filtro para obtener los tipos de bicicleta
    Args:
        lista (list): lista de bicicletas

    Returns:
        lista_nueva: Lista con solo los tipos de bicicleta
    """
    lista_nueva = []
    for ele in lista:
        if ele["tipo"]:
            lista_nueva.append(ele["tipo"])
    return lista_nueva  

filtro = list(set(filtrar_lista(lista)))

def validar_input_filtro():
    """
    Validacion de input de tipos de bicicleta
    Returns:
        aux: retorna el dato pasado por el input
    """
    aux = input("Ingrese el tipo de bicicleta: ").upper()
    while aux not in filtro:
        print("Tipo de bicicleta no válido. PASEO, MTB, PLAYERA, BMX.")
        aux = input("Ingrese el tipo de bicicleta: ").upper()
    return aux