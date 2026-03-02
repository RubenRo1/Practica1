from edificios import Edificio
from viviendas import Viviendas
from oficinas import Oficinas
from equipamiento import Equipamiento

class Ciudad:
    
    def __init__(self, nombre:str, habitantes:int, presupuesto:int, felicidad:int, edificios:list):
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
        return False
        
    def actualizar_presupuesto(self):
        
        ingresos = 0
        mantenimiento = 0
        
        for edificio in self.edificios:
            ingresos += edificio.calcular_ingresos()
            mantenimiento += edificio.coste_mantenimiento 
            
        self.presupuesto += ingresos - mantenimiento + self.IMPUESTO_POR_HABITANTE * self.habitantes

    def actualizar_felicidad(self):
        
        if self.habitantes == 0:
            self.felicidad = 50
            return 
        
        felicidad_total = 0
        num_equipamientos = 0
        
        for edificio in self.edificios:
            felicidad_total += edificio.impacto_felicidad
    
        self.felicidad += felicidad_total
        capacidad_vivienda = self.obtener_capacidad_viviendas()
        
        if capacidad_vivienda == 0:
            self.felicidad -= 30
        else:
            ratio = self.habitantes/capacidad_vivienda
            if ratio > 0.85:
                self.felicidad -= 10
            else:
                self.felicidad +=1
                
        for edificio in self.edificios:
            if isinstance(edificio,Equipamiento):
                num_equipamientos +=1
        
        equipamientos_necesarios = self.habitantes / 1007
        
        if num_equipamientos < equipamientos_necesarios:
            self.felicidad -= 1
        else:
            self.felicidad += 1

        self.felicidad = max(0, min(100, self.felicidad))        
    
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

    @property
    def nombre(self):
        return self.nombre
    @nombre.setter
    def nombre(self,nombre):
        self.nombre = nombre

    @property
    def habitantes(self):
        return self.habitantes
    @habitantes.setter
    def habitantes(self,habitantes):
        self.habitantes = habitantes
    
    @property
    def presupuesto(self):
        return self.presupuesto
    @presupuesto.setter
    def presupuesto(self,presupuesto):
        self.presupuesto = presupuesto
        
    @property
    def felicidad(self):
        return self.felicidad
    @felicidad.setter
    def felicidad(self,felicidad):
        self.felicidad = felicidad
    
    @property
    def edificios(self):
        return self.edificios
    @edificios.setter
    def edificios(self,edificios):
        self.edificios = edificios





                 