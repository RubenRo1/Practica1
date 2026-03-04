from edificios import Edificio
from viviendas import Viviendas
from oficinas import Oficinas
from equipamiento import Equipamiento

class Ciudad:
    """Representa una ciudad que contiene edificios, habitantes y presupuesto.

    Esta clase gestiona la construcción de edificios, la actualización del
    presupuesto y la felicidad de la población, así como el cálculo de
    capacidades de viviendas y oficinas, y el número de empresas presentes.

    Attributes
    ----------
    nombre : str
        Nombre de la ciudad.
    habitantes : int
        Número de habitantes de la ciudad.
    presupuesto : int
        Presupuesto disponible de la ciudad.
    felicidad : int
        Nivel de felicidad de la población (0-100).
    edificios : list
        Lista de edificios presentes en la ciudad.
    _IMPUESTO_POR_HABITANTE : int
        Cantidad fija de ingresos por habitante.
        
    Methods
    -------
    construir_edificio(edificio)
        Construye un edificio si hay presupuesto suficiente.
    actualizar_presupuesto()
        Actualiza el presupuesto sumando ingresos, impuestos y restando mantenimiento.
    actualizar_felicidad()
        Calcula y actualiza la felicidad de la población según distintos factores.
    obtener_capacidad_viviendas()
        Devuelve la capacidad total de todas las viviendas.
    obtener_capacidad_oficinas()
        Devuelve la capacidad total de todas las oficinas.
    obtener_empresas_actuales()
        Devuelve el número total de empresas en todas las oficinas.
    """
    
    def __init__(self, nombre:str, habitantes:int, presupuesto:int, felicidad:int, edificios:list):
        
        """Inicializa los atributos de la ciudad.

        Parameters
        ----------
        nombre : str
            Nombre de la ciudad.
        habitantes : int
            Número de habitantes.
        presupuesto : int
            Presupuesto inicial.
        felicidad : int
            Nivel inicial de felicidad (0-100).
        edificios : list
            Lista inicial de edificios.

        Returns
        -------
        None.
        """
        self._nombre = nombre
        self._habitantes = habitantes
        self._presupuesto = presupuesto
        self._felicidad = max(0, min(100,felicidad))
        self._edificios = edificios
        self._IMPUESTO_POR_HABITANTE = 500

    def construir_edificio(self,edificio: Edificio) -> bool:
        """Construye un edificio si hay presupuesto suficiente.

        Parameters
        ----------
        edificio : Edificio
            Objeto de tipo Edificio a construir.

        Returns
        -------
        bool
        True si se construyó el edificio, False si no hay presupuesto suficiente.
        """
        
        if self._presupuesto > edificio.coste_construccion:
            self._edificios.append(edificio)
            self._presupuesto -= edificio.coste_construccion
            return True
        return False
        
    def actualizar_presupuesto(self):
        """Actualiza el presupuesto de la ciudad.

        Suma los ingresos de todos los edificios, resta el coste de mantenimiento,
        y añade los ingresos provenientes de impuestos por habitante.
        
        Returns
        -------
        None
        """

        ingresos = 0
        mantenimiento = 0
        
        for edificio in self._edificios:
            ingresos += edificio.calcular_ingresos()
            mantenimiento += edificio.coste_mantenimiento 
            
        self.presupuesto += ingresos - mantenimiento + self._IMPUESTO_POR_HABITANTE * self._habitantes

    def actualizar_felicidad(self):
        """Calcula y actualiza la felicidad de la población.

        Factores considerados:
        - Impacto de todos los edificios.
        - Ratio habitantes/capacidad de viviendas.
        - Número de equipamientos en relación a los habitantes.
        Returns
        -------
        None
        """
        
        if self._habitantes == 0:
            self._felicidad = 50
            return 
        
        felicidad_total = 0
        num_equipamientos = 0
        
        for edificio in self._edificios:
            felicidad_total += edificio.impacto_felicidad
    
        self._felicidad += felicidad_total
        capacidad_vivienda = self.obtener_capacidad_viviendas()
        
        if capacidad_vivienda == 0:
            self._felicidad -= 30
        else:
            ratio = self._habitantes/capacidad_vivienda
            if ratio > 0.85:
                self._felicidad -= 10
            else:
                self._felicidad +=1
                
        for edificio in self._edificios:
            if isinstance(edificio,Equipamiento):
                num_equipamientos +=1
        
        equipamientos_necesarios = self._habitantes / 1007
        
        if num_equipamientos < equipamientos_necesarios:
            self._felicidad -= 1
        else:
            self._felicidad += 1

        self._felicidad = max(0, min(100, self._felicidad))        
    
    def obtener_capacidad_viviendas(self) -> int:
        """Devuelve la capacidad total de todas las viviendas de la ciudad.

        Returns
        -------
        int
        Capacidad total de todas las viviendas.
        """
        capacidad_total = 0
        for edificio in self._edificios:
            if isinstance(edificio, Viviendas):
                capacidad_total += edificio.capacidad
            
        return capacidad_total
        
    def obtener_capacidad_oficinas(self) -> int:
        """Devuelve la capacidad total de todas las oficinas de la ciudad.

        Returns
        -------
        int
        Capacidad total de oficinas.
        """
        capacidad_total = 0
        for edificio in self._edificios:
            if isinstance(edificio, Oficinas):
                capacidad_total += edificio.capacidad_oficinas
        
        return capacidad_total
        
    def obtener_empresas_actuales(self) -> int:
        """Devuelve el número total de empresas en todas las oficinas.

        Returns
        -------
        int
        Número total de empresas.
        """
        empresas = 0
        for edificio in self._edificios:
            if isinstance(edificio, Oficinas):
                empresas += edificio.empresas_actuales
                
        return empresas
    
    def __str__(self):
        """Devuelve toda la informacion sobre la ciudad
        
        Returns
        -------
        str
        Informacion completa sobre la ciudad
        """
        edificios_info = "\n".join([edificio.nombre for edificio in self.edificios])
            
        return (
        f"Ciudad: {self._nombre}\n"
        f"Habitantes: {self._habitantes}\n"
        f"Presupuesto: {self._presupuesto}\n"
        f"Felicidad: {self._felicidad}\n"
        f"Edificios:\n{edificios_info}"
    )

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def habitantes(self):
        return self._habitantes
    @habitantes.setter
    def habitantes(self,habitantes):
        self._habitantes = habitantes
    
    @property
    def presupuesto(self):
        return self._presupuesto
    @presupuesto.setter
    def presupuesto(self,presupuesto):
        self._presupuesto = presupuesto
        
    @property
    def felicidad(self):
        return self._felicidad
    @felicidad.setter
    def felicidad(self,felicidad):
        self._felicidad = felicidad
    
    @property
    def edificios(self):
        return self._edificios
    @edificios.setter
    def edificios(self,edificios):
        self._edificios = edificios





                 