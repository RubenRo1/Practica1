from edificios import Edificio

class Viviendas(Edificio):
    """ Representa un edificio de tipo vivienda.
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
        Devuelve la capacidad disponible de la vivienda.     
    """
        
    def __init__(self,capacidad: int, num_hogares: int, nombre : str, coste_construccion: int, coste_mantenimiento: int ,impacto_felicidad: int):
        
        super().__init__(nombre, coste_construccion, coste_mantenimiento ,impacto_felicidad)
        self.capacidad = capacidad
        self.num_hogares = num_hogares
        self._PRECIO_ALQUILER = 300
        
    def calcular_ingresos(self):
        
        return self.num_hogares * Viviendas._PRECIO_ALQUILER
    
    def obtener_capacidad_disponible(self):
        return 0
    
    @property
    def capacidad(self):
        return self.capacidad
    @capacidad.setter
    def capacidad(self,capacidad):
        self.capacidad = capacidad

    @property
    def num_hogares(self):
        return self.num_hogares
    @num_hogares.setter
    def num_hogares(self, num_hogares):
        self.num_hogares = num_hogares