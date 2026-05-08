

class producto:
    def __init__(self, ean, nombre, categoria, precio, stock, proveedores:list, fecha):
        self._ean = ean
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._stock = stock
        self._proveedores = proveedores
        self._fecha = fecha

    
    def __str__(self):
        """
        Devuelve una representación en texto del producto.
        """
        return (
        f"{self.ean} - {self.nombre} - {self.categoria}\n"
        f" Precio: {self.precio}€\n"
        f" Stock: {self.stock} unidades\n"
        f" Proveedores: {self.proveedores}\n"
        f" Fecha reposición: {self.fecha}"
        )
    
    @property
    def ean(self):
        return self._ean

    @ean.setter
    def ean(self, nuevo_ean):
        self._ean = nuevo_ean

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, nueva_categoria):
        self._categoria = nueva_categoria

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        self._precio = nuevo_precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock):
        self._stock = nuevo_stock

    @property
    def proveedores(self):
        return self._proveedores

    @proveedores.setter
    def proveedores(self, nuevos_proveedores):
        self._proveedores = nuevos_proveedores

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        self._fecha = nueva_fecha