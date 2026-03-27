"""
Autores:
    Iago Núñez Lourés - iago.nunez.loures@udc.es
    Rubén Rodríguez Catrufo - ruben.rodriguez.catrufo@udc.es
"""
class Pedido:
    """Representa un pedido en el sistema de reparto
    
    Esta clase almacena la informacion del cliente, el tipo de comida,
    la prioridad y realiza el seguimiento de los tiempos clave durante
    el ciclo de vida del pedido.

    Attributes
    ----------
    _id_pedido : str
        Identificador único del pedido.
    _id_cliente : str
        Identificador único del cliente que realiza el pedido.
    _tipo : str
        Categoría de la comida (ej. 'rapida' o 'tradicional').
    _prioridad : str
        Nivel de urgencia del pedido (ej. 'normal' o 'prioritario').
    _duracion_entrega : int
        Tiempo estimado que tarda el repartidor en entregar el pedido.
    _t_entrada : int or None
        Instante de tiempo en el que el pedido entra al sistema.
    _t_inicio_reparto : int or None
        Instante de tiempo en el que un repartidor toma el pedido.
    _t_fin : int or None
        Instante de tiempo en el que el pedido se considera entregado.
    """

    def __init__(self, id_pedido:str, id_cliente:str, tipo:str, prioridad: str, duracion_entrega:int): #pensando si poner bool la prioridad
        """Asigna atributos al objeto Pedido
        Parameters
        ----------
        id_pedido : str
            Identificador único del pedido.
        id_cliente : str
            Identificador del cliente.
        tipo : str
            Tipo de comida.
        prioridad : str
            Prioridad inicial del pedido.
        duracion_entrega : int
            Tiempo que durará el trayecto de reparto.

        Returns
        -------
        None.
        """
        self._id_pedido = id_pedido
        self._id_cliente = id_cliente
        self._tipo = tipo
        self._prioridad = prioridad
        
        self._duracion_entrega = duracion_entrega 

        self._t_entrada = None
        self._t_inicio_reparto = None
        self._t_fin = None #Tiempo de inicio del reparto + duracion_entrega, para considerar q el pedido fue enviado


    @property
    def id_pedido(self):
        return self._id_pedido
    @id_pedido.setter
    def id_pedido(self, id_pedido):
        self._id_pedido = id_pedido

    @property
    def id_cliente(self):
        return self._id_cliente
    @id_cliente.setter
    def id_cliente(self,id_cliente):
        self._id_cliente = id_cliente
    
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def prioridad(self):
        return self._prioridad
    @prioridad.setter
    def prioridad(self, prioridad):
        self._prioridad = prioridad

    @property
    def duracion_entrega(self):
        return self._duracion_entrega
    @duracion_entrega.setter
    def duracion_entrega(self,duracion_entrega):
        self._duracion_entrega = duracion_entrega

    @property
    def t_entrada(self):
        return self._t_entrada
    @t_entrada.setter
    def t_entrada(self, t_entrada):
        self._t_entrada = t_entrada

    @property
    def t_inicio_reparto(self):
        return self._t_inicio_reparto
    @t_inicio_reparto.setter
    def t_inicio_reparto(self, t_inicio_reparto):
        self._t_inicio_reparto = t_inicio_reparto

    @property
    def t_fin(self):
        return self._t_fin
    @t_fin.setter
    def t_fin(self, t_fin):
        self._t_fin = t_fin