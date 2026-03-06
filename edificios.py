from abc import ABC, abstractmethod

class Edificio(ABC):   
    """Clase abstracta que define los distintos tipos de edificio.

     Esta clase sirve como base para todos los edificios dentro del sistema.
     Proporciona los atributos comunes a todos los edificios y define métodos 
     abstractos que deben ser implementados por cada tipo de edificio específico.
     
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

        Returns
        -------
        str
        Información completa del edificio.
        """
        return (
            f"Nombre: {self._nombre}\n"
            f"Coste Construcción: {self._coste_construccion}\n"
            f"Coste Mantenimiento: {self._coste_mantenimiento}\n"
            f"Impacto felicidad: {self._impacto_felicidad}"
            )
    
    def __str__(self):
        """Devuelve toda la informacion sobre el edificio
        
        Returns
        -------
        str
        Informacion completa sobre el edificio
        """
        return(f"{self.obtener_informacion()}")
    
    @abstractmethod
    def calcular_ingresos(self):
        """Calcula los ingresos generados por el edificio. Debe implementarse en la subclase."""
        pass
    
    @abstractmethod
    def obtener_capacidad_disponible(self):
        """Devuelve la capacidad disponible del edificio. Debe implementarse en la subclase."""
        pass
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        if nombre == ''or not isinstance(nombre, str):
            raise ValueError
        self._nombre = nombre
    
    @property
    def coste_construccion(self):
        return self._coste_construccion
    @coste_construccion.setter
    def coste_construccion(self,coste_construccion):
        if coste_construccion < 0:
            raise ValueError
        self._coste_construccion = coste_construccion
    
    @property
    def coste_mantenimiento(self):
        return self._coste_mantenimiento
    @coste_mantenimiento.setter
    def set_coste_mantenimiento(self,coste_mantenimiento):
        if coste_mantenimiento < 0:
            raise ValueError
        self._coste_mantenimiento = coste_mantenimiento
        
    @property
    def impacto_felicidad(self):     
        return self._impacto_felicidad
    @impacto_felicidad.setter
    def impacto_felicidad(self,impacto_felicidad):
        if impacto_felicidad < 0:
            raise ValueError
        self._impacto_felicidad = impacto_felicidad    