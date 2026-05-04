from array_ordered_positional_list import ArrayOrderedPositionalList as ListaAlmacen
from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaReceta

from ingrediente import ingrediente
from libro_recetas import libro_recetas
from laboratorio import laboratorio


def leer_ingredientes(path="ingredientes.txt"):
    """
    Lee el fichero de ingredientes y carga el almacén de esencias.

    Crea una Lista Posicional Ordenada basada en arrays para permitir 
    búsquedas binarias eficientes en el laboratorio.

    Parameters
    ----------
    path : str, optional
        Ruta del fichero de texto (por defecto "ingredientes.txt").

    Returns
    -------
    ListaAlmacen
        Lista con objetos de la clase ingrediente cargados y ordenados.
    """
    almacen_esencias = ListaAlmacen()

    with open(path, encoding="utf-8") as f:
        for l in f.readlines():
            ls = l.strip().split(",")

            if len(ls) < 2:
                continue

            es_comodin = len(ls) == 3 and ls[2] == "*"
            nombre, cantidad = ls[0], int(ls[1])

            ingred = ingrediente(nombre, cantidad, es_comodin)
            almacen_esencias.add(ingred)

    print("--------ALMACEN DE ESENCIAS--------")
    print(" | ".join(str(i) for i in almacen_esencias))
    print()

    return almacen_esencias


def leer_recetas(path="recetas.txt"):
    """
    Lee el fichero de recetas y devuelve un objeto libro_recetas.
    Cada poción tiene asociada su propia Lista Posicional Ordenada.
    """
    recetario = libro_recetas()

    with open(path, encoding="utf-8") as f:
        for l in f.readlines():
            ls = l.strip().split(",")

            if len(ls) < 3:
                continue

            pocion, ingr, cant = ls[0], ls[1], int(ls[2])

            if not recetario.existe_receta(pocion):
                recetario.add_receta(pocion, ListaReceta())

            recetario.add_ingrediente_receta(
                pocion,
                ingrediente(ingr, cant)
            )

    print("--------LIBRO DE RECETAS--------")
    print(recetario)

    return recetario


def leer_encargos(lab, path="encargos.txt"):
    """
    Procesa el fichero de encargos en orden de llegada.
    La lógica de creación, actualización de stock y borrado de recetas
    queda delegada en la clase laboratorio.
    """
    with open(path, encoding="utf-8") as f:
        for l in f.readlines():
            ls = l.strip().split(",")

            if len(ls) < 2:
                continue

            pocion, cliente = ls[0], ls[1]
            print("\n--------------------------------\n\n")
            print(f"Nuevo encargo: {pocion} | Solicitado por: {cliente}")

            print(lab.crear_pocion(pocion))

            agotados = lab.del_ingredientes_agotados(pocion)
            if agotados != "":
                print(agotados, end="" if agotados.endswith("\n") else "\n")

            print(lab.stock_actual())
            print()


if __name__ == "__main__":
    almacen = leer_ingredientes()
    recetario = leer_recetas()

    lab = laboratorio(recetario, almacen)

    leer_encargos(lab)

    print("--------LIBRO DE RECETAS FINAL--------")
    print(recetario)