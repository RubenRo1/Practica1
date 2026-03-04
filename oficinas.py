from edificios import Edificio

class Oficinas(Edificio):
    """Representa un edificio de tipo oficina.
    
    Esta clase modela un edificio de oficinas que puede albergar varias empresas.
    Permite asignar o eliminar empresas, calcular los ingresos generados por los 
    alquileres y consultar la capacidad disponible de oficinas.
    
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
    calcular_ingresos()
        Calcula los ingresos generados por las oficinas
    obtener_capacidad_disponible()
        Devuelve la capacidad disponible de oficinas.   
    """
    def __init__(self, capacidad_oficinas:int, alquiler_por_oficina:int, nombre:str, coste_construccion:int, coste_mantenimiento:int ,impacto_felicidad:int):
        """Asigna atributos al objeto.

        Parameters
        ----------
        capacidad_oficinas : int
            Capacidad máxima de las oficinas.
        empresas_actuales : int
            Número inicial de empresas.
        alquiler_por_oficina : int
            Precio del alquiler por oficina.
        nombre : str
            Nombre del edificio.
        coste_construccion : int
            Coste de construcción.
        coste_mantenimiento : int
            Coste de mantenimiento.
        impacto_felicidad : int
            Impacto en la felicidad de la población.

        Returns
        -------
        None.
        """
        
        super().__init__(nombre, coste_construccion, coste_mantenimiento, impacto_felicidad)
        self._capacidad_oficinas = capacidad_oficinas
        self._empresas_actuales = 0
        self._alquiler_por_oficina = alquiler_por_oficina
    
    def asignar_empresas(self, cantidad: int) -> int:
        """Añade nuevas empresas hasta completar la capacidad disponible.

        Parameters
        ----------
        cantidad : int
            Número de empresas que se desean añadir.

        Returns
        -------
        int
        Número real de empresas añadidas.
        """
        empresas_disponibles = self.obtener_capacidad_disponible()
        empresas_añadir = min(cantidad, empresas_disponibles)
        self._empresas_actuales += empresas_añadir
                
        return empresas_añadir
    
    
    def eliminar_empresas(self,cantidad: int) -> int:
        """Elimina empresas del edificio.

        Parameters
        ----------
        cantidad : int
            Número de empresas que se desean eliminar.

        Returns
        -------
        int
        Número real de empresas eliminadas.
        """
        empresas_borrar = min(cantidad, self._empresas_actuales)
        self._empresas_actuales -= empresas_borrar
                    
        return empresas_borrar
        
    def calcular_ingresos(self):
        """Calcula los ingresos generados por las oficinas.

        Returns
        -------
        int
        Ingresos totales generados.
        """
        return self._empresas_actuales * self._alquiler_por_oficina
    
    def obtener_capacidad_disponible(self):
        """Devuelve la capacidad disponible de oficinas.

        Returns
        -------
        int
        Número de oficinas libres.
        """
        return self._capacidad_oficinas - self._empresas_actuales
    
    def __str__(self):
        """Devuelve toda la informacion sobre la oficia.

        Returns
        -------
        str
        Información completa de la oficina.
        """
        return (f"{super().obtener_informacion()}\n"
                f"Capacidad de la oficina: {self.capacidad_oficinas}\n"
                f"Empresas actuales en la oficina: {self.empresas_actuales}\n"
                f"Alquiler por oficina: {self.alquiler_por_oficina}\n")
        
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