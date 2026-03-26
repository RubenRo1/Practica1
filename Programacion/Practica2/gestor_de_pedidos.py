"""
Autores:
    Iago Núñez Lourés
    Rubén Rodríguez Catrufo
"""

from linked_queue import LinkedQueue
from pedido import Pedido

class gestor_pedidos:

    def __init__(self, repartidores=2):

        self._cola_registro = LinkedQueue()

        self._pedidos = LinkedQueue()
        self._contador = 0
        self._repartidores = repartidores
        self._t_actual = 0

        self._rapida_prioritaria = LinkedQueue()
        self._rapida_normal = LinkedQueue()
        self._tradicional_prioritaria = LinkedQueue()
        self._tradicional_normal = LinkedQueue()

        #Los vamos acumulando para poder sacar estadisticas
        self._pedidos_finalizados = []

    def registrar_pedido(self, pedido:Pedido):
        #Inserta el pedido en la cola de registro
        self._cola_registro.enqueue(pedido)


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

    def prioridades_y_retrasos(self):         
        # 1º Comprobar si el pedido normla supera las 8 unidades de tiempo para pasarlo a prioritario
        normales = [(self._rapida_normal, self._rapida_prioritaria),(self._tradicional_normal, self._tradicional_prioritaria)]
        for colas_normal, colas_prio in normales:
            if not colas_normal.is_empty():
                pedido = colas_normal.first()
                if (self._t_actual - pedido.t_entrada) > 8:
                    pedido = colas_normal.dequeue()
                    pedido.prioridad = 'prioritario'
                    colas_prio.enqueue(pedido)
                    print(f"tiempo {self._t_actual}: pedido {pedido.id_pedido} que entró en tiempo {pedido.t_entrada} ESCALADO a prioritario")

        # 2º Comprobar retraso y mostrar mensaje de retraso
        prioritarios = [self._rapida_prioritaria, self._tradicional_prioritaria]
        for colas_prio in prioritarios:
            if not colas_prio.is_empty():
                pedido = colas_prio.first()
                if (self._t_actual - pedido.t_entrada) > 5:
                    print(f"tiempo {self._t_actual}: pedido {pedido.id_pedido} que entró en tiempo {pedido.t_entrada} RETRASADO")

    def avanzar_tiempo(self):
        #Avanza el tiempo
        self._t_actual += 1

        if self._t_actual % 2 == 0 and not self._cola_registro.is_empty():
            #Cada 2 de unidades de tiempo extraemos el pedido y lo clasificamos, guardando el tiempo de entrada
            p = self._cola_registro.dequeue()
            p.t_entrada = self._t_actual
            self._clasificar_pedido(p)

            print(f"tiempo {self._t_actual}: entrada de pedido {p.id_pedido} "
                  f"de comida {p.tipo}-{p.prioridad}, duración:{p.duracion_entrega}")

        #Cada vez que avanza el tiempo comprobamos prioridades y retrasos
        self.prioridades_y_retrasos()


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

    

