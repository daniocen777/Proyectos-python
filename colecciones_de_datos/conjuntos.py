''' Colección desordenada de elementos únicos '''
conjunto = set()  # conjunto vacío
conjunto = {1, 2, 3}
conjunto.add(4)  # añadir al final
grupo = {"Daniel", "Mario", "Lola", "Carla"}
flag = "Daniel" in grupo  # true
print(flag)  # Retorna un true
''' No elementos duplicados '''
test = {"Daniel", "Daniel", "Daniel", "María"}
print(test)  # result => {'Daniel', 'María'}
''' Ejm.: Castear una lista a un conjunto = > se eliminan los elementos repetidos '''
lista = [1, 2, 3, 3, 3, 4, 5, 5]
conjunto_cast = set(lista)
print(conjunto_cast)  # result => {1, 2, 3, 4, 5}
''' Tranformar un conjunto a una lista '''
lista_cast = list(conjunto_cast)
print(lista_cast)  # result => [1, 2, 3, 4, 5]
''' Convertir una cadena a un conjunto (no se repiten las letras) '''
cadena = "Al pan pan y al vino vino"
# result => {' ', 'o', 'y', 'p', 'a', 'n', 'v', 'A', 'l', 'i'}
print(set(cadena))
