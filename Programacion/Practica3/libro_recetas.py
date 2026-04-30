"""
Autores:
    Iago Núñez Lourés - iago.nunez.loures@udc.es
    Rubén Rodríguez Catrufo - ruben.rodriguez.catrufo@udc.es
"""
from ingrediente import ingrediente
from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenada

class libro_recetas:
    """
    Clase que gestiona el catálogo de fórmulas alquímicas del gremio.

    Utiliza un diccionario para indexar las pociones por nombre, donde cada 
    valor es una Lista Posicional Ordenada (enlazada) de objetos ingrediente.

    Attributes
    ----------
    _recetas : dict
        Estructura de datos principal {nombre_pocion (str): ingredientes (ListaOrdenada)}.
    """

    def __init__(self, recetas=None):
        """
        Inicializa el libro de recetas vacío o con una estructura preexistente.

        Parameters
        ----------
        recetas : dict, optional
            Diccionario inicial de recetas (por defecto None).
        
        Returns
        -------
        None.
        """
        self._recetas = {} if recetas == None else recetas

    def __str__(self):
        """
        Genera una representación textual de todo el catálogo.

        Returns
        -------
        str
            Listado completo de pociones y sus componentes.
        """
        salida = ''
        for receta in self._recetas.keys():
            salida += f'{receta}\n\t{self._recetas[receta]}'
            for ingrediente in self._recetas[receta]:
                salida += f' {" | ".join(ingrediente.nombre, ": ", ingrediente.cantidad)}'
            salida += '\n'
        return salida

    def existe_receta(self, pocion:str):
        """
        Verifica si una poción está registrada en el libro.

        Parameters
        ----------
        pocion : str
            Nombre de la poción a buscar.

        Returns
        -------
        bool
            True si la clave existe en el diccionario.
        """
        return pocion in self._recetas.keys()

    def add_receta(self, pocion:str, receta:ListaOrdenada):
        """
        Añade una nueva poción al catálogo.

        Parameters
        ----------
        pocion : str
            Nombre identificativo de la poción.
        receta : ListaOrdenada
            Lista de ingredientes ya instanciada y ordenada.
        """
        self._recetas[pocion] = receta

    def add_ingrediente_receta(self, pocion, ingrediente):
        """
        Añade un ingrediente individual a una receta ya existente.

        Parameters
        ----------
        pocion : str
            Nombre de la poción a modificar.
        ingrediente : ingrediente
            Objeto ingrediente a insertar en la lista posicional.
        """
        if self.existe_receta(pocion):
            self._recetas[pocion].add(ingrediente)

    def del_receta(self, pocion):
        """
        Elimina una poción completa del catálogo.

        Parameters
        ----------
        pocion : str
            Nombre de la poción a eliminar.
        """
        if self.existe_receta(pocion):
            del self._recetas[pocion]

    def get_ingredientes(self, pocion:str):
        """
        Obtiene la lista de ingredientes de una poción.

        Parameters
        ----------
        pocion : str
            Nombre de la poción.

        Returns
        -------
        ListaOrdenada or None
            La lista de componentes si existe, None en caso contrario.
        """
        if not self.existe_receta(pocion):
            return None
        return self._recetas[pocion]
            
    def get_receta(self, pocion):
        """
        Genera el formato visual de una única receta para la salida de encargos.

        Parameters
        ----------
        pocion : str
            Nombre de la poción a mostrar.

        Returns
        -------
        str
            Cadena formateada con la receta o mensaje de error.
        """
        if not self.existe_receta(pocion):
            return f'No existe receta de {pocion}'
        
        salida = f'Poción: {pocion}\n'
        for ingrediente in self._recetas[pocion]:
            salida += f'\t- {ingrediente.nombre}: {ingrediente.cantidad}\n'
        return salida
    
    def get_pociones_por_ingrediente(self, ingrediente:ingrediente):
        """
        Busca qué pociones contienen un ingrediente específico.

        Parameters
        ----------
        ingrediente : ingrediente
            El ingrediente que se desea localizar en las recetas.

        Returns
        -------
        list
            Lista de nombres de pociones que contienen dicho ingrediente.
        """
        pociones = []
        for pocion, receta in self._recetas.items():
            if ingrediente in receta:
                pociones.append(pocion)
        return pociones
    
    def del_pociones_por_ingrediente(self, ingrediente:ingrediente):
        """
        Elimina en cascada todas las recetas que contienen un ingrediente agotado.

        Parameters
        ----------
        ingrediente : ingrediente
            El ingrediente que ha llegado a stock cero.

        Returns
        -------
        list
            Nombres de las recetas que han sido borradas del catálogo.
        """
        recetas_a_eliminar = self.get_pociones_por_ingrediente(ingrediente)
        for receta in recetas_a_eliminar:
            self.del_receta(receta)
        
        return recetas_a_eliminar
    
    @property
    def recetas(self):
        return self._recetas
    
    @recetas.setter
    def recetas(self, recetas):
        self._recetas = recetas
