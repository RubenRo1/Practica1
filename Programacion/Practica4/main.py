from producto import producto
from avl_tree import AVL
import csv


avl_super = AVL()
avl_max = AVL()


def cargar_datos():
    with open("Practica4/inventario_supercompra.csv",newline="") as csvfile:
        producto_supermercado = csv.reader(csvfile,delimiter=",")

        for row in producto_supermercado:
            producto_supercompra = producto(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            avl_super[producto_supercompra.codigo_barra] = producto_supercompra

    with open("Practica4/inventario_mercamax.csv",newline="") as csvfile:
        producto_supermercado2 = csv.reader(csvfile,delimiter=",")

        for row in producto_supermercado2:
            producto_mercamax = producto(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            avl_max[producto_mercamax.codigo_barra] = producto_mercamax


def mostrar_datos(tree,avl_super):
     
     if avl_super is not None:
        mostrar_datos(tree, tree.left(avl_super))
        print(f"Codigo: {avl_super.key()} -> {avl_super.value()}")
        mostrar_datos(tree, tree.right(avl_super))

def unificar():
    pass

if __name__ == "__main__":
    cargar_datos()
    mostrar_datos(avl_super, avl_super.root())