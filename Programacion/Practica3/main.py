from array_ordered_positional_list import ArrayOrderedPositionalList as ListaAlmacen
from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaReceta

from ingrediente import ingrediente
from libro_recetas import libro_recetas
from laboratorio import laboratorio


def leer_ingredientes(path="ingredientes.txt"):
    """
    Lee el fichero de ingredientes y devuelve una lista posicional ordenada
    con el almacén de esencias.
    """
    almacen = ListaAlmacen()

    with open(path, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()

            if linea == "":
                continue

            partes = linea.split(",")

            nombre = partes[0]
            cantidad = int(partes[1])
            es_comodin = len(partes) == 3 and partes[2] == "*"

            almacen.add(ingrediente(nombre, cantidad, es_comodin))

    return almacen


def leer_recetas(path="recetas.txt"):
    """
    Lee el fichero de recetas y devuelve un libro_recetas.
    Cada poción tiene asociada una Lista Posicional Ordenada de ingredientes.
    """
    recetario = libro_recetas()

    with open(path, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()

            if linea == "":
                continue

            pocion, nombre_ingrediente, cantidad = linea.split(",")

            if not recetario.existe_receta(pocion):
                recetario.add_receta(pocion, ListaReceta())

            lista_ingredientes = recetario.get_ingredientes(pocion)
            lista_ingredientes.add(ingrediente(nombre_ingrediente, int(cantidad)))

    return recetario


def imprimir_almacen_inicial(almacen):
    """
    Imprime el almacén inicial en el formato pedido.
    """
    print("--------ALMACEN DE ESENCIAS--------")
    print(" | ".join(str(ing) for ing in almacen))


def imprimir_libro_recetas(recetario, titulo="--------LIBRO DE RECETAS--------"):
    """
    Imprime el libro de recetas.
    """
    print(titulo)
    print(recetario, end="")


def procesar_encargos(lab, path="encargos.txt"):
    """
    Procesa todos los encargos del fichero.
    """
    with open(path, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()

            if linea == "":
                continue

            pocion, cliente = linea.split(",")

            print(f"Nuevo encargo: {pocion} | Solicitado por: {cliente}")

            print(lab.crear_pocion(pocion))

            agotados = lab.del_ingredientes_agotados(pocion)
            if agotados:
                print(agotados)

            print(lab.stock_actual())
            print()


def main():
    almacen = leer_ingredientes()
    recetario = leer_recetas()

    lab = laboratorio(recetario, almacen)

    imprimir_almacen_inicial(almacen)
    imprimir_libro_recetas(recetario)
    print()

    procesar_encargos(lab)

    imprimir_libro_recetas(
        recetario,
        "--------LIBRO DE RECETAS FINAL--------"
    )


if __name__ == "__main__":
    main()