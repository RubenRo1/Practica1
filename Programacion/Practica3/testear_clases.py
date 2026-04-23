from libro_recetas import libro_recetas
from ingrediente import ingrediente
from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenada

patata = ingrediente('patata')
bacon = ingrediente('bacon')
queso = ingrediente('queso', True)
print(bacon)
print(queso)

recetas = {'bacon_y_patatas':{bacon:1, patata:3}}
libro = libro_recetas(recetas)
print(libro)
libro.add_recetas('bacon_solo', {bacon:3})
print(libro)

lista = ListaOrdenada()
lista.add(bacon)

print(lista.first().element())