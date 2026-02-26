from edificios import Edificio

class Oficinas(Edificio):
    def __init__(self, capacidad_oficinas:int, empresas_actuales:int, alquiler_por_oficina:int, nombre:str, coste_construccion:int, coste_mantenimiento:int ,impacto_felicidad:int):
        
        super().__init__(nombre, coste_construccion, coste_mantenimiento, impacto_felicidad)
        self.capacidad_oficinas = capacidad_oficinas
        self.empresas_actuales = 0
        self.alquiler_por_oficina = alquiler_por_oficina
    
    def asignar_empresas(self, cantidad: int) -> int:
        
        empresas_disponibles = self.obtener_capacidad_disponible()
        empresas_añadir = min(cantidad, empresas_disponibles)
        self.empresas_actuales += empresas_añadir
                
        return empresas_añadir
    
    
    def eliminar_empresas(self,cantidad: int) -> int:
            
        empresas_borrar = min(cantidad, self.empresas_actuales)
        self.empresas_actuales -= empresas_borrar
                    
        return empresas_borrar
        
    
    def calcular_ingresos(self):
        return self.empresas_actuales * self.alquiler_por_oficina
    
    def obtener_capacidad_disponible(self):
        return self.capacidad_oficinas - self.empresas_actuales