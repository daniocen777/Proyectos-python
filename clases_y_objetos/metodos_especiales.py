class Pelicula:
    ''' constructor '''

    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película', self.titulo)

    ''' Método destructor '''

    def __del__(self):
        print('Se está borrando la película', self.titulo)

    ''' Método string => redefinir '''

    def __str__(self):
        return '{}'.format(self.titulo)

    ''' Método length => redefinir '''

    def __len__(self):
        return self.duracion


p = Pelicula('El Padrino', 175, 1972)
print(len(p))
