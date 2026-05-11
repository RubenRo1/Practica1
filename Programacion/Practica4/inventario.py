from avl_tree import AVL
from producto import producto
import csv
import ast
import copy


class Inventario:
    """
    Representa el inventario de una cadena de supermercados.

    Internamente almacena los productos en un árbol AVL, usando como clave
    el código EAN de cada producto.
    """

    def __init__(self, nombre):
        """
        Crea un inventario vacío.

        Args:
            nombre (str): Nombre de la cadena o inventario.
        """
        self._nombre = nombre
        self._productos = AVL()

    def __len__(self):
        """
        Devuelve el número de productos del inventario.

        Returns:
            int: Número de productos almacenados en el AVL.
        """
        return len(self._productos)

    def insertar_producto(self, prod):
        """
        Inserta un producto en el inventario.

        Si ya existe un producto con el mismo EAN, se sustituye.

        Args:
            prod (producto): Producto que se va a insertar.
        """
        self._productos[prod.ean] = prod

    def contiene(self, ean):
        """
        Comprueba si existe un producto con el EAN indicado.

        Args:
            ean (str): Código de barras del producto.

        Returns:
            bool: True si el producto existe, False en caso contrario.
        """
        try:
            self._productos[ean]
            return True
        except KeyError:
            return False

    def obtener_producto(self, ean):
        """
        Devuelve el producto asociado a un EAN.

        Args:
            ean (str): Código de barras del producto.

        Returns:
            producto: Producto asociado al EAN.

        Raises:
            KeyError: Si el EAN no existe en el inventario.
        """
        return self._productos[ean]

    def cargar_csv(self, ruta):
        """
        Carga los productos de un archivo CSV en el inventario.

        El CSV debe tener las columnas:
        EAN, nombre, categoría, precio, stock, proveedores y fecha.

        Args:
            ruta (str): Ruta del archivo CSV.
        """
        with open(ruta, newline="") as csvfile:
            lector = csv.reader(csvfile, delimiter=",")
            next(lector)  # Saltamos la cabecera

            for row in lector:
                prod = producto(
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

        El recorrido es inorden porque el AVL mantiene las claves ordenadas.
        """
        print("RECORRIDO INORDEN (ordenado por código de barras):")
        print("=" * 55)

        for ean in self._productos:
            print(self._productos[ean])


    def fusionar_unificado(self, otro, nombre):
        """
        Crea un inventario unificado con todos los productos.

        Si un producto aparece en ambos inventarios:
        - se suma el stock;
        - se combinan los proveedores sin duplicados;
        - se conserva el precio del producto con fecha de reposición más reciente;
        - se conserva la fecha de reposición más reciente.
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

                #Para el unificado usamos la fexcha como criterio
                prod_fusionado, incidencia = self._fusionar_productos(
                    prod_resultado, prod_otro, criterio_precio="fecha")

                resultado.insertar_producto(prod_fusionado)
                incidencias.append(incidencia)

        return resultado, incidencias

    def fusionar_comun(self, otro, nombre):
        """
        Crea un inventario común solo con los productos compartidos.

        Si un producto aparece en ambos inventarios:
        - se suma el stock;
        - se combinan los proveedores sin duplicados;
        - se conserva el precio más caro;
        - se conserva la fecha de reposición más reciente.

        Args:
            otro (Inventario): Segundo inventario a fusionar.

        Returns:
            tuple: Inventario común e incidencias generadas.
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

        Args:
            otro (Inventario): Segundo inventario.

        Returns:
            int: Número de productos compartidos.
        """
        contador = 0

        for ean in self._productos:
            if otro.contiene(ean):
                contador += 1

        return contador

    def contar_unicos(self, otro):
        """
        Cuenta cuántos productos aparecen solo en uno de los inventarios.

        Args:
            otro (Inventario): Segundo inventario.

        Returns:
            int: Número de productos no compartidos.
        """
        compartidos = self.contar_compartidos(otro)
        return len(self) + len(otro) - 2 * compartidos

    def _fusionar_productos(self, prod1, prod2, criterio_precio):
        """
        Fusiona dos productos con el mismo EAN.

        Args:
            prod1 (producto): Producto del primer inventario.
            prod2 (producto): Producto del segundo inventario.
            criterio_precio (str): Puede ser "fecha" o "mayor".

        Returns:
            tuple: Producto fusionado e incidencia en formato texto.
        """
        fusionado = copy.deepcopy(prod1)

        # Sumamos stock.
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

        # La fecha siempre será la más reciente.
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