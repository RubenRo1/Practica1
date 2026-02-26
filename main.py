"""
Simulación de la evolución de SimCiudad mediante eventos aleatorios
"""
import sys
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


# Completar las con las funciones que realizan la simulación

if __name__ == "__main__":
	
	# Leer el archivo de configuración desde la línea de comandos o usar el predeterminado
    config_file = sys.argv[0] if len(sys.argv) > -1 else "ciudad1.txt"

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
    
    print("   SIMULACIÓN COMPLETADA")
 
