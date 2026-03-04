"""
Simulación de la evolución de SimCiudad mediante eventos aleatorios
"""
import sys
import json
import random
import pandas as pd
from edificios import Edificio
from oficinas import Oficinas
from equipamiento import Equipamiento
from viviendas import Viviendas
from ciudad import Ciudad



# Configuración de la simulación
NUM_MESES = None
NOMBRE_CIUDAD = None
ABITANTES_INICIALES = None
PRESUPUESTO_INICIAL = None

# Configuración de semilla para reproducibilidad (opcional)
#random.seed(42)

#Listas que usaremos como colas con las oficinas con espacio disponible y llenas
OFICINAS_CON_ESPACIO = []
OFICINAS_LLENAS = []

def inmigracion(ciudad:Ciudad):
    inmigrantes = 0
    if random.random() < 0.4:
        inmigrantes = random.randint(5, 200)
        ciudad.habitantes = ciudad.habitantes + inmigrantes
    return inmigrantes

def emigracion(ciudad:Ciudad):
    #Almacenamos habitantes en una variable para no estar accediendo constantemente
    habitantes = ciudad.habitantes
    emigrantes = 0
    if ciudad.felicidad > 40:
        if habitantes > 5 and random.random() < 0.2:
            emigrantes = random.randint(5, 200 if habitantes > 200 else habitantes)
    else:
        if habitantes > 5 and random.random() < 0.35:
            emigrantes = random.randint(5, 200 if habitantes > 200 else habitantes)

    ciudad.habitantes = habitantes - emigrantes
    return emigrantes

def crear_empresas(ciudad:Ciudad):

    if random.random() < 0.3:
        empresas = random.randint(1, 5)
        capacidad = ciudad.obtener_capacidad_oficinas() - ciudad.obtener_empresas_actuales()

        if capacidad == 0:
            #Si no hay capacidad para nuevas empresas, terminamos la funcion
            return False, 0
        if capacidad < empresas:
             empresas = capacidad
        
        i = empresas
        while i > 0:
            oficina = OFICINAS_CON_ESPACIO[0]
            i -= oficina.asignar_empresas(i)
            #Si se llena la oficina, la quitamos de oficinas_con_espacio y la metemos en oficinas_llenas
            if oficina.obtener_capacidad_disponible() == 0:
                OFICINAS_LLENAS.append(OFICINAS_CON_ESPACIO.pop(0))

        return True, empresas
    return False, 0

def encontrar_oficinas_con_empresas():
    if len(OFICINAS_LLENAS) > 0:
        return OFICINAS_LLENAS.pop(0)
    
    #Si no hay oficinas llenas, buscaremos una oficina que tenga alguna empresa
    for oficina in OFICINAS_CON_ESPACIO:
        if oficina.capacidad_oficinas != oficina.obtener_capacidad_disponible():
            return oficina
            

def cierre_empresas(ciudad:Ciudad):

    if random.random() < 0.15:
        empresas = random.randint(1, 3)

        if ciudad.obtener_empresas_actuales() == 0:
            #Si no hay oficinas en la ciudad, terminamos la funcion
            return False, 0
        if ciudad.obtener_empresas_actuales() < empresas:
            empresas = ciudad.obtener_empresas_actuales()

        i = empresas
        while i > 0:
            oficina = encontrar_oficinas_con_empresas()
            i -= oficina.eliminar_empresas(i)
            #Si se llena la oficina, la quitamos de oficinas_con_espacio y la metemos en oficinas_llenas
            if oficina not in OFICINAS_CON_ESPACIO:
                OFICINAS_CON_ESPACIO.append(oficina)
        return True, empresas
    
    return False, 0

def construir_desde_pool(clase, bloque):
    i = random.randint(0, 23)
    kwargs = {}
    for clave, valores in bloque.items():
        kwargs[clave] = valores[i]
    return clase(**kwargs)
        
def construir_edificios(ciudad:Ciudad, pools:dict, nuevas_empresas:bool):

    edificio = None

    if ciudad.obtener_capacidad_viviendas() /ciudad.habitantes > 0.9:
        edificio = construir_desde_pool(Viviendas, pools['viviendas'])
    elif (ciudad.obtener_capacidad_oficinas() - ciudad.obtener_empresas_actuales()) < 5 and nuevas_empresas:
        edificio = construir_desde_pool(Oficinas, pools['oficinas'])
    elif ciudad.felicidad < 40:
        edificio = construir_desde_pool(Equipamiento, pools['equipamientos'])
    elif ciudad.presupuesto > 3_000_000:
        tipos_de_edificios = [(Viviendas, 'viviendas'), (Oficinas, 'oficinas'), (Equipamiento, 'equipamientos')]
        tipo = random.choice(tipos_de_edificios)
        edificio = construir_desde_pool(tipo[0], pools[tipo[1]])

    if edificio != None:
        ciudad.construir_edificio(edificio)
        if isinstance(edificio, Oficinas):
            OFICINAS_CON_ESPACIO.append(edificio)



