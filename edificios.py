from abc import ABC, abstractmethod

class Edificio(ABC):   
    """Clase abstracta que define los distintos tipos de edificio.

     Esta clase sirve como base para todos los edificios dentro del sistema.
     Proporciona los atributos comunes a todos los edificios y define métodos 
     abstractos que deben serimplementados por cada tipo de edificio específico.
     
    Attributes
    ----------
    nombre : str
        Nombre del edificio.
    coste_construccion : int
        Coste de construcción.
    coste_mantenimiento : int
        Coste de mantenimiento.
    impacto_felicidad : int
        Impacto en la felicidad de la población.
        
    Methods
    -------
    obtener_informacion()
        Devuelve toda la información del edificio.
    calcular_ingresos()
        Calcula los ingresos generados por el edificio.
    obtener_capacidad_disponible()
        Devuelve la capacidad disponible del edificio.
    """
    def __init__(self,nombre: str, coste_construccion: int , coste_mantenimiento: int ,impacto_felicidad : int):
        """
        Asigna atributos al objeto.

        Parameters
        ----------
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
        
        self._nombre = nombre
        self._coste_construccion = coste_construccion
        self._coste_mantenimiento = coste_mantenimiento
        self._impacto_felicidad = impacto_felicidad
            
    def obtener_informacion(self):
        """
        Devuelve toda la información del edificio.

        Parameters
        ----------
        None.

        Returns
        -------
        str
        Información completa del edificio.
        """
        return (
            f"Nombre: {self.nombre}\n"
            f"Coste Construcción: {self.coste_construccion}\n"
            f"Coste Mantenimiento: {self.coste_mantenimiento}\n"
            f"Impacto felicidad: {self.impacto_felicidad}"
            )
    
    @abstractmethod
    def calcular_ingresos(self):
        pass
    
    @abstractmethod
    def obtener_capacidad_disponible(self):
        pass
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    
    @property
    def coste_construccion(self):
        return self._coste_construccion
    @coste_construccion.setter
    def coste_construccion(self,coste_construccion):
        self._coste_construccion = coste_construccion
    
    @property
    def coste_mantenimiento(self):
        return self._coste_mantenimiento
    @coste_mantenimiento.setter
    def set_coste_mantenimiento(self,coste_mantenimiento):
        self._coste_mantenimiento = coste_mantenimiento
        
    @property
    def impacto_felicidad(self):     
        return self._impacto_felicidad
    @impacto_felicidad.setter
    def impacto_felicidad(self,impacto_felicidad):
        self._impacto_felicidad = impacto_felicidad    