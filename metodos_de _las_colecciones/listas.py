lista = [1, 2, 3, 4, 5]
lista.append(5)  # añadir
lista.clear()  # borra todos los elementos
''' unir listas '''
lista_1 = [2, 4, 6]
lista_2 = [10, 12, 14]
lista_1.extend(lista_2)
print(lista_1)  # [2, 4, 6, 10, 12, 14]
''' Contar un elemento y el índeice en una lista y  '''
lista_3 = ['holas', 'mundos', 'mundos', 'mundos']
print(lista_3.count('mundos'))  # 3
print(lista_3.index('holas'))  # 0
''' Intoruducir un elemento en el índice especificado '''
lista_4 = [5, 10, 15, 25]
lista_4.insert(-1, 20)
print(lista_4)  # [5, 10, 15, 20, 25]
''' Eliminar un elemento en el índice especificado '''
lista_5 = [10, 20, 30, 40, 50]
lista_5.pop(1)
print(lista_5)  # [10, 30, 40, 50]
''' Eliminar un elemento '''
lista_6 = [10, 20, 30, 40, 40, 40, 50]
lista_6.remove(40)  # Sólo borra el primero
print(lista_6)  # [10, 20, 30, 40, 40, 50]
''' Dar la vuelta a la lista '''
lista_7 = [10, 20, 30, 40, 50]
lista_7.reverse()
print(lista_7)  # [50, 40, 30, 20, 10]
''' Ordenar una lista numérica '''
lista_8 = [2, 1, 5, 7, 4, 8, 3]
lista_8.sort() # de menor a mayor
print(lista_8)  # [1, 2, 3, 4, 5, 7, 8]
lista_8.sort(reverse=True) # de mayor a menor
print(lista_8)  # [8, 7, 5, 4, 3, 2, 1]
