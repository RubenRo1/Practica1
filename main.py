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

#Listas que usaremos para facilitar la busqueda de oficinas y evitar iterar toda la lista de edificios
OFICINAS_CON_ESPACIO = []
OFICINAS_LLENAS = []

def inmigracion(ciudad:Ciudad):
    """
    Añade habitantes de la ciudad

    Parameters
    ----------
    ciudad : Ciudad
        Ciudad a la cual vendrán(o no) nuevos habitantes

    Returns
    -------
    inmigrantes : int
        Número de habitantes que han entrado la ciudad
    """
    inmigrantes = 0
    if random.random() < 0.4:
        inmigrantes = random.randint(5, 200)
        ciudad.habitantes = ciudad.habitantes + inmigrantes
    return inmigrantes

def emigracion(ciudad:Ciudad):
    """
    Elimina habitantes de la ciudad

    Parameters
    ----------
    ciudad : Ciudad
        Ciudad de la cual se irán (o no) los habitantes

    Returns
    -------
    emigrantes : int
        Número de habitantes que han abandonado la ciudad
    """

    #Almacenamos habitantes en una variable para no estar accediendo constantemente
    habitantes = ciudad.habitantes
    emigrantes = 0
    if ciudad.felicidad > 40:
        if habitantes > 5 and random.random() < 0.2:
            #Si hay menos de 200 habitantes, se usarña el numero de habitantes como cota superior
            emigrantes = random.randint(5, 200 if habitantes > 200 else habitantes)
    else:
        if habitantes > 5 and random.random() < 0.35:
            emigrantes = random.randint(5, 200 if habitantes > 200 else habitantes)

    ciudad.habitantes = habitantes - emigrantes
    return emigrantes

def crear_empresas(ciudad:Ciudad):
    """
    Crea empresas en la ciudad

    Parameters
    ----------
    ciudad : Ciudad
        Ciudad sobre la que se crearán (o no) las empresas

    Returns
    -------
    empresas : int
        Número de empresas que se han creado
    """

    if random.random() < 0.3:
        empresas = random.randint(1, 5)
        capacidad = ciudad.obtener_capacidad_oficinas() - ciudad.obtener_empresas_actuales()

        #Si no hay capacidad para nuevas empresas, terminamos la funcion
        if capacidad == 0:
            return 0
        #Si hay espacio, pero menos del numero de empresas que queremos construir, constriremos las máximas posibles
        if capacidad < empresas:
             empresas = capacidad
        
        i = empresas
        while i > 0:
            #Siempre intentamos llenar la primera oficina, como si fuese una cola
            oficina = OFICINAS_CON_ESPACIO[0]
            i -= oficina.asignar_empresas(i)
            #Si se llena la oficina, la quitamos de oficinas_con_espacio y la metemos en oficinas_llenas
            if oficina.obtener_capacidad_disponible() == 0:
                OFICINAS_LLENAS.append(OFICINAS_CON_ESPACIO.pop(0))

        return empresas
    return 0

def encontrar_oficinas_con_empresas():
    """
    Busca oficinas que tengan espacio disponible

    Parameters
    ----------

    Returns
    -------
    oficina : Oficinas
        Oficina con espacio disponible
    """

    #Primero, intentamos abrir espacio en las oficinas que estén llenas
    if len(OFICINAS_LLENAS) > 0:
        return OFICINAS_LLENAS.pop(0)
    
    #Si no hay oficinas llenas, buscaremos una oficina que tenga alguna empresa
    for oficina in OFICINAS_CON_ESPACIO:
        if oficina.capacidad_oficinas != oficina.obtener_capacidad_disponible():
            return oficina
            

def cierre_empresas(ciudad:Ciudad):
    """
    Cierra empresas en la ciudad

    Parameters
    ----------
    ciudad : Ciudad
        Ciudad sobre la que se cerrarán (o no) las empresas

    Returns
    -------
    empresas : int
        Número de empresas que se han cerrado
    """

    if random.random() < 0.15:
        empresas = random.randint(1, 3)

        #Si no hay oficinas en la ciudad, terminamos la funcion
        if ciudad.obtener_empresas_actuales() == 0:
            return 0
        #Si hay oficinas, pero menos de las que queremos cerrar, cerraremos las que sea posible
        if ciudad.obtener_empresas_actuales() < empresas:
            empresas = ciudad.obtener_empresas_actuales()

        i = empresas
        while i > 0:
            oficina = encontrar_oficinas_con_empresas()
            i -= oficina.eliminar_empresas(i)
            #Si la oficina no estaba en la lista de oficinas con espacio, la añadiremos tras liberar espacio
            if oficina not in OFICINAS_CON_ESPACIO:
                OFICINAS_CON_ESPACIO.append(oficina)
        return empresas
    
    return 0

