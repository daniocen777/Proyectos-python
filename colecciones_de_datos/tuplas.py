''' Inmutables, a diferencia de las listas '''
tupla = (100, "Holas", [1, 2, 3, 4], -50, 100)
print(tupla)
# Consulta de elementos
# Desde -2 hasta el final
print(tupla[-2:])  # Resultado => ([1, 2, 3, 4], -50)
print(tupla[2][1])  # Elemento de lista dentro de la tupla = 2
''' index para buscar un elemento y saber su posición '''
print(tupla.index("Holas"))  # Respuesta => 1 | Sale error si no lo encuentra
''' Contar la cantidad de elementos que hay (elemento repetido) '''
print(tupla.count(100))  # Respuesta => 2
