from edificios import Edificio

class Equipamiento(Edificio):
    """Representa un edificio de tipo equipamiento.

    Esta clase modela edificios como parques, polideportivos u otros servicios
    que tienen un tipo específico y una capacidad de uso determinada. No generan
    ingresos económicos directos, pero aportan beneficios a la población.

    Attributes
    ----------
    tipo : str
        Tipo de equipamiento (por ejemplo: deportivo, cultural, recreativo).
    capacidad_uso : int
        Capacidad máxima de uso del equipamiento.

    Methods
    -------
    calcular_ingresos()
        Devuelve 0, ya que los equipamientos no generan ingresos.
    obtener_capacidad_disponible()
        Devuelve la capacidad de uso del equipamiento.
    """
    def __init__(self, tipo: str, capacidad_uso: int, nombre: str, coste_construccion: int, coste_mantenimiento: int ,impacto_felicidad: int):
        """Asigna atributos al objeto.

        Parameters
        ----------
        tipo : str
            Tipo de equipamiento.
        capacidad_uso : int
            Capacidad máxima de uso.
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
        super().__init__(nombre, coste_construccion, coste_mantenimiento, impacto_felicidad)
        self._tipo = tipo
        self._capacidad_uso = capacidad_uso
        
    def calcular_ingresos(self):
        """Calcula los ingresos generados por el equipamiento.

        Returns
        -------
        int
        Siempre devuelve 0, ya que los equipamientos no generan ingresos.
        """
        return 0
         
    def obtener_capacidad_disponible(self):
        """Devuelve la capacidad disponible del equipamiento.

        Returns
        -------
        int
        Capacidad de uso del equipamiento.
        """
        return self._capacidad_uso
    
    def __str__(self):
        """Devuelve toda la informacion sobre el equipamiento.

        Returns
        -------
        str
        Información completa del equipamiento.
        """
        return (f"{super().obtener_informacion()}\n"
                f"Tipo de equipamiento: {self.tipo}\n"
                f"Capacidad máxima de uso: {self.capacidad_uso}\n")
    
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,tipo):
        self._tipo = tipo
    
    @property
    def capacidad_uso(self): 
        return self._capacidad_uso 
    @capacidad_uso.setter
    def capacidad_uso(self,capacidad_uso): 
        self._capacidad_uso = capacidad_uso