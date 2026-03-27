"""
Autores:
    Iago Núñez Lourés
    Rubén Rodríguez Catrufo
"""
import sys
import pandas as pd
from pedido import Pedido
from gestor_de_pedidos import gestor_pedidos
from linked_queue import LinkedQueue

def cargar_pedidos_desde_archivo(ruta):
    """
    Funcion que crea las 
    """
    cola_registro = LinkedQueue()

    with open(ruta, "r", encoding="utf-8") as archivo:
        for num_linea, linea in enumerate(archivo, start=1):
            linea = linea.strip()

            if not linea:
                continue

            partes = linea.split()

            if len(partes) != 5:
                raise ValueError(
                    f"Línea {num_linea} inválida: se esperaban 5 campos y hay {len(partes)} -> {linea}"
                )
            id_pedido, id_cliente, tipo, prioridad, duracion = partes
            pedido = Pedido(
                id_pedido,
                id_cliente,
                tipo,
                prioridad,
                int(duracion)
            )

            cola_registro.enqueue(pedido)

    return cola_registro

def crear_dataframe(pedidos:list):
    filas = []

    for pedido in pedidos:
        filas.append({
            "tipo": pedido.tipo,
            "tiempo_espera": pedido.t_inicio_reparto - pedido.t_entrada,
            "tiempo_total": pedido.t_fin - pedido.t_entrada,
            "escalado_automatico": pedido.cambio_prioridad
        })

    return pd.DataFrame(filas)

def mostrar_estadisticas(df:pd.DataFrame):
    tiempo_medio_espera_por_tipo = df.groupby("tipo")["tiempo_espera"].mean()
    porcentaje_escalados = df["escalado_automatico"].mean() * 100
    tiempo_total_medio = df["tiempo_total"].mean()

    print("\n--- ESTADÍSTICAS FINALES ---")
    print("\nTiempo medio de espera por tipo de pedido:")
    print(tiempo_medio_espera_por_tipo)

    print(f"\nPorcentaje de pedidos escalados automáticamente: {porcentaje_escalados:.2f}%")

    print(f"\nTiempo total medio desde la entrada hasta la entrega: {tiempo_total_medio:.2f}")

def mostrar_eventos(eventos:dict):
    #Pedidos registrados
    if eventos['pedido_registrado'] != None:
        pedido = eventos['pedido_registrado']
        print(f'tiempo {eventos['tiempo_actual']}: entrada de pedido {pedido.id_pedido} de comida {pedido.tipo}-{pedido.prioridad}, duración: {pedido.duracion_entrega} ')
    
    #Pedidos que entraron en reparto
    if len(eventos['pedidos_entraron_reparto']) > 0:
        for pedido in eventos['pedidos_entraron_reparto']:
            print(f'tiempo {eventos['tiempo_actual']}: inicio de reparto {pedido.id_pedido} que entró en tiempo {pedido.t_entrada}, duración: {eventos['tiempo_actual'] - pedido.t_entrada} ')

    #Pedidos que finalizaron reparto
    if len(eventos['pedidos_entregados']) > 0:
        for pedido in eventos['pedidos_entregados']:
            print(f'tiempo {eventos['tiempo_actual']}: fin de reparto {pedido.id_pedido} iniciado en tiempo {pedido.t_inicio_reparto}, duración: {pedido.duracion_entrega} ')

    #Aviso de pedidos por escalados
    if len(eventos['escalados']) > 0:
        for pedido in eventos['escalados']:
            print(f'tiempo {eventos['tiempo_actual']}: pedido {pedido.id_pedido} que entro en tiempo {pedido.t_entrada} ESCALADO a prioritario')

    #Aviso de pedidos por retraso
    if len(eventos['retrasados']) > 0:
        for pedido in eventos['retrasados']:
            print(f'tiempo {eventos['tiempo_actual']}: pedido {pedido.id_pedido} que entro en tiempo {pedido.t_entrada} RETRASADO')

if __name__ == '__main__':
    # Leer el archivo de configuración desde la línea de comandos o usar el predeterminado
    ruta = sys.argv[1] if len(sys.argv) > 1 else "/home/iago/code/uni/prog/Practica1/Programacion/Practica2/pedidos_06.txt"
    #creamos la cola de registro que le pasaremos al gestor
    cola_registro = cargar_pedidos_desde_archivo(ruta)
    gestor = gestor_pedidos(cola_registro)

    #mientras haya pedidos pendientes, vamos avanzando y mostrando los eventos
    while gestor.hay_pedidos_pendientes():
        mostrar_eventos(gestor.avanzar_tiempo())
    
    #Una vez acabada la simulacion, mostramos las estadisticas
    pedidos_finalizados = gestor.pedidos_finalizados
    df = crear_dataframe(pedidos_finalizados)
    mostrar_estadisticas(df)