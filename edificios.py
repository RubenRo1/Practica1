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
    
    
class Viviendas(Edificio):
    
        
    def __init__(self,capacidad,num_hogares, nombre, coste_construccion, coste_mantenimiento ,impacto_felicidad):
        
        super().__init__(nombre, coste_construccion, coste_mantenimiento ,impacto_felicidad)
        self.capacidad = capacidad
        self.num_hogares = num_hogares
        self._PRECIO_ALQUILER = 300
        
    def calcular_ingresos(self):
        
        return self.num_hogares * Viviendas._PRECIO_ALQUILER
    
    def obtener_capacidad_disponible(self):
        return 0
    
class Oficinas(Edificio):
    def __init__(self, capacidad_oficinas, empresas_actuales, alquiler_por_oficina, nombre, coste_construccion, coste_mantenimiento ,impacto_felicidad):
        
        super().__init__(nombre, coste_construccion, coste_mantenimiento, impacto_felicidad)
        self.capacidad_oficinas = capacidad_oficinas
        self.empresas_actuales = 0
        self.alquiler_por_oficina = alquiler_por_oficina
    
    def asignar_empresas(self, cantidad):
        return 0
    
    def eliminar_empresas(self,cantidad):
        return 0
    
    def calcular_ingresos(self):
        
        return self.empresas_actuales * self.alquiler_por_oficina
    
    def obtener_capacidad_disponible(self):
        return self.capacidad_oficinas - self.empresas_actuales
    
class Equipamiento(Edificio):
    
    def __init__(self, tipo, capacidad_uso, nombre, coste_construccion, coste_mantenimiento ,impacto_felicidad):
        
        super().__init__(nombre, coste_construccion, coste_mantenimiento, impacto_felicidad)
        self.tipo = tipo
        self,capacidad_uso = capacidad_uso
        
    def calcular_ingresos(self):
        
        return 0
         
    def obtener_capacidad_disponible(self):
        
        return self.capacidad_uso
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    