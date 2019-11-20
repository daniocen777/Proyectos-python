class Player:
    """ self => instancia de la clase """

    """ init ==> para definir el comportamiento la clase con su instancia """
    """ El objetivo fundamental del método __init__ es inicializar los
     atributos del objeto que creamos """

    """ Las ventajas de implementar el método __init__ en lugar del método inicializar son:
   1. El método __init__ es el primer método que se ejecuta cuando se crea un objeto.
   2. El método __init__ se llama automáticamente. Es decir es imposible de olvidarse de
    llamarlo ya que se llamará automáticamente.
   3. Quien utiliza POO en Python (Programación Orientada a Objetos) conoce el
    objetivo de este método.
   Otras características del método __init__ son:
    => Se ejecuta inmediatamente luego de crear un objeto. """

    """ 1° forma """
    """ def __init__(self, hit_points=50, mana=50, vocation="No vocation", hechizo="Puff"):
        self.hit_points = hit_points  # por defecto
        self.mana = mana
        self.vocation = vocation
        self.hechizo = hechizo  # hechizo """

    """ 2° forma => on diccionario """

    def __init__(self, **kwargs):
        self.hit_points = kwargs.get("hit_points", 50)
        self.mana = kwargs.get("mana", 50)
        self.vocation = kwargs.get("vocation", "No vocation")
        self.hechizo = kwargs.get("hechizo", "Puff")

    def lanzar_hechizo(self):
        return self.hechizo
