from edificios import Edificio

class Oficinas(Edificio):
    """ Representa un edificio de tipo oficina.
    Attributes
    ----------
    capacidad_oficinas : int
        Capacidad máxima de las oficinas.
    empresas_actuales : int
        Número de empresas actuales.
    alquiler_por_oficina : int
        Precio del alquiler para cada oficina.
    Methods
    -------
    asignar_empresas(cantidad)
        Añade nuevas empresas hasta completar la capacidad disponible.
    eliminar_empresas(cantidad)
        Elimina empresas del edificio.
    obtener_capacidad_disponible()
        Devuelve la capacidad disponible de oficinas.   
    """
    def __init__(self, capacidad_oficinas:int, alquiler_por_oficina:int, nombre:str, coste_construccion:int, coste_mantenimiento:int ,impacto_felicidad:int):
        
        super().__init__(nombre, coste_construccion, coste_mantenimiento, impacto_felicidad)
        self._capacidad_oficinas = capacidad_oficinas
        self._empresas_actuales = 0
        self._alquiler_por_oficina = alquiler_por_oficina
    
    def asignar_empresas(self, cantidad: int) -> int:
        
        empresas_disponibles = self.obtener_capacidad_disponible()
        empresas_añadir = min(cantidad, empresas_disponibles)
        self._empresas_actuales += empresas_añadir
                
        return empresas_añadir
    
    
    def eliminar_empresas(self,cantidad: int) -> int:
            
        empresas_borrar = min(cantidad, self._empresas_actuales)
        self._empresas_actuales -= empresas_borrar
                    
        return empresas_borrar
        
    def __str__(self):
        return self.obtener_informacion()
        
    def calcular_ingresos(self):
        return self._empresas_actuales * self._alquiler_por_oficina
    
    def obtener_capacidad_disponible(self):
        return self._capacidad_oficinas - self._empresas_actuales
    
    @property
    def capacidad_oficinas(self):
       return self._capacidad_oficinas
    @capacidad_oficinas.setter   
    def capacidad_oficinas(self,capacidad_oficinas):
        self._capacidad_oficinas = capacidad_oficinas

    @property
    def empresas_actuales(self):
       return self._empresas_actuales
    @empresas_actuales.setter    
    def empresas_actuales(self,empresas_actuales):
        self._empresas_actuales = empresas_actuales 
    
    @property
    def alquiler_por_oficina(self):
       return self._alquiler_por_oficina
    @alquiler_por_oficina.setter
    def alquiler_por_oficina(self,alquiler_por_oficina):
        self._alquiler_por_oficina = alquiler_por_oficina