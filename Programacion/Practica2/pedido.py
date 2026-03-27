class Pedido:

    def __init__(self, id_pedido:str, id_cliente:str, tipo:str, prioridad: str, duracion_entrega:int): #pensando si poner bool la prioridad
        
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