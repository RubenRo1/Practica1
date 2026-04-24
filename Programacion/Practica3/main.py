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
    Lee el fichero de recetas y genera el libro de recetas.

    Cada poción se asocia a una Lista Posicional Ordenada basada en 
    nodos (enlazada) para gestionar sus ingredientes.

    Parameters
    ----------
    path : str, optional
        Ruta del fichero de recetas (por defecto "recetas.txt").

    Returns
    -------
    libro_recetas
        Objeto que contiene el diccionario de fórmulas alquímicas.
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
    Muestra por consola el estado inicial del almacén.

    Parameters
    ----------
    almacen : ListaAlmacen
        La estructura que contiene las existencias iniciales.
    """
    print("--------ALMACEN DE ESENCIAS--------")
    print(" | ".join(str(ing) for ing in almacen))


def imprimir_libro_recetas(recetario, titulo="--------LIBRO DE RECETAS--------"):
    """
    Imprime el contenido del libro de recetas siguiendo el formato pedido.

    Parameters
    ----------
    recetario : libro_recetas
        El catálogo de pociones a mostrar.
    titulo : str, optional
        Encabezado de la sección (por defecto LIBRO DE RECETAS).
    """
    print(titulo)
    print(recetario, end="")


def procesar_encargos(lab, path="encargos.txt"):
    """
    Gestiona la simulación de pedidos de clientes desde un fichero.

    Para cada encargo, solicita al laboratorio la creación de la poción, 
    gestiona el borrado en cascada de ingredientes agotados y muestra 
    el stock actualizado.

    Parameters
    ----------
    lab : laboratorio
        La instancia controladora que ejecuta la lógica.
    path : str, optional
        Ruta del fichero de encargos (por defecto "encargos.txt").
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
    """
    Función de entrada principal (Entry Point) del programa.
    
    Orquesta la carga de datos, la inicialización del laboratorio 
    y la ejecución de la simulación.
    """
    
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