

class producto:
    def __init__(self, ean, nombre, categoria, precio, stock, proveedores:list, fecha):
        self.ean = ean
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.proveedores = proveedores
        self.fecha = fecha

    
    def __str__(self):
        return f"{self.nombre} | {self.categoria} | {self.precio} | {self.stock} | {self.proveedores} | {self.fecha} |"
