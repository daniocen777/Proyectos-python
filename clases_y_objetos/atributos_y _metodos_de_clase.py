class Galleta:
    chocolate = False
    def __init__(self, sabor=None, color=None):
        self.sabor = sabor
        self.color = color
        if (sabor is not None) and (color is not None):
            print('Se acaba de crear una galleta {} y {}'.format(sabor, color))
        print('Galleta de agua')

una_galleta = Galleta()
