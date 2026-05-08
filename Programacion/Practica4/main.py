from producto import producto
from inventario import Inventario
from avl_tree import AVL
import csv
import copy
import ast

avl_super = AVL()
avl_max = AVL()

def mostrar_incidencias(incidencias):

    print(f"INCIDENCIAS:")
    print("="*30,"\n")
    if len(incidencias) == 0:
        print("No hay productos compartidos.\n")
        return
    
    for incidencia in incidencias:
        print(incidencia, "\n")

def generar_informe_fusion(avl_super, avl_max, incidencias, resultado, tipo):
    
    print(f"="*60)
    print(f"INVENTARIO {resultado} - MegaMercado")
    print(f"Fusión de SuperCompra (SC) y MegaMax (MM) ({tipo})")
    print(f"="*60, "\n")

    compartidos = avl_super.contar_compartidos(avl_max)
    unicos = avl_super.contar_unicos(avl_max)

    print(f"INFORME DE FUSION")
    print(f"="*20, "\n")
    print(f"Productos en SuperCompra (SC): {len(avl_super)}" )
    print(f"Productos en MegaMax (SC): {len(avl_max)}")
    print(f"Productos únicos: {unicos}")
    print(f"Productos compartidos: {compartidos}\n")

    mostrar_incidencias(incidencias)


def menu():

    avl_super = Inventario("SuperCompra")
    avl_max = Inventario("MegaMax")
    cargados = False

    while True:

        print("\n====== MEGAMERCADO ======")
        print("1: Cargar datos")
        print("2: Mostrar inventarios originales")
        print("3: Inventario unificado")
        print("4: Inventario común")
        print("5: Salir")
        print("====== MEGAMERCADO ======")

        opcion = input("\nSeleccione una opción: ")

        match opcion:
            case "1":

                cargados = True

                avl_super.cargar_csv("inventario_supercompra.csv")
                avl_max.cargar_csv("inventario_mercamax.csv")
                
                print("\nDatos cargados correctamente.")
            
            case "2":
                if not cargados:
                    print(f"\nPrimero debes cargar los datos.")
                    continue

                print(f"\n--- INVENTARIO SUPERCOMPRA ---")
                avl_super.mostrar_inorden()

                print(f"\n--- INVENTARIO MEGAMAX ---")
                avl_max.mostrar_inorden()

            case "3":
                if not cargados:
                    print(f"\nPrimero debes cargar los datos.")
                    continue

                avl_unificado, incidencias = (avl_super.fusionar_unificado(avl_max, "MegaMercado"))
                generar_informe_fusion(avl_super, avl_max, incidencias, "UNIFICADO","Todos los productos")      

                print("\n")
                
                avl_unificado.mostrar_inorden()

            case "4":
                
                if not cargados:
                    print(f"\nPrimero debes cargar los datos.")
                    continue

                avl_unificado, incidencias = (avl_super.fusionar_comun(avl_max, "MegaMercado"))
                generar_informe_fusion(avl_super, avl_max, incidencias, "COMÚN","Solo productos compartidos")      

                print("\n")
                
                avl_unificado.mostrar_inorden()
    
            case "5":
                
                print(f"\nSaliendo del programa...")
                break

            case _:

                print(f"\nERROR\nOpción inválida")


if __name__ == "__main__":
    
    menu()
