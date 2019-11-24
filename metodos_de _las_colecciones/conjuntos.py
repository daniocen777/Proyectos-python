conjunto = set()
''' Añadir '''
conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
print(conjunto)  # {1, 2, 3}
''' Descartar un elemento '''
conjunto.discard(1)
print(conjunto)  # {2, 3}
conjunto.add(1)
''' Copia de un conjunto '''
conjunto_2 = conjunto.copy()
conjunto_2.add(4)
print(conjunto)  # {1, 2, 3}
print(conjunto_2)  # {1, 2, 3, 4}
''' Limpiar el conjunto '''
conjunto_2.clear()
print(conjunto_2)  # set()
''' Comparación de conjuntos '''
c1 = {1, 2, 3}
c2 = {3, 4, 5}
c3 = {-1, 99}
c4 = {1, 2, 3, 4, 5}
# -- Conjuntos disjuntos-- #
print(c1.isdisjoint(c3))  # True
print(c1.isdisjoint(c2))  # False > concuenrda con el 3
# -- Subconjunto-- #
print(c1.issubset(c4))  # True
print(c3.issubset(c4))  # False
# -- Contenedor de conjunto-- #
print(c4.issuperset(c2))  # True
print(c4.issuperset(c3))  # False
''' Elementos diferentes entre conjuntos '''
c_update = c1.difference(c2)
print(c_update)  # {1, 2}
