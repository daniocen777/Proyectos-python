class Producto:
    def __init__(self, referencia, nombre, precio, descripcion):
        self.referecia = referencia
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return"""
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PRECIO\t\t{}
        DESCRIPCIÓN\t{}
        """.format(self.referecia, self.nombre, self.precio, self.descripcion)


class Adorno(Producto):
    pass


adorno = Adorno(2014, 'Vaso adornado', 15,
                'Vaso de porcelana adornado con árboles')
print(adorno)


class Alimento(Producto):

    def __init__(self, referencia, nombre, precio, descripcion, productor, distribuidor):
        super().__init__(referencia, nombre, precio, descripcion)
        self.productor = productor
        self.distribuidor = distribuidor

    def __str__(self):
        return"""
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PRECIO\t\t{}
        DESCRIPCIÓN\t{}
        PRODUCTOR\t{}
        DISTRIBUIDOR\t{}
        """.format(self.referecia, self.nombre, self.precio, self.descripcion, self.productor, self.distribuidor)


a = Alimento(2990, 'Pan', 34.22, 'Pan al pan', 'Panadería', 'Panadero')
print(a)
