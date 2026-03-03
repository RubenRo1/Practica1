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
random.seed(42)

#Listas que usaremos como colas con las oficinas con espacio disponible y llenas
OFICINAS_CON_ESPACIO = []
OFICINAS_LLENAS = []

def inmigracion(ciudad:Ciudad):
    if random.random() < 0.4:
        ciudad.habitantes = ciudad.habitantes + random.randint(5, 200)

def emigracion(ciudad:Ciudad):
    #Almacenamos habitantes en una variable para no estar accediendo constantemente
    habitantes = ciudad.habitantes
    if ciudad.felicidad > 40:
        if habitantes > 5 and random.random() < 0.2:
            ciudad.habitantes = habitantes - random.randint(5, 200 if habitantes > 200 else habitantes)
    else:
        if habitantes > 5 and random.random() < 0.35:
            ciudad.habitantes = habitantes - random.randint(5, 200 if habitantes > 200 else habitantes)

def crear_empresas(ciudad:Ciudad):

    if random.random() < 0.3:
        empresas = random.randint(1, 5)
        capacidad = ciudad.obtener_capacidad_oficinas() - ciudad.obtener_empresas_actuales()

        if capacidad == 0:
            #Si no hay capacidad para nuevas empresas, terminamos la funcion
            return
        if capacidad < empresas:
             empresas = capacidad
        while empresas < 0:
            oficina = OFICINAS_CON_ESPACIO[0]
            empresas -= oficina.asignar_empresas(empresas)
            #Si se llena la oficina, la quitamos de oficinas_con_espacio y la metemos en oficinas_llenas
            if oficina.obtener_capacidad_disponible() == 0:
                OFICINAS_LLENAS.append(OFICINAS_CON_ESPACIO.pop(0))

def cierre_empresas(ciudad:Ciudad):

    if random.random() < 0.15:
        empresas = random.randint(1, 3)

        if ciudad.obtener_empresas_actuales == 0:
            #Si no hay oficinas en la ciudad, terminamos la funcion
            return
        if ciudad.obtener_empresas_actuales() < empresas:
            empresas = ciudad.obtener_empresas_actuales()

        while empresas < 0:
            if len(OFICINAS_LLENAS) > 0:
                oficina = OFICINAS_LLENAS.pop(0)
            else:
                #Si no hay oficinas llenas, buscaremos una oficina que tenga alguna empresa
                for x in OFICINAS_CON_ESPACIO:
                    if x.capacidad_oficinas != x.obtener_capacidad_disponible():
                        oficina = x

            empresas -= oficina.eliminar_empresas(empresas)
            #Si se llena la oficina, la quitamos de oficinas_con_espacio y la metemos en oficinas_llenas
            OFICINAS_CON_ESPACIO.append(oficina)
        
def construir_edificios(ciudad:Ciudad, pool_viviendas:dict, pool_oficinas:dict, pool_equipamiento:dict):

    if ciudad.obtener_capacidad_viviendas/ciudad.habitantes > 0.9:
        seleccion = random.randint(0,23)
        edificio = Viviendas()
        ciudad.construir_edificio()

def construir_desde_pool(clase, bloque):
    i = random.randint(0, 23)
    kwargs = {}
    
    for clave, valores in bloque.items():
        kwargs[clave] = valores[i]

    return clase(**kwargs)

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
            
    # Ejecutar la simulación
    # Completar el código con la llamada a la función que inicia la simulación

    
    with open("/home/iago/code/uni/prog/Practica1/pools.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    vivienda = construir_desde_pool(
    Viviendas,
    data["viviendas"])
    
    print("   SIMULACIÓN COMPLETADA")
 
