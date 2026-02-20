from edificios import Edificio
from viviendas import Viviendas
from oficinas import Oficinas
from equipamiento import Equipamientos

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
        
    def actualizar_felicidad(self):
        
        felicidad_total = 0
        
        for edificio in self.edificios:
            
            felicidad_total += edificio.impacto_felicidad
    
        self.felicidad += felicidad_total
        
        capacidad_vivienda = self.obtener_capacidad_viviendas()
        
        ratio = self.habitantes/capacidad_vivienda
        
        if capacidad_vivienda == 0:
            
            self.felicidad -= 30
        
        else:
        
            if ratio > 0.85:
                
                self.felicidad -= 10
            
            else:
                
                self.felicidad +=1
                
        for edificio in self.edificios:
            if isinstance(edificio,Equipamiento):
                
    
        
    def obtener_capacidad_viviendas(self) -> int:
   
        capacidad_total = 0
        
        for edificio in self.edificios:
            
            if isinstance(edificio, Viviendas):
               
                capacidad_total += edificio.capacidad
           
            
        return capacidad_total
        
    def obtener_capacidad_oficinas(self) -> int:
        
        capacidad_total = 0
        
        for edificio in self.edificios:
            
            if isinstance(edificio, Oficinas):
                
                capacidad_total += edificio.capacidad_oficinas
        
        return capacidad_total
        
        
    def obtener_empresas_actuales(self) -> int:
        
        empresas = 0
        
        for edificio in self.edificios:
            
            if isinstance(edificio, Oficinas):
                
                empresas += edificio.empresas_actuales
                
        return empresas
                 