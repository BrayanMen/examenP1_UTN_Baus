from funciones_bicicletas import *
from manipulacion_csv import *
from validacion import *
import os

def limpiar_terminal():
    os.system("cls")

def main():
    """
    Menu de aplicacion.
    """
    while True:
        print("Menú:")
        print("1) Cargar archivo .CSV")
        print("2) Imprimir lista")
        print("3) Asignar tiempos")
        print("4) Informar ganador")
        print("5) Filtrar por tipo")
        print("6) Informar promedio por tipo")
        print("7) Mostrar posiciones")
        print("8) Guardar posiciones")
        print("9) Salir")
        opcion = input("Seleccione una opción: ")
        limpiar_terminal()
        
        match str(opcion):
            case "1":
                nombre_archivo = input("Ingrese el nombre del archivo .CSV: ")
                bicicletas_cargadas = cargar_archivo_csv(nombre_archivo)
            case "2":
                mostrar_lista(bicicletas_cargadas)
            case "3":
                asignar_tiempos(bicicletas_cargadas)
                mostrar_lista(bicicletas_cargadas)
            case "4":
                mostrar_lista(ganador_carrera(bicicletas_cargadas))
            case "5":
                filtro = validar_input_filtro()
                filtrar_por_tipo(bicicletas_cargadas,filtro)
                mostrar_lista(bicicletas_cargadas)
            case "6":
                informar_promedio(bicicletas_cargadas)
            case "7":
                ordenar_bicicletas_doble_criterio(bicicletas_cargadas, "tipo", "tiempo")
            case "8":
                nombre_json = input("Ingresar nombre para archivo JSON: ")
                guardar_archivo_json(bicicletas_cargadas, nombre_json)
            case "9":
                print("Hasta luego!!")
                break
                
if __name__ == "__main__":
    main()
