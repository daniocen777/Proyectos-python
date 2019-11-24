class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: {}, {} ruedas'.format(self.color, self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ', {} Km/h, {} cc'.format(self.velocidad, self.cilindrada)

coche = Coche('azul', 4, 150, 1200)
print(coche)