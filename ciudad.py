from edificios import Edificio

class Ciudad:
    def __init__(self, nombre : str, habitantes : int, presupuesto : int, felicidad : int, edificios : list):
        
        self.nombre = nombre
        self.habitantes = habitantes
        self.presupuesto = presupuesto
        self.felicidad = max(0, min(100,felicidad))
        self.edificios = edificios
        self._IMPUESTO_POR_HABITANTE = 500

    def construir_edificio(self,edificio: Edificio) -> bool:
        
        if self.presupuesto > edificio.coste_construccion:
            
            self.edificios.append(edificio)
            
            self.presupuesto -= edificio.coste_construccion
            
            return True
        
        else:
            
            return False
        
    def actualizar_presupuesto(self):
        
        ingreso = 0
        mantenimiento = 0
        
        for edificio in self.edificios:
            ingreso += edificio.calcular_ingresos()
            mantenimiento += edificio.coste_mantenimiento 
            
        self.presupuesto += (ingreso - mantenimiento) + self.IMPUESTO_POR_HABITANTE
        
    def actualizar_felicidad():
        return 0
        
    def obtener_capacidad_viviendas():
        return 0
        
    def obtener_capacidad_oficinas():
        return 0
        
    def obtener_empresas_actuales():
        return 0
                 