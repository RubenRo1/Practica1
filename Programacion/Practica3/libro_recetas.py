"""
Autores:
    Iago Núñez Lourés - iago.nunez.loures@udc.es
    Rubén Rodríguez Catrufo - ruben.rodriguez.catrufo@udc.es
"""
from ingrediente import ingrediente
from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenada

class libro_recetas:

    def __init__(self, recetas=None):
        self._recetas = {} if recetas == None else recetas

    def __str__(self):
        salida = ""
        for receta in sorted(self._recetas.keys()):
            salida += f"{receta}\n\t"
            salida += " | ".join(str(ing) for ing in self._recetas[receta])
            salida += "\n"
        return salida

    def existe_receta(self, pocion:str):
        return pocion in self._recetas.keys()

    def add_receta(self, pocion:str, receta:ListaOrdenada):
        self._recetas[pocion] = receta

    def add_ingrediente_receta(self, pocion, ingrediente):
        if self.existe_receta(pocion):
            self._recetas[pocion].add(ingrediente)

    def del_receta(self, pocion):
        if self.existe_receta(pocion):
            del self._recetas[pocion]

    def get_ingredientes(self, pocion:str):
        if not self.existe_receta(pocion):
            return None
        return self._recetas[pocion]
            
    def get_receta(self, pocion):
        if not self.existe_receta(pocion):
            return f'No existe receta de {pocion}'
        
        salida = f'Poción: {pocion}\n'
        for ingrediente in self._recetas[pocion]:
            salida += f'\t- {ingrediente.nombre}: {ingrediente.cantidad}\n'
        return salida
    
    def get_pociones_por_ingrediente(self, ingrediente:ingrediente):
        pociones = []
        for pocion, receta in self._recetas.items():
            if ingrediente in receta:
                pociones.append(pocion)
        return pociones
    
    def del_pociones_por_ingrediente(self, ingrediente:ingrediente):
        recetas_a_eliminar = self.get_pociones_por_ingrediente(ingrediente)
        for receta in recetas_a_eliminar:
            self.del_receta(receta)
        
        return recetas_a_eliminar
    
    @property
    def recetas(self):
        return self._recetas
    
    @recetas.setter
    def recetas(self, recetas):
        self._recetas = recetas
