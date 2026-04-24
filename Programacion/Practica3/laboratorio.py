"""
Autores:
    Iago Núñez Lourés - iago.nunez.loures@udc.es
    Rubén Rodríguez Catrufo - ruben.rodriguez.catrufo@udc.es
"""
from libro_recetas import libro_recetas
from ingrediente import ingrediente
from array_ordered_positional_list import ArrayOrderedPositionalList as ListaOrdenada

class laboratorio:
    """
    Clase controladora que orquesta la interacción entre el almacén y el recetario.

    Gestiona el ciclo de vida de las pociones: desde la verificación de stock 
    hasta el procesamiento de carencias mediante la esencia universal y la 
    limpieza de ingredientes agotados. [cite: 4, 9, 65]

    Attributes
    ----------
    _recetario : libro_recetas
        Instancia que contiene el diccionario de pócimas disponibles. [cite: 13]
    _almacen : ListaOrdenada
        Lista posicional basada en array con los ingredientes en stock. [cite: 10, 67]
    """

    def __init__(self, recetario:libro_recetas, almacen:ListaOrdenada):
        """
        Inicializa el laboratorio con sus dos estructuras principales.

        Parameters
        ----------
        recetario : libro_recetas
            El libro que contiene las recetas cargadas.
        almacen : ListaOrdenada
            La lista de existencias disponibles.
        
        Returns
        -------
        None.
        """
        self._recetario= recetario
        self._almacen = almacen

    def _encontrar_ingrediente(self, elemento):
        """
        Localiza un ingrediente en el almacén mediante búsqueda binaria.

        Aprovecha que la lista está basada en arrays para lograr una 
        eficiencia O(log n). [cite: 67]

        Parameters
        ----------
        elemento : ingrediente or str
            Objeto ingrediente o cadena de texto con el nombre a buscar.

        Returns
        -------
        int or None
            La posición (índice) en el array si se encuentra, None si no.
        """
        nombre = elemento if isinstance(elemento, str) else elemento.nombre

        if self._almacen.is_empty():
            return None

        izquierda = self._almacen.first()
        derecha = self._almacen.last()

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            ingrediente = self._almacen.get_element(medio)

            if ingrediente.nombre == nombre:
                return medio
            elif ingrediente.nombre < nombre:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        return None

    def crear_pocion(self, pocion:str):
        """
        Procesa el encargo de una poción específica. [cite: 27]

        Verifica disponibilidad, calcula carencias y determina si el encargo 
        puede ser atendido con o sin ayuda de la esencia universal. [cite: 5, 7]

        Parameters
        ----------
        pocion : str
            Nombre de la poción solicitada.

        Returns
        -------
        str
            Mensaje detallado con el resultado del encargo. [cite: 28-51]
        """
        salida = ''
        if not self._recetario.existe_receta(pocion):
            return f'Encargo NO ATENDIDO. Receta de {pocion} deconocida'
        salida += f'{self._recetario.get_receta(pocion)}\n'
        ingredientes = self._recetario.get_ingredientes(pocion)

        carencias, posiciones = self._check_carencias(ingredientes)

        #Los diccionarios vacios devuelven falso al checkearlos
        if not carencias:
            #Si no hay carencias, se atiende el encargo
            salida += f'Encargo {pocion} ATENDIDO'
            for pos, ingrediente in zip(posiciones, ingredientes):
                self._almacen.get_element(pos).cantidad -= ingrediente.cantidad
            return salida
        
        #Si hay carencias, llamamos al metodo de suplir carencias
        encargo_existoso, carencia_total, stock_esencia = self._suplir_carencias(carencias)
        #Si no se pueden suplir
        if not encargo_existoso:
            salida += f'Encargo {pocion} FALLIDO.\nFaltan (Sin comodin suficiente):\n'
            #Respectivos ingredientes con las cantidades que faltan
            for pos in carencias.keys():
                salida += f"\t- {self._almacen.get_element(pos).nombre}: {carencias[pos]}\n"
            #Stock de la esencia
            salida += f'Esencia universal:\n\t- disponible: {stock_esencia}\n\t- necesaria: {carencia_total}\n'
            return salida
        
        #si se pueden suplir
        salida += 'Suplido con esencia universal:\n'
        salida = salida.join(f'\t- {self._almacen.get_element(ingrediente).nombre}: {carencias[ingrediente]}\n'for ingrediente in carencias.keys())
        return salida

    def del_ingredientes_agotados(self, pocion):
        """
        Limpia el almacén y el recetario tras procesar un encargo. [cite: 6, 52]

        Elimina ingredientes con cantidad 0 y purga las recetas que los 
        requieren (borrado en cascada). [cite: 52-55]

        Parameters
        ----------
        pocion : str
            Nombre de la poción recién procesada.

        Returns
        -------
        str
            Registro de ingredientes agotados y recetas eliminadas.
        """

        salida = ''
        #Puede que la receta no exista
        if not self._recetario.existe_receta(pocion):
            return salida
    
        for ingrediente in self._recetario.recetas[pocion]:
            pos = self._encontrar_ingrediente(ingrediente)
            ingrediente_almacen = self._almacen.get_element(pos)

            if ingrediente_almacen.cantidad == 0:
                self._almacen.delete(pos)
                recetas_a_eliminar = self._recetario.del_pociones_por_ingrediente(ingrediente)
                for receta in recetas_a_eliminar:
                    salida += f'Agotado: {ingrediente.nombre} | Borrada: receta de {receta}\n'

        pos = self._encontrar_ingrediente('esencia_universal')
        esencia = self._almacen.get_element(pos) if pos != None else None
        
        if esencia != None and esencia.cantidad == 0:
            salida += 'Agotado esencia universal (*)'
            self._almacen.delete(pos)

        return salida

    def _suplir_carencias(self, carencias):
        """
        Calcula si la esencia universal puede cubrir las faltas detectadas. [cite: 39]

        Parameters
        ----------
        carencias : dict
            Diccionario {posicion_almacen: cantidad_faltante}.

        Returns
        -------
        tuple
            (bool: exito, int: carencia_total, int: stock_disponible).
        """

        #Calculamos la carencia total
        carencia_total = sum(carencias.values())

        pos = self._encontrar_ingrediente('esencia_universal')
        esencia = self._almacen.get_element(pos) if pos != None else None

        stock_esencia = 0 if esencia == None else esencia.cantidad

        #Si hay suficiente esencia, acualizamos la cantidades
        if stock_esencia >= carencia_total:
            esencia.cantidad -= carencia_total
            for ingrediente in carencias.keys():
                self._almacen.get_element(ingrediente).cantidad = 0

        return stock_esencia >= carencia_total, carencia_total, stock_esencia
    
    def _check_carencias(self, ingredientes:ListaOrdenada):
        """
        Compara los requisitos de una receta con el stock actual.

        Parameters
        ----------
        ingredientes_necesarios : ListaOrdenada
            Ingredientes y cantidades que pide la receta.

        Returns
        -------
        tuple
            (dict de carencias, list de posiciones con stock suficiente).
        """

        #Almacenamos las posiciones en el almacen y la carencia del ingrediente
        carencias = {}
        posiciones = []
        for ingrediente in ingredientes:
            pos = self._encontrar_ingrediente(ingrediente)
            ingrediente_almacen = self._almacen.get_element(pos)
            
            if ingrediente_almacen.cantidad < ingrediente.cantidad:
                #Guardamos las posiciones como clave para no tener que volver a realizar la busqueda
                #en caso de que se pueda hacer la receta
                carencias[pos] = ingrediente.cantidad - ingrediente_almacen.cantidad
            else:
                posiciones.append(pos)
            
        
        return carencias, posiciones

    def stock_actual(self):
        """
        Genera una cadena con el estado visual del almacén. [cite: 58-59]

        Returns
        -------
        str
            Representación formateada del stock.
        """
        salida = "--------STOCK ACTUAL--------\n"
        salida += " | ".join(str(ing) for ing in self._almacen)
        return salida        

    '''
    getters y setters
    '''

    