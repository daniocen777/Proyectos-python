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
''' print(adorno) '''


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


alimento = Alimento(2990, 'Pan', 34.22, 'Pan al pan', 'Panadería', 'Panadero')


class Libro(Producto):
    def __init__(self, referencia, nombre, precio, descripcion, sbn, autor):
        super().__init__(referencia, nombre, precio, descripcion)
        self.sbn = sbn
        self.autor = autor

    def __str__(self):
        return"""
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PRECIO\t\t{}
        DESCRIPCIÓN\t{}
        SBN\t{}
        AUTOR\t{}
        """.format(self.referecia, self.nombre, self.precio, self.descripcion, self.sbn, self.autor)


libro = Libro(2990, '2666', 89.22, 'Obra latinoamericana',
              '34444333', 'Pedro Páramo')

productos = [adorno, alimento]
productos.append(libro)
''' print(productos) '''

''' for p in productos:
    print(p, '\n') '''

''' for p in productos:
    # Si un producto es instncia de una Clase => return true
    if (isinstance(p, Adorno)):
        print(p.referecia, '|', p.nombre)
    elif(isinstance(p, Alimento)):
        print(p.referecia, '|', p.nombre, '|', p.productor, '|', p.distribuidor)
    elif(isinstance(p, Libro)):
        print(p.referecia, '|', p.nombre, '|', p.autor, '|', p.sbn)
    else:
        print('No hay') '''


def rebajar_producto(p, rebaja):
    ''' Devuelve un producto con una rebaja en % de su precio '''
    p.precio = p.precio - (p.precio/100 * rebaja)
    return p

alimento_rebajado = rebajar_producto(alimento, 10)
print(alimento_rebajado)
