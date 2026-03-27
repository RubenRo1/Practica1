"""
Autores:
    Iago Núñez Lourés
    Rubén Rodríguez Catrufo
"""

from linked_queue import LinkedQueue
from pedido import Pedido
from exceptions import tipo_invalido, prioridad_invalida

class gestor_pedidos:

    def __init__(self, cola_registro = None, repartidores=2):

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
        """Ejecuta un ciclo completo de simulación."""
        
        eventos = {}
        eventos['pedido_registrado'] = None
        self._t_actual += 1
        #Registramos un nuevo pedido cada 2 ciclos, empezando en el ciclo 1
        if self._t_actual % 2 != 0:
            eventos['pedido_registrado'] = self._registrar_pedido()

        eventos['retraso'] = self._avisar_retrasos_prioritarios()
        eventos['escalado'] = self._escalar_normales()
        
        eventos['pedidos_entregados'] = self._liberar_repartidores()
        eventos['pedidos_entraron_reparto'] = self._asignar_repartos()

        return eventos

    def hay_pedidos_pendientes(self):
        """Devuelve True si aún quedan pedidos por gestionar o repartir."""
        return (
            not self._cola_registro.is_empty()
            or not self._cola_rapida_prioritaria.is_empty()
            or not self._cola_rapida_normal.is_empty()
            or not self._cola_tradicional_prioritaria.is_empty()
            or not self._cola_tradicional_normal.is_empty()
            or len(self._pedidos_en_reparto) > 0
            )

    def resumen_estado(self):
        """Devuelve un resumen del estado actual del sistema."""
        pass

    def anadir_pedido(self, pedido):
        """No es necesario en el ejercicio, peron en una situacion real, entrarian nuevos pedidos a la cola de registro"""
        self._cola_registro.enqueue(pedido)

    def _registrar_pedido(self):
        """Cada 2 unidades, pasa un pedido de la cola de registro a su cola correspondiente."""

        pedido = self._cola_registro.dequeue()
        self._clasificar_pedido(pedido)
        return pedido

    def _avisar_retrasos_prioritarios(self):
        """Comprueba si hay prioritarios esperando más de 5 unidades."""

        return (self._tradicional_prioritaria.first().t_entrada - self._t_actual < 0
                or self._rapida_prioritaria.first().t_entrada - self._t_actual < 0)

    def _escalar_normales(self):
        """Convierte en prioritarios los pedidos normales que superen 8 unidades de espera."""

        if self._rapida_normal.first().t_entrada - self._t_actual > 8:
            self._rapida_prioritaria.enqueue(self._rapida_normal.first())
            return self._rapida_normal.dequeue()
        
        if self._tradicional_normal.first().t_entrada - self._t_actual > 8:
            self._tradicional_prioritaria.enqueue(self._tradicional_normal.first())
            return self._tradicional_normal.dequeue()
        
        return None

    def _liberar_repartidores(self):
        """Comprueba qué pedidos ya han terminado su reparto."""

        pedidos_entregados = []
        for pedido in self._pedidos_en_reparto:
            if pedido.t_inicio_reparto - self._t_actual == pedido.duracion_entrega:
                pedido.t_fin = self._t_actual
                self._pedidos_finalizados.append(pedido)
                self._pedidos_en_reparto.remove(pedido)

                pedidos_entregados.append(pedido)
                self._repartidores_libres += 1

        return pedidos_entregados
            
    def _asignar_repartos(self):
        """Asigna pedidos a repartidores libres respetando prioridad y orden."""
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
        """Obtiene el siguiente pedido a repartir según las reglas de prioridad."""

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


    '''
    Hay que anadir la logica de asignacion de repartidores, reparto y
    entregas de pedido. Tambien el control de los tiempos y de prioridades

    Revisar excepciones y ver si podemos modificar la clase de pedido
    para anadir getters y setters de los tiempos

    Esta clase deberia funcionar como un servicio mas que como un
    objeto instanciable, asique nos toca leer literatura y ver como
    crear una buena estructura para la misma

    Si puedo a la tarde creo un esquema logico para hacernos bien a la idea
    de como implementarlo, pq me esta rayando la cabeza
    '''

    

