"""
Autores:
    Iago Núñez Lourés - iago.nunez.loures@udc.es
    Rubén Rodríguez Catrufo - ruben.rodriguez.catrufo@udc.es
"""

from avl_tree import AVL
from producto import Producto
import csv
import ast
import copy

class Inventario:
    """
    Representa el inventario de una cadena de supermercados.

    El inventario almacena los productos en un árbol AVL, utilizando el
    código EAN como clave. De esta forma, las inserciones, búsquedas y
    recorridos ordenados se realizan directamente sobre el TAD AVL.
    """

    def __init__(self, nombre):
        """
        Crea un inventario vacío.

        Parameters
        ----------
        nombre : str
            Nombre de la cadena o del inventario.

        Returns
        -------
        None.
        """
        self._nombre = nombre
        self._productos = AVL()

    def __len__(self):
        """
        Devuelve el número de productos del inventario.

        Parameters
        ----------
        None.

        Returns
        -------
        int
            Número de productos almacenados en el árbol AVL.
        """
        return len(self._productos)

    def insertar_producto(self, prod):
        """
        Inserta un producto en el inventario.

        El producto se almacena en el árbol AVL usando su código EAN como
        clave. Si ya existe un producto con el mismo EAN, se sustituye el
        valor anterior por el nuevo producto.

        Parameters
        ----------
        prod : producto
            Producto que se va a insertar en el inventario.

        Returns
        -------
        None.
        """
        self._productos[prod.ean] = prod

    def contiene(self, ean):
        """
        Comprueba si existe un producto con el EAN indicado.

        Parameters
        ----------
        ean : str
            Código de barras del producto que se desea buscar.

        Returns
        -------
        bool
            True si el producto está en el inventario, False en caso contrario.
        """
        #AVL_Tree tira un KeyError si no existe. Aunque en este ejercicio no deberia saltar nunca,
        #debemos tenerlo en cuenta porque sino nunca devolveria false, sino una excepcio
        try:
            self._productos[ean]
            return True
        except KeyError:
            return False

    def obtener_producto(self, ean):
        """
        Devuelve el producto asociado a un código EAN.

        Parameters
        ----------
        ean : str
            Código de barras del producto que se desea obtener.

        Returns
        -------
        producto
            Producto asociado al código EAN indicado.

        Raises
        ------
        KeyError
            Si no existe ningún producto con ese EAN en el inventario.
        """
        #No controlamos la excepcion en esta, ya que en este caso si que nos aporta informacion, 
        # y podemos dejar al usuario de la clase decidir si controlarla desde fuera
        return self._productos[ean]

    def cargar_csv(self, ruta):
        """
        Carga los productos de un archivo CSV en el inventario.

        El archivo debe contener una cabecera y las columnas necesarias para
        construir cada producto: EAN, nombre, categoría, precio, stock,
        proveedores y fecha de última reposición.

        Parameters
        ----------
        ruta : str
            Ruta del archivo CSV que contiene los productos.

        Returns
        -------
        None.
        """
        with open(ruta, newline="") as csvfile:
            lector = csv.reader(csvfile, delimiter=",")
            next(lector)  # Saltamos la cabecera del csv

            for row in lector:
                prod = Producto(
                    row[0],
                    row[1],
                    row[2],
                    float(row[3]),
                    int(row[4]),
                    ast.literal_eval(row[5]),
                    row[6]
                )

                self.insertar_producto(prod)

    def mostrar_inorden(self):
        """
        Muestra el inventario ordenado por código EAN.

        El recorrido se realiza sobre el árbol AVL, que devuelve las claves
        ordenadas de menor a mayor. Cada clave permite recuperar e imprimir
        el producto asociado.

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
        print("RECORRIDO INORDEN (ordenado por código de barras):")
        print("=" * 55)

        for ean in self._productos:
            print(self._productos[ean])

    def fusionar_unificado(self, otro, nombre):
        """
        Crea un inventario unificado con todos los productos.

        El inventario resultante contiene los productos de ambos inventarios.
        Si un producto aparece en los dos, se fusiona sumando el stock,
        combinando proveedores sin duplicados, tomando el precio del producto
        con fecha de reposición más reciente y conservando dicha fecha más
        reciente.

        Parameters
        ----------
        otro : Inventario
            Segundo inventario que se fusionará con el inventario actual.
        nombre : str
            Nombre que tendrá el inventario resultante.

        Returns
        -------
        tuple
            Tupla formada por el inventario unificado y la lista de incidencias
            generadas durante la fusión.
        """
        resultado = copy.deepcopy(self)
        resultado.nombre = nombre

        incidencias = []

        for ean in otro._productos:
            prod_otro = otro._productos[ean]

            if not resultado.contiene(ean):
                resultado.insertar_producto(copy.deepcopy(prod_otro))
            else:
                prod_resultado = resultado.obtener_producto(ean)

                # Para el unificado usamos la fecha como criterio.
                prod_fusionado, incidencia = self._fusionar_productos(
                    prod_resultado, prod_otro, criterio_precio="fecha")

                resultado.insertar_producto(prod_fusionado)
                incidencias.append(incidencia)

        return resultado, incidencias

    def fusionar_comun(self, otro, nombre):
        """
        Crea un inventario común con los productos compartidos.

        El inventario resultante solo contiene productos que aparecen en ambos
        inventarios. Para cada producto compartido, se suma el stock, se
        combinan los proveedores sin duplicados, se toma el precio más caro y
        se conserva la fecha de reposición más reciente.

        Parameters
        ----------
        otro : Inventario
            Segundo inventario con el que se compara el inventario actual.
        nombre : str
            Nombre que tendrá el inventario común resultante.

        Returns
        -------
        tuple
            Tupla formada por el inventario común y la lista de incidencias
            generadas durante la fusión.
        """
        resultado = Inventario(nombre)
        incidencias = []

        # Solo recorremos productos del primer inventario.
        # Si también están en el segundo, se fusionan.
        for ean in self._productos:
            prod_self = self._productos[ean]

            if otro.contiene(ean):
                prod_otro = otro.obtener_producto(ean)

                prod_fusionado, incidencia = self._fusionar_productos(
                    prod_self, prod_otro, criterio_precio="mayor")

                resultado.insertar_producto(prod_fusionado)
                incidencias.append(incidencia)

        return resultado, incidencias

    def contar_compartidos(self, otro):
        """
        Cuenta cuántos productos aparecen en ambos inventarios.

        Parameters
        ----------
        otro : Inventario
            Inventario con el que se compara el inventario actual.

        Returns
        -------
        int
            Número de productos compartidos por ambos inventarios.
        """
        contador = 0

        for ean in self._productos:
            if otro.contiene(ean):
                contador += 1

        return contador

    def contar_unicos(self, otro):
        """
        Cuenta cuántos productos aparecen solo en uno de los inventarios.

        Parameters
        ----------
        otro : Inventario
            Inventario con el que se compara el inventario actual.

        Returns
        -------
        int
            Número de productos exclusivos de uno de los dos inventarios.
        """
        compartidos = self.contar_compartidos(otro)
        return len(self) + len(otro) - 2 * compartidos

    def _fusionar_productos(self, prod1, prod2, criterio_precio):
        """
        Fusiona dos productos con el mismo código EAN.

        El método crea una copia profunda del primer producto y modifica sus
        datos para representar la combinación de ambos productos. El criterio
        de precio cambia según el tipo de fusión: por fecha para el inventario
        unificado y por precio mayor para el inventario común.

        Parameters
        ----------
        prod1 : producto
            Producto procedente del primer inventario.
        prod2 : producto
            Producto procedente del segundo inventario.
        criterio_precio : str
            Criterio usado para decidir el precio final. Puede ser "fecha" o
            "mayor".

        Returns
        -------
        tuple
            Tupla formada por el producto fusionado y el texto de incidencia
            que describe los cambios realizados.
        """
        fusionado = copy.deepcopy(prod1)
        fusionado.stock = prod1.stock + prod2.stock

        # Combinamos proveedores sin duplicados.
        for proveedor in prod2.proveedores:
            if proveedor not in fusionado.proveedores:
                fusionado.proveedores.append(proveedor)

        # Decidimos precio según el tipo de fusión.
        if criterio_precio == "fecha":
            if prod2.fecha > prod1.fecha:
                fusionado.precio = prod2.precio
            else:
                fusionado.precio = prod1.precio

        elif criterio_precio == "mayor":
            fusionado.precio = max(prod1.precio, prod2.precio)

        fusionado.fecha = max(prod1.fecha, prod2.fecha)

        incidencia = (
            f"{fusionado.ean} ({fusionado.nombre}) (SC) vs (MM)\n"
            f" Stock: {prod1.stock} + {prod2.stock} = {fusionado.stock} unidades\n"
            f" Precio: {prod1.precio}€ vs {prod2.precio}€ -> {fusionado.precio}€\n"
            f" Proveedores: {prod1.proveedores} vs {prod2.proveedores} -> {fusionado.proveedores}\n"
            f" Fecha reposición: {prod1.fecha} vs {prod2.fecha} -> {fusionado.fecha}"
        )

        return fusionado, incidencia
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre