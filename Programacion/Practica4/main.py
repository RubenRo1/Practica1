from producto import producto
from avl_tree import AVL
import csv
import copy
import ast


avl_super = AVL()
avl_max = AVL()

def cargar_datos():
    with open("Practica4/inventario_supercompra.csv",newline="") as csvfile:
        producto_supermercado = csv.reader(csvfile,delimiter=",")
        next(producto_supermercado) #Salta la 1º linea
        for row in producto_supermercado:
            producto_supercompra = producto(row[0], row[1], row[2], float(row[3]), int(row[4]), ast.literal_eval(row[5]), row[6])
            avl_super[producto_supercompra.ean] = producto_supercompra

    with open("Practica4/inventario_mercamax.csv",newline="") as csvfile:
        producto_supermercado2 = csv.reader(csvfile,delimiter=",")
        next(producto_supermercado2) #Salta la 1º linea
        for row in producto_supermercado2:
            producto_mercamax = producto(row[0], row[1], row[2], float(row[3]), int(row[4]), ast.literal_eval(row[5]), row[6])
            avl_max[producto_mercamax.ean] = producto_mercamax


def mostrar_datos(tree,p):
     if p is not None:
        mostrar_datos(tree, tree.left(p))
        print(f"Codigo: {p.key()} -> {p.value()}")
        mostrar_datos(tree, tree.right(p))


def insertar_unificado(tree, p, avl_unificado):

    if p is not None:
        insertar_unificado(tree, tree.left(p), avl_unificado)

        producto_actual = p.value()
        ean = producto_actual.ean

        if ean not in avl_unificado:

            avl_unificado[ean] = copy.deepcopy(producto_actual)

        else:
            
            existe = avl_unificado[ean]
            existe.stock += producto_actual.stock

            for proveedores in producto_actual.proveedores:
                if proveedores not in existe.proveedores:
                    existe.proveedores.append(proveedores)

            if producto_actual.fecha > existe.fecha:
                
                existe.precio = producto_actual.precio
                existe.fecha = producto_actual.fecha

        insertar_unificado(tree, tree.right(p), avl_unificado)

def unificar(avl_max, avl_super):

    avl_unificado = AVL()

    insertar_unificado(avl_super, avl_super.root(), avl_unificado)
    insertar_unificado(avl_max, avl_max.root(), avl_unificado)

    return avl_unificado


if __name__ == "__main__":
    cargar_datos()
    print(f"--------------DATOS SUPERCOMPRA--------------")
    mostrar_datos(avl_super, avl_super.root())
    print(f"--------------DATOS MERCAMAX--------------")
    mostrar_datos(avl_max, avl_max.root())
    print(f"--------------FUUUUUUUUSION--------------")
    avl_unificado = unificar(avl_max, avl_super)

    mostrar_datos(avl_unificado, avl_unificado.root())


    """
    Hice el punto 2 de la tarea q es Inventario unificado pero falta la ultima parte q esel informe de la fusion, lo q muestra y tal osea creo q es
    hacer full prints, rollo STOCK SUPER1 + SUPER2 = NUEVO STOCK.
    Faltaria tambn la parte de inventario comun q es lo fusionarlas igual pero poniendo el producto mas caro y luego haciendo el informe de fusion
    de nuevo, no parece complicado pero tiene pinta de dar mcuha pereza skibidi dom dom 
    """
