''' Más utilizadas de python => clave-valor '''
dicccionario_vacio = {}
colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
# Acceso al valor
print(colores['azul'])  # result => blue
numeros = {10: 'diez', 20: 'veinte'}
print(numeros[10])  # result => diez
''' modificar los elementos '''
colores['amarillo'] = 'white'
# result => {'amarillo': 'white', 'azul': 'blue', 'verde': 'green'}
print(colores)
''' borrar los elementos '''
del(colores['amarillo'])
print(colores)  # result => {'azul': 'blue', 'verde': 'green'}
''' Recorrer un diccionario '''
edades = {'Memo': 20, 'Pepe': 45, 'Lucia': 20, 'Juan': 32}
# Recorrido de claves
for edad in edades:
    print(edad)  # result => Memo \n Pepe \n Lucia \ Juan

# Recorrido de los valores
for clave in edades:
    print(edades[clave])  # result => 20 \n 45 \n 20 \ 32

# Mostrar las claves y sus valores
for clave in edades:
    print(clave, edades[clave])

''' Manera correcta de recorrer diccionarios '''
for clave, valor in edades.items():
    print(clave, valor)
''' result => Memo 20
Pepe 45
Lucia 20
Juan 32 '''

''' Colecciones de datos avanzadas '''
lista_personajes = []
personaje = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Humano'}
lista_personajes.append(personaje)  # agregando diccionario a la lista
personaje = {'Nombre': 'Legolas', 'Clase': 'Arqueras', 'Raza': 'Elfo'}
lista_personajes.append(personaje)  # agregando diccionario a la lista
personaje = {'Nombre': 'Gimli', 'Clase': 'Guerreo', 'Raza': 'Enano'}
lista_personajes.append(personaje)  # agregando diccionario a la lista
# result => [{'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Humano'}, {'Nombre': 'Legolas', 'Clase': 'Arqueras', 'Raza': 'Elfo'}, {'Nombre': 'Gimli', 'Clase': 'Guerreo', 'Raza': 'Enano'}]
print(lista_personajes)
# Recorriendo
for p in lista_personajes:
    print(p['Nombre'], p['Clase'])
''' result :
 Gandalf Mago
Legolas Arqueras
Gimli Guerreo  '''
