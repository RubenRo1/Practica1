"""
Autores:
    Iago Núñez Lourés - iago.nunez.loures@udc.es
    Rubén Rodríguez Catrufo - ruben.rodriguez.catrufo@udc.es
"""

class ingrediente:

    def __init__(self, nombre, es_comodin=False):
        self._nombre = nombre
        self._es_comodin = es_comodin

    def __str__(self):
        return f'{self._nombre} {'(*)' if self._es_comodin else ''}'
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def es_comodin(self):
        return self._es_comodin
    
    @es_comodin.setter
    def es_comodin(self, es_comodin):
        self._es_comodin = es_comodin
