from producto import producto
from avl_tree import AVL


def prueba_arbol():
    avl = AVL()

    p1 = producto("8410000000011", "Leche Entera 1L", "Lacteos", 1.25, 100, ["Norte", "PastoSA"])
    p2 = producto("8412345678901", "Arroz Largo 1kg", "Cereales", 2.15, 50, ["Arrocera Valencia"])
    p3 = producto("8422222222222", "Aceite Oliva 1L", "Aceites", 5.99, 30, ["Olivar"])

    avl[p1.codigo_barra] = p1
    avl[p2.codigo_barra] = p2
    avl[p3.codigo_barra] = p3

    inorden(avl, avl.root())

def inorden(tree, p):


    print(p.key() ," -> ", p.value().nombre)
    p2 = tree.left(p)
    print(p2.key() ," -> ", p2.value().nombre)
    

    # if p is not None:
    #     inorden(tree, tree.left(p))
    #     print(p.key(), "->", p.value().nombre)
    #     inorden(tree, tree.right(p))


def cargar_datos():
    pass


def unificar():
    pass

if __name__ == "__main__":
    prueba_arbol()