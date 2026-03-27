"""
Autores:
    Iago Núñez Lourés
    Rubén Rodríguez Catrufo
"""

"""
ANADIR GETTERS DE LOS DATOS NECESARIOS
"""

from linked_queue import LinkedQueue
from pedido import Pedido
from exceptions import tipo_invalido, prioridad_invalida

class gestor_pedidos:
    """Administra las cuatro colas de pedidos y asigna los pedidos al reparto .

    Esta clase controla el ciclo de vida de los pedidos desde su registro, 
    clasificación por tipo y prioridad, gestión de esperas (escalado y avisos) 
    hasta la asignación de repartidores libres.

    Attributes
    ----------
    _cola_registro : LinkedQueue
        Cola de espera donde aguardan los pedidos antes de ser procesados.
    _repartidores_max : int
        Número total de repartidores contratados en el sistema.
    _repartidores_libres : int
        Número de repartidores que no están realizando una entrega actualmente.
    _t_actual : int
        Contador de unidades de tiempo transcurridas en la simulación.
    _rapida_prioritaria : LinkedQueue
        Cola de pedidos rápidos con alta prioridad.
    _rapida_normal : LinkedQueue
        Cola de pedidos rápidos con prioridad normal.
    _tradicional_prioritaria : LinkedQueue
        Cola de pedidos tradicionales con alta prioridad.
    _tradicional_normal : LinkedQueue
        Cola de pedidos tradicionales con prioridad normal.
    _pedidos_en_reparto : list
        Lista de objetos Pedido que están actualmente en tránsito.
    _pedidos_finalizados : list
        Historial de todos los pedidos cuya entrega se ha completado.

    Methods
    -------
    avanzar_tiempo():
        Ejecuta un ciclo completo de simulación y devuelve los eventos ocurridos
    hay_pedidos_pendientes():
        Indica si quedan pedidos por gestionar o repartir.
    anadir_pedido(pedido):
        Añade un pedido en la cola de registro
    _registrar_pedido():
        Cada 2 unidades, pasa un pedido de la cola de registro a su cola correspondiente.
    _avisar_retrasos_prioritarios():
        Identifica pedidos prioritarios que superan el tiempo de espera.
    _escalar_normales():
        Cambia pedidos de prioridad normal a prioritaria por tiempo.
    _liberar_repartidores():
        Finaliza las entregas y libera a los repartidores correspondientes.
    _asignar_repartos():
        Asocia pedidos pendientes a los repartidores que están libres.
    _siguiente_pedido():
        Selecciona el próximo pedido a repartir según la jerarquía de colas.
    _clasificar_pedido(pedido):
        Ubica un pedido en su cola específica según tipo y prioridad.
    
    """
    def __init__(self, cola_registro = None, repartidores=2):
        """Inicializa el gestor con colas vacias y los repartidores ya definidos.

        Parameters
        ----------
        cola_registro : LinkedQueue
            Cola inicial de pedidos. Si es None, se crea una vacia.
        repartidores : int
            Numero de repartidores (por defecto 2).

        Returns
        -------
        None.
        """
        self._cola_registro = cola_registro if cola_registro != None else LinkedQueue()

        self._repartidores_max = repartidores
        self._repartidores_libres = repartidores
        self._t_actual = 0

        self._rapida_prioritaria = LinkedQueue()
        self._rapida_normal = LinkedQueue()
        self._tradicional_prioritaria = LinkedQueue()
        self._tradicional_normal = LinkedQueue()

        #Los vamos acumulando para poder sacar estadisticas
        self._pedidos_en_reparto = []
        self._pedidos_finalizados = []

    def avanzar_tiempo(self):
        """Ejecuta un ciclo completo de simulación actualizando todos los estados.
        
        Incrementa el tiempo, registra pedidos, comprueba retrasos, escala prioridades
        y gestiona la logica de reparto.
        
        Returns
        -------
        dict
            Diccionario con los eventos sucedidos en este ciclo (registros, 
            retrasos, escalados, entregas y nuevos repartos).
        """

        eventos = {}
        self._t_actual += 1
        eventos['tiempo_actual'] = self._t_actual
        eventos['pedido_registrado'] = None
        #Registramos un nuevo pedido cada 2 ciclos, empezando en el ciclo 1
        if self._t_actual % 2 != 0:
            eventos['pedido_registrado'] = self._registrar_pedido()

        eventos['retrasados'] = self._avisar_retrasos_prioritarios()
        eventos['escalados'] = self._escalar_normales()
        
        eventos['pedidos_entregados'] = self._liberar_repartidores()
        eventos['pedidos_entraron_reparto'] = self._asignar_repartos()

        return eventos

    def hay_pedidos_pendientes(self):
        """Comprueba si el sistema tiene trabajo pendiente en alguna de sus áreas.

        Returns
        -------
        bool
            True si hay pedidos en registro, colas de trabajo o en reparto.
        """
        return (
            not self._cola_registro.is_empty()
            or not self._rapida_prioritaria.is_empty()
            or not self._rapida_normal.is_empty()
            or not self._tradicional_prioritaria.is_empty()
            or not self._tradicional_normal.is_empty()
            or len(self._pedidos_en_reparto) > 0
            )

    def anadir_pedido(self, pedido):
        """Añade un nuevo pedido a la cola de registro
        
        Parameters
        ----------
        pedido : Pedido
            El objeto pedido que entra al sistema.

        Returns
        -------
        None.
        """
        self._cola_registro.enqueue(pedido)

    def _registrar_pedido(self):
        """Procesa un pedido de la cola de registro y lo clasifica
        
        Returns
        -------
        Pedido or None
            El pedido procesado, None si la cola estaba vacía.
        """

        #Comprobamos si queda algo en la cola de registro
        if self._cola_registro.is_empty():
            return None

        pedido = self._cola_registro.dequeue()
        pedido.t_entrada = self._t_actual
        self._clasificar_pedido(pedido)
        return pedido

    def _avisar_retrasos_prioritarios(self):
        """Identidica los pedidos prioritarios que llevan más de 5 unidades esperando.

        Returns
        -------
        list
            Lista de objetos Pedido en el frente de las colas prioritarias 
            que presentan retraso.
        """
        retrasados = []
        #Comprobamos que las colas no esten vacias antes de acceder a ellas
        if (not self._rapida_prioritaria.is_empty() and
            self._t_actual - self._rapida_prioritaria.first().t_entrada > 5):
            retrasados.append(self._rapida_prioritaria.first())

        if (not self._tradicional_prioritaria.is_empty() and
            self._t_actual - self._tradicional_prioritaria.first().t_entrada > 5):
            retrasados.append(self._tradicional_prioritaria.first())

        return retrasados

    def _escalar_normales(self):
        """Convierte pedidos normales a prioritarios tras 8 unidades de espera.

        Returns
        -------
        list
            Lista de pedidos que han sido escalados en este ciclo.
        """

        escalados = []
        #Comprobamos primero si estan vacias y luego si el primero va con retraso
        if (not self._tradicional_normal.is_empty() 
            and self._t_actual - self._rapida_normal.first().t_entrada > 8):
            pedido = self._rapida_normal.dequeue()
            pedido.prioridad = 'prioritario'
            self._rapida_prioritaria.enqueue(pedido)
            escalados.append(pedido)
        
        if (not self._tradicional_normal.is_empty() 
            and self._t_actual - self._tradicional_normal.first().t_entrada > 8):
            pedido = self._tradicional_normal.dequeue()
            pedido.prioridad = 'prioritario'
            self._tradicional_prioritaria.enqueue(pedido)
            escalados.append(pedido)
        
        return escalados

    def _liberar_repartidores(self):
        """Comprueba qué pedidos ya han terminado su reparto.
        
        Returns
        -------
        list
            Pedidos cuya entrega se ha completado en este instante.
        """

        pedidos_entregados = []
        #Recorremos una copia de la lista para no editarla y recorrela a la vez
        for pedido in self._pedidos_en_reparto[:]:
            if  self._t_actual - pedido.t_inicio_reparto == pedido.duracion_entrega:
                pedido.t_fin = self._t_actual
                self._pedidos_finalizados.append(pedido)
                self._pedidos_en_reparto.remove(pedido)

                pedidos_entregados.append(pedido)
                self._repartidores_libres += 1

        return pedidos_entregados
            
    def _asignar_repartos(self):
        """Asigna pedidos a repartidores libres respetando prioridad y orden.
        
        Returns
        -------
        list
            Pedidos que han iniciado su reparto en este ciclo.
        """
        
        #Lista con los pedidos que han entrado en reparto
        pedidos = []
        while self._repartidores_libres > 0:
            pedido = self._siguiente_pedido()
            #Puede ser que haya repartidores pero no pedidos a repartir
            if pedido == None:
                break
            
            pedido.t_inicio_reparto = self._t_actual
            self._pedidos_en_reparto.append(pedido)
            self._repartidores_libres -= 1
            pedidos.append(pedido)

        return pedidos
        
    def _siguiente_pedido(self):
        """Selecciona el pedido con mayor prioridad según el orden jerárquico.

        Jerarquía: Rápida Prio > Tradicional Prio > Rápida Normal > Tradicional Normal.

        Returns
        -------
        Pedido or None
            El siguiente pedido en la jerarquía, None si no hay pendientes.
        """

        #Realizamos los checks siguiendo la prioridad, 
        # y en caso de que no haya pedidos pendientes, devolvemos None

        if not self._rapida_prioritaria.is_empty():
            return self._rapida_prioritaria.dequeue()
        if not self._tradicional_prioritaria.is_empty():
            return self._tradicional_prioritaria.dequeue()
        if not self._rapida_normal.is_empty():
            return self._rapida_normal.dequeue()
        if not self._tradicional_normal.is_empty():
            return self._tradicional_normal.dequeue()
        
        return None

    def _clasificar_pedido(self, pedido:Pedido):
        """Añade un pedido en su cola específica según tipo y prioridad.

        Parameters
        ----------
        pedido : Pedido
            El objeto pedido a clasificar.

        Returns
        -------
        None.
        """
        match pedido.tipo, pedido.prioridad:
            case 'rapida', 'prioritario':
                self._rapida_prioritaria.enqueue(pedido)
            case 'rapida', 'normal':
                self._rapida_normal.enqueue(pedido)
            case 'tradicional', 'prioritario':
                self._tradicional_prioritaria.enqueue(pedido)
            case 'tradicional', 'normal':
                self._tradicional_normal.enqueue(pedido)
            case _:
                if pedido.tipo not in ['rapida', 'tradicional']:
                    raise tipo_invalido
                raise prioridad_invalida

    @property
    def pedidos_finalizados(self):
        return self._pedidos_finalizados