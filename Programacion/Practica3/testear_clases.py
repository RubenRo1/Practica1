from libro_recetas import libro_recetas
from ingrediente import ingrediente
from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenada

patata = ingrediente('patata',2)
bacon = ingrediente('bacon',2)
queso = ingrediente('queso',2, True)
print(bacon)
print(queso)

recetas = {'bacon_y_patatas':{bacon:2, patata:4}} #Cambiar para que funcione
libro = libro_recetas(recetas)
print(libro)
libro.add_recetas('bacon_solo', {bacon:3})
print(libro)

lista = ListaOrdenada()
lista.add(bacon)

print(lista.first().element())