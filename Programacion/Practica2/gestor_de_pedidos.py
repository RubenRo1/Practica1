"""
Autores:
    Iago Núñez Lourés
    Rubén Rodríguez Catrufo
"""

from linked_queue import LinkedQueue
from pedido import Pedido

class gestor_pedidos:

    def __init__(self, repartidores=2):

        self._pedidos = LinkedQueue()
        self._contador = 0
        self._repartidores = repartidores

        self._rapida_prioritaria = LinkedQueue()
        self._rapida_normal = LinkedQueue()
        self._tradicional_prioritaria = LinkedQueue()
        self._tradicional_normal = LinkedQueue()

        #Los vamos acumulando para poder sacar estadisticas
        self._pedidos_finalizados = []

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
                #crear excepcion si no existe ese tipo
                pass
        

    def anadir_pedido(self, pedido:Pedido):
        #Primero clasificamos en caso de que el pedido sea invalido
        self._clasificar_pedido(pedido)
        #Anadir tiempos de entrada, hay que tocar Pedido
        self._pedidos.enqueue(pedido)

    def avanzar_tiempo(self):
        pass

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

    

