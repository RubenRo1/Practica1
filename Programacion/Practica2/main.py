from gestor_de_pedidos import gestor_pedidos
from pedido import Pedido

def main():
    gestor = gestor_pedidos(repartidores=2)

    #Como entenderas lo de leer el fichero lo hizo la IA xd
    try:
        with open('pedidos_06.txt', 'r') as fichero:
            for linea in fichero:
                datos = linea.split()
                if len(datos) == 5:
                    # id, cliente, tipo, prio, duracion
                    p = Pedido(datos[0], datos[1], datos[2], datos[3], int(datos[4]))
                    gestor.registrar_pedido(p) # <--- Aquí entra en tu cola_registro
    except FileNotFoundError:
        print("Fichero no encontrado")

    #Simulacion por 50 tiempos (para comprobar que se procesan los pedidos, se escalan y se retrasan)
    for _ in range(50):
        gestor.avanzar_tiempo()


if __name__ == "__main__":
    
    main()