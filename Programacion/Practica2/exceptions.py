"""
Autores:
    Iago Núñez Lourés
    Rubén Rodríguez Catrufo

Archivo con las excepciones que deben usar las clases
del programa.
"""

class Empty(Exception):
    """Error attempting to access an element from an empty container."""

    pass

class tipo_invalido(Exception):
    """
        El tipo del pedido no es valido
        Debe ser o 'rapida' o 'tradicional'.
    """

    pass

class prioridad_invalida(Exception):
    """
        La prioridad del pedido no es valida.
        Debe ser o 'prioritario' o 'normal'.
    """

    pass