def construir_desde_pool(clase, bloque):
    """
    Crea edificios de Viviendas, Oficinas y Equipamiento empleando la pool de datos, 
    y escogiendo de forma aleatoria entre ellos.

    Parameters
    ----------
    clase : Class
        Tipo de dato del edificio (Viviendas, Oficinas, Equipamiento)
    bloque : dict
        Bloque con los parametros correspondientes al tipo de edificio a construir.

    Returns
    -------
    edificio : String
        Tipo del edificio construido. En caso de que no se construya nada, devolvera NoneType
    """
    #En nuestro pool, existen 24 posibilidades entre las que elegir. Escogeremos un numero
    #del 0 al 24 y construiremos ese edificio con los parametros de esas posiciones
    n = 24
    i = random.randint(0, n - 1)

    #Diccionario que guardará los argumentos a recibir de cada clase
    argumentos = {}
    for clave, valores in bloque.items():
        argumentos[clave] = valores[i]

    #Creamos el objeto de la clase indicada descomprimiendo el diccionario que creamos antes
    return clase(**argumentos)
        
def construir_edificios(ciudad:Ciudad, pools:dict, nuevas_empresas:bool):
    """
    Construye los edificios de la ciudad atendiendo a las reglas de la simulacón

    Parameters
    ----------
    ciudad : Ciudad
        Objeto Ciudad en el que se construirán los edificios.
    pools : dict
        Diccionario con los datos de los edificios.
    nuevas_empresas : bool
        Marcador de si se han construido nuevas empresas en este mes.

    Returns
    -------
    String
        String con el tipo de edificio
    """

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

    #Solo construimos el edificio si se ha cumplido alguna de las condiciones
    if edificio != None:
        if not ciudad.construir_edificio(edificio):
            edificio = None
        #Si el edificio es una oficina, lo añadimos a la lista de oficinas con espacio
        if isinstance(edificio, Oficinas):
            OFICINAS_CON_ESPACIO.append(edificio)

    return str(type(edificio))



def simulacion(ciudad: Ciudad, pools:dict, num_meses: int):
    """
    Ejecuta la simulación mes a mes de la ciudad, aplicando eventos aleatorios
    y actualizando el estado de la ciudad.

    Parameters
    ----------
    ciudad : Ciudad
        Objeto Ciudad sobre el que se ejecuta la simulación.
    pools : dict
        Diccionario con los datos de las clases para construirlas.
    num_meses : int
        Número de meses a simular.

    Returns
    -------
    data : list
        Lista con los datos de la simulación
    """

    data = []
    #Diccionario con las clases de edificio, para poder imprimir su tipo
    tipos_de_edificio = {"<class 'NoneType'>":'Ninguno',
                         "<class 'equipamiento.Equipamiento'>":'Equipamientos',
                         "<class 'oficinas.Oficinas'>":'Oficinas',
                         "<class 'viviendas.Viviendas'>":'Viviendas'}

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
        n_empresas = crear_empresas(ciudad)
        n_cierres = cierre_empresas(ciudad)

        edificio = construir_edificios(ciudad, pools, n_empresas != 0)

        # Actualización de la ciudad
        ciudad.actualizar_presupuesto()
        ciudad.actualizar_felicidad()

        # Mostrar estado mensual resumido
        print(f"Habitantes:            {ciudad.habitantes}")
        print(f"Felicidad:             {ciudad.felicidad}")
        print(f"Presupuesto:           {ciudad.presupuesto}")

        print(f'Llegada de habitantes: {inmigrantes}')
        print(f'Salida de habitantes:  {emigrantes}')
        print(f'Empresas creadas:      {n_empresas}')
        print(f'Empresas cerradas:     {n_cierres}')
        print(f'Edificios construidos:  {tipos_de_edificio[edificio]}')

        data.append([ciudad.habitantes, ciudad.felicidad, ciudad.presupuesto, inmigrantes, emigrantes, 
                     n_empresas, n_cierres, ciudad.obtener_empresas_actuales(), ciudad.obtener_capacidad_oficinas(), len(ciudad.edificios)])

    return data

def analisis_estadistico(data:list, columnas:list, estadisticas:list):
    """
    Crea el dataframe con las columnas indicadas e imprime sus estadisticas

    Parameters
    ----------
    data : list
        Lista con los datos en crudo
    columnas : list
        Lista con los nombres de cada columna
    estadisticas : list
        Lista con los datos estadisticos a extraer de cada columna (media, desviación típica...)

    Returns
    -------
    None
    """
    dataframe = pd.DataFrame(data, columns=columnas)

    argumentos = dict.fromkeys(columnas, estadisticas)
    analisis = dataframe.agg(argumentos)
    print(analisis)

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
    
    #Cargamos el json con la pool de datos para crear edificios
    with open("/home/iago/code/uni/prog/Practica1/pools1.json", "r", encoding="utf-8") as f:
        pools = json.load(f)

    ciudad = Ciudad('Villa Vamos Tarde', HABITANTES_INICIALES, 15000000, 20, [])
    data = simulacion(ciudad, pools, NUM_MESES)

    #Analisis estadistico de la simulacion
    #Nombres de las columnas que analizaremos
    columnas = ['habitantes', 'felicidad', 'presupuesto', 'inmigrantes', 
                'emigrantes', 'empresas creadas', 'empresas cerradas', 
                'empresas totales', 'capacidad de empresas', 'edificios']
    
    #Informacion estadistica que queremos extraer del dataframe
    estadisticas = ["mean","std", 'max', 'min']
    
    print(f'\n\n--- Estadisticas de los {NUM_MESES} meses de simulación ---\n')
    analisis_estadistico(data, columnas, estadisticas)

    print("   SIMULACIÓN COMPLETADA")
 
