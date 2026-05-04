from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenadaLinked
from array_ordered_positional_list import ArrayOrderedPositionalList as ListaOrdenadaArray
from ingrediente import ingrediente
from libro_recetas import libro_recetas

def leer_ingredientes(path="ingredientes.txt"):
    almacen_esencias = ListaOrdenadaArray()
    with open(path) as f:
        print("--------ALMACEN DE ESENCIAS--------")
        for l in f.readlines():
            ls = l.strip().split(",")
            es_comodin = len(ls) == 3 and ls[2] == '*'
            nombre, cantidad = ls[0], int(ls[1])
            
            ingred = ingrediente(nombre, cantidad,es_comodin)
            almacen_esencias.add(ingred)

            # print (f"POR HACER: añadir al almacén \"{nombre}\" {es_comodin} con ({cantidad} unidades)")   
            # print(f"{ingred} : ",end=" | ")
        
        print(" | ".join(str(i) for i in almacen_esencias))   


def leer_recetas(path="recetas.txt"):
    with open(path) as f:
        for l in f.readlines():
            ls = l.strip().split(",")
            pocion, ingr, cant = ls[0], ls[1], int(ls[2])
            print (f"POR HACER: añadir al recetario  \"{ingr}\" ({cant} unidades) de la poción \"{pocion}\"")

def leer_encargos(path="encargos.txt"):
    with open(path) as f:
        for l in f.readlines():
            ls = l.strip().split(",")
            pocion, cliente = ls[0], ls[1]
            print (f"POR HACER: procesar pedido {pocion} del cliente {cliente}")
			
if __name__ == "__main__":
    # leer_ingredientes()
    leer_recetas() 
    # leer_encargos()

"""
almacen es dicc con ingrediente cantidad (o quizas una clase laboratorio 
que cree las pociones y almacene los ingredientes??)
ingrediente es una clase con nombre y es_comodin
libro de recetas es una clase que almacena un dicc con ingrediente y cantidad
"""            