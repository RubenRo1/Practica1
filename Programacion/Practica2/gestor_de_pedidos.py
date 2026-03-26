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
        self._pedidos_en_reparto = []
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
                p = colas_normal.first()
                if (self._t_actual - p.t_entrada) > 8:
                    p = colas_normal.dequeue()
                    p.prioridad = 'prioritario'
                    colas_prio.enqueue(p)
                    print(f"tiempo {self._t_actual}: pedido {p.id_pedido} que entró en tiempo {p.t_entrada} ESCALADO a prioritario")

        # 2º Comprobar retraso y mostrar mensaje de retraso
        prioritarios = [self._rapida_prioritaria, self._tradicional_prioritaria]
        for colas_prio in prioritarios:
            if not colas_prio.is_empty():
                p = colas_prio.first()
                
                if (self._t_actual - p.t_entrada) > 5:




                    # ------------------------------------------------IA-----------------------------------------------------------
                    if not hasattr(p, '_avisado_retraso'): # Comprueba si existe el flag
                        print(f"tiempo {self._t_actual}: pedido {p.id_pedido} que entró en tiempo {p.t_entrada} RETRASADO")
                        p._avisado_retraso = True
                    # ------------------------------------------------IA-----------------------------------------------------------




                    

    def obtener_siguiente_pedido(self):

        if not self._rapida_prioritaria.is_empty():
            return self._rapida_prioritaria.dequeue()
        
        elif not self._tradicional_prioritaria.is_empty():
            return self._tradicional_prioritaria.dequeue()
        
        elif not self._rapida_normal.is_empty():
            return self._rapida_normal.dequeue()
        
        elif not self._tradicional_normal.is_empty():
            return self._tradicional_normal.dequeue()

        return None
    
    def gestionar_reparto(self):
        
        for p in self._pedidos_en_reparto[:]:
            if self._t_actual == (p.t_inicio_reparto + p.duracion_entrega):
                self._pedidos_en_reparto.remove(p)
                self._repartidores += 1
                print(f"tiempo {self._t_actual}: fin reparto pedido {p.id_pedido}, iniciado en tiempo {p.t_inicio_reparto}, duración: {p.duracion_entrega}")
        
        while self._repartidores > 0:
            siguiente = self.obtener_siguiente_pedido()

            if siguiente is not None:

                siguiente.t_inicio_reparto = self._t_actual
                self._pedidos_en_reparto.append(siguiente)
                self._repartidores -= 1
                print(f"tiempo {self._t_actual}: inicio reparto pedido {siguiente.id_pedido} que entró en tiempo {siguiente.t_entrada}, duración {siguiente.duracion_entrega}")
            
            else:
                break

    def avanzar_tiempo(self):
        #Avanza el tiempo
        self._t_actual += 1

        if self._t_actual % 2 == 0 and not self._cola_registro.is_empty():
            #Cada 2 de unidades de tiempo extraemos el pedido y lo clasificamos, guardando el tiempo de entrada
            p = self._cola_registro.dequeue()
            p.t_entrada = self._t_actual
            self._clasificar_pedido(p)

            print(f"tiempo {self._t_actual}: entrada de pedido {p.id_pedido} de comida {p.tipo}-{p.prioridad}, duración:{p.duracion_entrega}")

        #Cada vez que avanza el tiempo comprobamos prioridades y retrasos
        self.prioridades_y_retrasos()
        self.gestionar_reparto()


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

    

