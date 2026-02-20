from edificios import Edificio

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

