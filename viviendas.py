from edificios import Edificio

class Viviendas(Edificio):
    """ Representa un edificio de tipo vivienda.
    
    Esta clase modela un edificio residencial donde viven múltiples hogares.
    Incluye     la capacidad máxima de la vivienda, el número actual de hogares
    y un precio fijo de alquiler por hogar. Proporciona métodos para calcular
    los ingresos generados y para obtener la capacidad disponible.
    
    Attributes
    ----------
    capacidad : int
        Capacidad máxima de la vivienda.
    num_hogares : int
        Número de hogares que ocupan la vivienda.
    _PRECIO_ALQUILER : int
        Variable privada que define el precio fijo del alquiler (300 €).
    Methods
    -------
    calcular_ingresos()
        Devuelve los ingresos generados (num_hogares * precio del alquiler).
    obtener_capacidad_disponible()
        Devuelve la capacidad disponible de la vivienda (siempre 0).     
    """
        
    def __init__(self,capacidad: int, num_hogares: int, nombre : str, coste_construccion: int, coste_mantenimiento: int ,impacto_felicidad: int):
        """Asigna atributos al objeto.

        Parameters
        ----------
        capacidad : int
            Capacidad máxima de la vivienda.
        num_hogares : int
            Número inicial de hogares.
        nombre : str
            Nombre del edificio.
        coste_construccion : int
            Coste de construcción del edificio.
        coste_mantenimiento : int
            Coste de mantenimiento del edificio.
        impacto_felicidad : int
            Impacto en la felicidad de la población.

        Returns
        -------
        None.
        """
        
        super().__init__(nombre, coste_construccion, coste_mantenimiento ,impacto_felicidad)
        self._capacidad = capacidad
        self._num_hogares = num_hogares
        self._PRECIO_ALQUILER = 300
        
    def calcular_ingresos(self):
        """Calcula los ingresos generados por la vivienda.

        Returns
        -------
        int
        Ingresos totales generados (num_hogares * precio del alquiler).
        """
    
        return self._num_hogares * self._PRECIO_ALQUILER
    
    def obtener_capacidad_disponible(self):
        """Devuelve la capacidad disponible de la vivienda.

        Returns
        -------
        int
        Siempre devuelve 0 para viviendas.
        """
        return 0
    
    def __str__(self):
        """Devuelve toda la informacion sobre la vivienda
        
        Returns
        -------
        str
        Informacion completa sobre la vivienda
        """
        return(f"{super().obtener_informacion()}\n"
               f"Capacidad: {self._capacidad}\n"
               f"Nº de hogares: {self._num_hogares}\n"
               f"Precio alquiler: {self._PRECIO_ALQUILER}")
        
    
    @property
    def capacidad(self):
        return self._capacidad
    @capacidad.setter
    def capacidad(self,capacidad):
        self._capacidad = capacidad

    @property
    def num_hogares(self):
        return self._num_hogares
    @num_hogares.setter
    def num_hogares(self, num_hogares):
        self._num_hogares = num_hogares