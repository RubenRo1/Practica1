from edificios import Edificio

class Equipamiento(Edificio):
    
    def __init__(self, tipo: str, capacidad_uso: int, nombre: str, coste_construccion: int, coste_mantenimiento: int ,impacto_felicidad: int):
        
        super().__init__(nombre, coste_construccion, coste_mantenimiento, impacto_felicidad)
        self.tipo = tipo
        self.capacidad_uso = capacidad_uso
        
    def calcular_ingresos(self):
        return 0
         
    def obtener_capacidad_disponible(self):
        return self.capacidad_uso