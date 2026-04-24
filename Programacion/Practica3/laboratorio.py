"""
Autores:
    Iago Núñez Lourés - iago.nunez.loures@udc.es
    Rubén Rodríguez Catrufo - ruben.rodriguez.catrufo@udc.es
"""
from libro_recetas import libro_recetas
from ingrediente import ingrediente
from array_ordered_positional_list import ArrayOrderedPositionalList as ListaOrdenada

class laboratorio:

    def __init__(self, recetario:libro_recetas, almacen:ListaOrdenada):
        self._recetario= recetario
        #que el almacen sea una lista posicional y no un diccionario solo complica las cosas
        #Es un mal uso de una lista posicional, ya que el orden de los ingredientes es irrelevante
        #y se deberia priorizar el facil acceso a los mismos

        #Usaremos una la lista ordenada de array ya que nos sera mas facil hacer la busqueda de losm ingredientes
        self._almacen = almacen

    def _encontrar_ingrediente(self, elemento:ingrediente):
        #Al ser una lista basada en arrays, podemos realizar busqueda binaria,
        #ya que las posiciones son numeros enteros
        if self._almacen.is_empty():
            return None

        izquierda = self._almacen.first()
        derecha = self._almacen.last()

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            ingrediente = self._almacen.get_element(medio)

            if ingrediente.nombre == elemento.nombre:
                return medio
            elif ingrediente.nombre < elemento.nombre:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        return None


    def crear_pocion(self, pocion:str):
        #Comprobamos que exista receta y la sacamos
        salida = ''
        if not self._recetario.existe_receta(pocion):
            return f'Encargo NO ATENDIDO. Receta de {pocion} deconocida'
        salida += f'{self._recetario.get_receta(pocion)}\n'
        ingredientes = self._recetario.get_ingredientes(pocion)

        carencias = self._check_carencias(ingredientes)

        #Los diccionarios vacios devuelven falso al checkearlos
        if not carencias:
            #Si no hay carencias, se atiende el encargo
            salida += f'Encargo {pocion} ATENDIDO'
            return salida
        
        #Si hay carencias, llamamos al metodo de suplir carencias
        encargo_existoso, carencia_total, stock_esencia = self._suplir_carencias(carencias)
        #Si no se pueden suplir
        if not encargo_existoso:
            salida += f'Encargo {pocion} FALLIDO.\nFaltan (Sin comodin suficiente):\n'
            #Respectivos ingredientes con las cantidades que faltan
            salida = salida.join(f'\t- {self._almacen.get_element(ingrediente).nombre}: {carencias[ingrediente]}\n'for ingrediente in carencias.keys())
            #Stock de la esencia
            salida += f'Esencia universal:\n\t- disponible: {stock_esencia}\n\t- necesaria: {carencia_total}\n'
            return salida
        
        #si se pueden suplir
        salida += 'Suplido con esencia universal:\n'
        salida = salida.join(f'\t- {self._almacen.get_element(ingrediente).nombre}: {carencias[ingrediente]}\n'for ingrediente in carencias.keys())
        return salida


    def del_ingredientes_agotados(self, pocion):
        for ingrediente in 

    def add_ingrediente():
        pass
    

    def _suplir_carencias(self, carencias):
        #Calculamos la carencia total
        carencia_total = sum(carencias.values())

        esencia = self._almacen.get_element(
                  self._encontrar_ingrediente('esencia_universal')
                  )
        stock_esencia = 0 if esencia == None else esencia.cantidad

        #Si hay suficiente esencia, acualizamos la cantidades
        if stock_esencia >= carencia_total:
            esencia.cantidad -= carencia_total
            for ingrediente in carencias.keys():
                self._almacen.get_element(ingrediente).cantidad = 0

        return stock_esencia >= carencia_total, carencia_total, stock_esencia



    
    def _check_carencias(self, ingredientes:ListaOrdenada):
        
        #Almacenamos las posiciones en el almacen y la carencia del ingrediente
        carencias = {}
        for ingrediente in ingredientes:
            pos = self._encontrar_ingrediente(ingrediente)
            ingrediente_almacen = self._almacen.get_element(pos)
            
            if ingrediente_almacen.cantidad < ingrediente.cantidad:
                #Guardamos las posiciones como clave para no tener que volver a realizar la busqueda
                #en caso de que se pueda hacer la receta
                carencias[pos] = ingrediente.cantidad - ingrediente_almacen.cantidad
            else:
                ingrediente_almacen.cantidad -= ingrediente.cantidad
        
        return carencias




    def stock_actual():
        pass

    '''
    getters y setters
    '''

    