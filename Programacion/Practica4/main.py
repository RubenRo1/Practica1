from producto import producto
from avl_tree import AVL
import csv
import copy
import ast


avl_super = AVL()
avl_max = AVL()

def cargar_datos():

    with open("inventario_supercompra.csv",newline="") as csvfile:
        producto_supermercado = csv.reader(csvfile,delimiter=",")
        next(producto_supermercado) #Salta la 1º linea
        for row in producto_supermercado:
            producto_supercompra = producto(row[0], row[1], row[2], float(row[3]), int(row[4]), ast.literal_eval(row[5]), row[6])
            avl_super[producto_supercompra.ean] = producto_supercompra

    with open("inventario_mercamax.csv",newline="") as csvfile:
        producto_supermercado2 = csv.reader(csvfile,delimiter=",")
        next(producto_supermercado2) #Salta la 1º linea
        for row in producto_supermercado2:
            producto_mercamax = producto(row[0], row[1], row[2], float(row[3]), int(row[4]), ast.literal_eval(row[5]), row[6])
            avl_max[producto_mercamax.ean] = producto_mercamax


def mostrar_datos(tree,p):
    if p is not None:
        mostrar_datos(tree, tree.left(p))
        print(f"{p.key()} - {p.value().nombre} - {p.value().categoria}")
        print(f"Precio: {p.value().precio}€\nStock: {p.value().stock} unidades\nProveedores: {p.value().proveedores}\nFecha reposicion: {p.value().fecha}\n")
        mostrar_datos(tree, tree.right(p))


def insertar_fusion(tree, p, avl_unificado, incidencias, tipo):

    if p is None:
        return

    insertar_fusion(tree, tree.left(p), avl_unificado, incidencias, tipo)
    
    producto_actual = p.value()
    ean = producto_actual.ean

    if ean not in avl_unificado:
        avl_unificado[ean] = copy.deepcopy(producto_actual)
        
    else:
                
        existe = avl_unificado[ean]

        stock1 = existe.stock
        stock2 = producto_actual.stock
        precio1 = existe.precio
        precio2 = producto_actual.precio
        fecha1 = existe.fecha
        fecha2 = producto_actual.fecha
        proveedores1 = existe.proveedores.copy()
        proveedores2 = producto_actual.proveedores.copy()
                
        existe.stock += producto_actual.stock

        for proveedores in producto_actual.proveedores:
            if proveedores not in existe.proveedores:
                existe.proveedores.append(proveedores)
                
        if tipo == "Unificar":
            
            if producto_actual.fecha > existe.fecha:        
                existe.precio = producto_actual.precio
                existe.fecha = producto_actual.fecha
        else:

            if producto_actual.precio > existe.precio:
                existe.precio = producto_actual.precio
                
            if producto_actual.fecha > existe.fecha:
                existe.fecha = producto_actual.fecha
                    
        incidencia = (
            f"{ean} ({existe.nombre}) (SC) vs (MM)\n"
            f"Stock: {stock1} + {stock2} -> {existe.stock}\n"
            f"Precio: {precio1}€ vs {precio2}€ -> {existe.precio}\n"
            f"Proveedores: {proveedores1} vs {proveedores2} -> {existe.proveedores}\n"
            f"Fecha reposicion:  {fecha1} vs {fecha2} -> {existe.fecha}")
                
        incidencias.append(incidencia)


    insertar_fusion(tree, tree.right(p), avl_unificado, incidencias, tipo)
            

def unificar(avl_max, avl_super, tipo):

    avl_unificado = AVL()

    incidencias = []

    insertar_fusion(avl_super, avl_super.root(), avl_unificado, incidencias, tipo)
    insertar_fusion(avl_max, avl_max.root(), avl_unificado, incidencias, tipo)

    return avl_unificado, incidencias


def generar_informe_fusion(avl_super, avl_max, avl_unificado, resultado, tipo):
    
    print(f"="*60)
    print(f"INVENTARIO {resultado} - MegaMercado")
    print(f"Fusión de SuperCompra (SC) y MegaMax (MM) ({tipo})")
    print(f"="*60, "\n")
    
    compartidos = len(avl_max) + len(avl_super) - len(avl_unificado)
    unicos = len(avl_unificado) - compartidos

    print(f"INFORME DE FUSION")
    print(f"="*20, "\n")
    print(f"Productos en SuperCompra (SC): {len(avl_super)}" )
    print(f"Productos en MegaMax (SC): {len(avl_max)}")
    print(f"Productos únicos: {unicos}")
    print(f"Productos compartidos: {compartidos}\n")


if __name__ == "__main__":
    cargar_datos()
    avl_unificado, incidencias = unificar(avl_max, avl_super,"Unificar")

    generar_informe_fusion(avl_super, avl_max, avl_unificado, "UNIFICADO","Solo productos compartidos")
    
    print(f"INCIDENCIAS:")
    print("="*30,"\n")

    for incidencia in incidencias:
        print(incidencia, "\n")

    """
    Hice el punto 2 de la tarea q es Inventario unificado pero falta la ultima parte q esel informe de la fusion, lo q muestra y tal osea creo q es
    hacer full prints, rollo STOCK SUPER1 + SUPER2 = NUEVO STOCK.
    Faltaria tambn la parte de inventario comun q es lo fusionarlas igual pero poniendo el producto mas caro y luego haciendo el informe de fusion
    de nuevo, no parece complicado pero tiene pinta de dar mcuha pereza skibidi dom dom 
    """
