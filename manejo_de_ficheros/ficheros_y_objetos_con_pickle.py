import pickle  # wr de cualquier elemento, no solo de texto plano
lista = [1, 2, 3, 4, 5]
# wb => escritura binaria
fichero = open('lista.pcjl', 'wb')  # Borra todo y puntero al inicio
pickle.dump(lista, fichero)  # binario
''' Recuperando el fichero en binario '''
# rb => lectura binaria
fichero = open('lista.pcjl', 'rb')
lista_2 = pickle.load(fichero)
''' print(lista_2)  # [1, 2, 3, 4, 5] '''
fichero.seek(0)  # Volviendo al inicio
fichero.close()
''' Guardando una clase '''


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


nombres = ['Héctor', 'Martha', 'Elizabeth']
personas = []
for n in nombres:
    p = Persona(n)
    personas.append(p)

fichero = open('personas.pckl', 'wb')
pickle.dump(personas, fichero)
fichero.close()
# Recuperando los datos
fichero = open('personas.pckl', 'rb')
personas_02 = pickle.load(fichero)
fichero.close()
# Recorrer
''' Héctor
Martha
Elizabeth '''
for persona in personas:
    print(persona)
