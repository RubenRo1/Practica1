from abc import ABC, abstractmethod

class Edificio(ABC):
    def __init__(self,nombre: str, coste_construccion: int , coste_mantenimiento: int ,impacto_felicidad : int):
        
        self.nombre = nombre
        self.coste_construccion = coste_construccion
        self.coste_mantenimiento = coste_mantenimiento
        self.impacto_felicidad = impacto_felicidad
        
    def obtener_informacion(self):
        
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
        return self.nombre
    @nombre.setter
    def nombre(self,nombre):
        self.nombre = nombre
    
    @property
    def coste_construccion(self):
        return self.coste_construccion
    @coste_construccion.setter
    def coste_construccion(self,coste_construccion):
        self.coste_construccion = coste_construccion
    
    @property
    def coste_mantenimiento(self):
        return self.coste_mantenimiento
    @coste_mantenimiento.setter
    def set_coste_mantenimiento(self,coste_mantenimiento):
        self.coste_mantenimiento = coste_mantenimiento
        
    @property
    def impacto_felicidad(self):     
        return self.impacto_felicidad
    @impacto_felicidad.setter
    def impacto_felicidad(self,impacto_felicidad):
        self.impacto_felicidad = impacto_felicidad    