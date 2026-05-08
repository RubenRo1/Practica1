"""
Autores:
    Iago Núñez Lourés - iago.nunez.loures@udc.es
    Rubén Rodríguez Catrufo - ruben.rodriguez.catrufo@udc.es
"""

from inventario import Inventario

def mostrar_incidencias(incidencias):
    """Muestra las incidencias generadas durante
    la fusión de inventarios.

    Parameters
    ----------
    incidencias : list
        Lista de incidencias en formato texto.

    Returns
    -------
    None.
    """
    print("INCIDENCIAS:")
    print("="*30,"\n")
    if len(incidencias) == 0:
        print("No hay productos compartidos.\n")
        return
    
    for incidencia in incidencias:
        print(incidencia, "\n")

def generar_informe_fusion(inventario_super, inventario_max, incidencias, resultado, tipo):
    """Genera el informe de fusión de inventarios.

    Parameters
    ----------
    inventario_super : Inventario
        Inventario de SuperCompra.
    inventario_max : Inventario
        Inventario de MegaMax.
    incidencias : list
        Lista de incidencias generadas durante la fusión.
    resultado : str
        Tipo de inventario generado
        (UNIFICADO o COMÚN).
    tipo : str
        Descripción del tipo de fusión.

    Returns
    -------
    None.
    """
    print("="*60)
    print(f"INVENTARIO {resultado} - MegaMercado")
    print(f"Fusión de SuperCompra (SC) y MegaMax (MM) ({tipo})")
    print("="*60, "\n")

    compartidos = inventario_super.contar_compartidos(inventario_max)
    unicos = inventario_super.contar_unicos(inventario_max)

    print("INFORME DE FUSION")
    print("="*20, "\n")
    print(f"Productos en SuperCompra (SC): {len(inventario_super)}" )
    print(f"Productos en MegaMax (MM): {len(inventario_max)}")
    print(f"Productos únicos: {unicos}")
    print(f"Productos compartidos: {compartidos}\n")

    mostrar_incidencias(incidencias)

def pausa():
    """Pausa la ejecución del programa hasta que
    el usuario pulse ENTER.

    Parameters
    ----------
    None.

    Returns
    -------
    None.
    """
    input("\nPulse ENTER para continuar ")

def menu():
    """
    Muestra el menú principal del programa y
    gestiona las operaciones disponibles.

    Options
    -------
    1 : Cargar datos.
    2 : Mostrar inventarios originales.
    3 : Generar inventario unificado.
    4 : Generar inventario común.
    5 : Salir del programa.

    Returns
    -------
    None.
    """

    inventario_super = Inventario("SuperCompra")
    inventario_max = Inventario("MegaMax")
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

                inventario_super.cargar_csv("inventario_supercompra.csv")
                inventario_max.cargar_csv("inventario_mercamax.csv")
                
                print("\nDatos cargados correctamente.")

                pausa()
            
            case "2":
                if not cargados:
                    print("\nPrimero debes cargar los datos.")
                    continue

                print("\n--- INVENTARIO SUPERCOMPRA ---")
                inventario_super.mostrar_inorden()

                print("\n--- INVENTARIO MEGAMAX ---")
                inventario_max.mostrar_inorden()

                pausa()

            case "3":
                if not cargados:
                    print("\nPrimero debes cargar los datos.")
                    continue

                inventario_unificado, incidencias = (inventario_super.fusionar_unificado(inventario_max, "MegaMercado"))
                generar_informe_fusion(inventario_super, inventario_max, incidencias, "UNIFICADO","Todos los productos")      

                print("\n")
                
                inventario_unificado.mostrar_inorden()

                pausa()

            case "4":
                
                if not cargados:
                    print("\nPrimero debes cargar los datos.")
                    continue

                inventario_unificado, incidencias = (inventario_super.fusionar_comun(inventario_max, "MegaMercado"))
                generar_informe_fusion(inventario_super, inventario_max, incidencias, "COMÚN","Solo productos compartidos")      

                print("\n")
                
                inventario_unificado.mostrar_inorden()
    
                pausa()
            case "5":
                
                print("\nSaliendo del programa...")
                break

            case _:

                print("\nERROR\nOpción inválida")


if __name__ == "__main__": 
    menu()
