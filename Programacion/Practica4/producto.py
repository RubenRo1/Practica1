

class producto:
    def __init__(self, codigo_barra, nombre, categoria, precio, stock, proveedores:list, fecha):
        self.codigo_barra = codigo_barra
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.proveedores = proveedores
        self.fecha = fecha

    
    def __str__(self):
        return f"{self.nombre} | {self.categoria} | {self.precio} | {self.stock} | {self.proveedores} | {self.fecha} |"
