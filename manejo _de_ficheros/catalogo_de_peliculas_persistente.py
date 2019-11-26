from io import open
import pickle


class Pelicula:
    ''' constructor '''

    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película', self.titulo)

    ''' Método string => redefinir '''

    def __str__(self):
        return '{}'.format(self.titulo)


class Catalogo:
    peliculas = []

    # Constructor
    def __init__(self):
        self.cargar()

    def agregar(self, p):
        self.peliculas.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print('El catálogo está vacío')
            return

        for p in self.peliculas:
            print(p)

    # ab => append binario + lectura
    def cargar(self):
        # Te crea el fichero si no existe
        fichero = open('catalogo.pckl', 'ab+')
        fichero.seek(0)
        try:
            # Intentar leer
            self.peliculas = pickle.load(fichero)
        except:
            print('Fichero vacío')
        finally:
            fichero.close()
            del(fichero)
            print('Se ha cargado {} películas'.format(len(self.peliculas)))

    def guardar(self):
        fichero = open('catalogo.pckl', 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()
        del(fichero)

    # Destructor
    def __del__(self):
        self.guardar()  # Guardado automático
        print('Se ha guardado el fichero')


catalogo = Catalogo()
''' catalogo.agregar(Pelicula('El Padrino', 175, 1972))
catalogo.agregar(Pelicula('El Padrino: Parte 2', 202, 1974)) '''
catalogo.agregar(Pelicula('Otra pelícla', 120, 2001))
catalogo.mostrar()