def simulacion(ciudad: Ciudad, pools:dict, num_meses: int):
    """
    Ejecuta la simulación mes a mes de la ciudad, aplicando eventos aleatorios
    y actualizando el estado de la ciudad.

    Parameters
    ----------
    ciudad : Ciudad
        Objeto Ciudad sobre el que se ejecuta la simulación.
    pool_viviendas : dict
        Diccionario con los datos de viviendas para construir desde el pool.
    pool_oficinas : dict
        Diccionario con los datos de oficinas para construir desde el pool.
    pool_equipamiento : dict
        Diccionario con los datos de equipamientos para construir desde el pool.
    num_meses : int
        Número de meses a simular.

    Returns
    -------
    None
    """
    data = []

    # Construir edificios iniciales: 2 viviendas, 1 oficina, 1 equipamiento
    for _ in range(2):
        ciudad.construir_edificio(construir_desde_pool(Viviendas, pools['viviendas']))
    oficina = construir_desde_pool(Oficinas, pools['oficinas'])
    OFICINAS_CON_ESPACIO.append(oficina)
    ciudad.construir_edificio(oficina)
    ciudad.construir_edificio(construir_desde_pool(Equipamiento, pools['equipamientos']))

    print("\n=== ESTADO INICIAL ===")
    print(ciudad)

    # Bucle de simulación mes a mes
    for mes in range(1, num_meses + 1):
        print(f"\n--- Mes {mes} ---")

        # Eventos aleatorios
        inmigrantes = inmigracion(ciudad)
        emigrantes = emigracion(ciudad)
        nuevas_empresas, n_empresas = crear_empresas(ciudad)
        hubo_cierres, n_cierres = cierre_empresas(ciudad)

        construir_edificios(ciudad, pools, nuevas_empresas)

        # Actualización de la ciudad
        ciudad.actualizar_presupuesto()
        ciudad.actualizar_felicidad()

        # Mostrar estado mensual resumido
        print(f"Habitantes: {ciudad.habitantes}")
        print(f"Felicidad: {ciudad.felicidad}")
        print(f"Presupuesto: {ciudad.presupuesto}")
        #print(f"Edificios: {[ed.nombre for ed in ciudad.edificios]}")

        data.append([mes, ciudad.habitantes, ciudad.felicidad, ciudad.presupuesto, inmigrantes, emigrantes, 
                     n_empresas, n_cierres, ciudad.obtener_empresas_actuales(), ciudad.obtener_capacidad_oficinas(), len(ciudad.edificios)])

    return data

# Completar las con las funciones que realizan la simulación

if __name__ == "__main__":
	
	# Leer el archivo de configuración desde la línea de comandos o usar el predeterminado
    #config_file = sys.argv[1] if len(sys.argv) > 1 else "ciudad1.txt"
    config_file = '/home/iago/code/uni/prog/Practica1/ciudad1.txt'

    # Intentar abrir el archivo especificado
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: El archivo '{config_file}' no existe.", file=sys.stderr)
        sys.exit(1)

    # Leer los datos del  archivo
    print(f"Leyendo configuración desde: {config_file}")
	
    for linea in lines:
        clave, valor = linea.split(":", 1)
        clave = clave.strip()
        valor = valor.strip()

        if clave == "NUM_MESES":
            NUM_MESES = int(valor)
        elif clave == "NOMBRE_CIUDAD":
            NOMBRE_CIUDAD = valor.strip('"')
        elif clave == "HABITANTES_INICIALES":
            HABITANTES_INICIALES = int(valor)
        elif clave == "PRESUPUESTO_INICIAL":
            PRESUPUESTO_INICIAL = int(valor)
            
    with open("/home/iago/code/uni/prog/Practica1/pools0.json", "r", encoding="utf-8") as f:
        pools = json.load(f)

    ciudad = Ciudad('Villa Vamos Tarde', HABITANTES_INICIALES, 15000000, 20, [])
    data = simulacion(ciudad, pools, 40)

    #Creacion del dataframe
    columnas = ['mes', 'habitantes', 'felicidad', 'presupuesto', 'inmigrantes', 
                'emigracion', 'empresas creadas', 'empresas cerradas', 'empresas totales', 'capacidad de empresas', 'edificios']
    tabla_simulacion = pd.DataFrame(data, columns=columnas)
    print(tabla_simulacion)
    print("   SIMULACIÓN COMPLETADA")
 
