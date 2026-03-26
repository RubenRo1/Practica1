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
    while (not gestor._cola_registro.is_empty() or 
           not gestor._rapida_prioritaria.is_empty() or
           not gestor._tradicional_prioritaria.is_empty() or
           not gestor._rapida_normal.is_empty() or
           not gestor._tradicional_normal.is_empty() or
           len(gestor._pedidos_en_reparto) > 0):
        gestor.avanzar_tiempo()


if __name__ == "__main__":
    
    main()