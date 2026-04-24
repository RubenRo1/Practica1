"""
Autores:
    Iago Núñez Lourés - iago.nunez.loures@udc.es
    Rubén Rodríguez Catrufo - ruben.rodriguez.catrufo@udc.es
"""
from functools import total_ordering

#Como los ingredientes van a ir en listas posicionales, necesitamos poder compararlos.
#Con el uso de @total ordering, nos ahorramos el reescribir todos los metodos magicos
#de comparacion, y asi podremos comparar simplemente a partir de eq y lt
@total_ordering
class ingrediente:
    """Representa un ingrediente dentro del sistema de pociones.

    Esta clase gestiona la información básica de un ingrediente, incluyendo su
    nombre, cantidad disponible y si es considerado un comodín..

    Attributes
    ----------
    _nombre : str
        Nombre indentificativo del ingrediente.    
    _cantidad : int
        Número total de unidades disponibles en el inventario.
    _es_comodin : bool
        Indica si el ingrediente puede sustituir a otros en una receta.
    """


    def __init__(self, nombre, cantidad:int,es_comodin=False ):
        """Inicializa un nuevo objeto ingrediente.

        Parameters
        ----------
        _nombre : str
            Nombre indentificativo del ingrediente.    
        _cantidad : int
            Número total de unidades disponibles en el inventario.
        _es_comodin : bool
            Indica si el ingrediente puede sustituir a otros en una receta.
            
        Returns
        -------
        None.
        """
        self._nombre = nombre
        self._cantidad = cantidad
        self._es_comodin = es_comodin

    def __lt__(self, otro):
        return self._nombre < otro.nombre
    
    def __eq__(self,value):
        return self._nombre == value.nombre

    def __str__(self):
        marca = " (*)" if self._es_comodin else ""
        return f"{self._nombre}{marca}: {self._cantidad}"
    
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

    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad