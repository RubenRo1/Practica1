from abc import ABC, abstractmethod

class Edificio(ABC):
    def __init__(self,nombre, coste_construccion, coste_mantenimiento ,impacto_felicidad):
        
        self.nombre = nombre
        self.coste_construccion = coste_construccion
        self.coste_mantenimiento = coste_mantenimiento
        self.impacto_felicidad = impacto_felicidad
        
    def obtener_informacion(self):
        
        return (
            f"Nombre: {self.nombre}\n"
            f"Coste Construcción{self.coste_construccion}\n"
            f"Coste Mantenimiento{self.coste_mantenimiento}\n"
            f"Impacto felicidad{self.impacto_felicidad}"
            )
    
    @abstractmethod
    def calcular_ingresos(self):
        pass
    
    def obtener_capacidad_disponible(self):
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    