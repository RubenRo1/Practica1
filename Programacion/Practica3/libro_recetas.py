"""
Autores:
    Iago Núñez Lourés - iago.nunez.loures@udc.es
    Rubén Rodríguez Catrufo - ruben.rodriguez.catrufo@udc.es
"""

class libro_recetas:
    '''
    Esperar a que samuel nos resuelva la duda de la lista ordenada
    '''

    def __init__(self, recetas=None):
        self._recetas = {} if recetas is None else recetas

    def existe_receta(self, pocion):
        return pocion in self._recetas.keys()

    def add_receta(self, pocion, receta):
        self._recetas[pocion] = receta

    def add_ingrediente_receta(self, pocion, ingrediente, catidad):
        pass

    def del_receta(self, pocion):
        if self.existe_receta(pocion):
            self._recetas.pop(pocion)

    def print_receta(self, pocion):
        if not self.existe_receta(pocion):
            return ''
        
        salida = f'Poción: {pocion}\n'
        for ingrediente in self._recetas[pocion]:
            salida += f'\t- {ingrediente.nombre}: {self._recetas[pocion][ingrediente]}\n'
        return salida

    def __str__(self):
        salida = ''
        for receta in self._recetas.keys():
            salida += f'{receta}\n\t{self._recetas[receta]}'
            for ingrediente in self._recetas[receta]:
                salida += f'{ingrediente.nombre}: {self._recetas[receta][ingrediente]} | '
            salida += '\n'
        return salida
    
    @property
    def recetas(self):
        return self._recetas
    
    @recetas.setter
    def recetas(self, recetas):
        self._recetas = recetas
