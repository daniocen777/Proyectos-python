''' En python, se emulan las pilas con listas '''
# pila => sólo añadir o quitar (LIFO)
from collections import deque
pila = [3, 4, 5]
pila.append(6)
pila.append(7)
print(pila)  # result => [3, 4, 5, 6, 7]
# Sacar el último elemento
pila.pop()
print(pila)  # result => [3, 4, 5, 6]
''' Error si se quita el último elemento de una pila vacía '''

''' Para las colas, se debe impotar => from collections import deque '''
# colas => sólo añadir o quitar (FIFO - 1° entrar 1° en salir)
cola = deque()
cola = deque(['Hector', 'Juana', 'Miguel'])
print(cola)  # result => deque(['Hector', 'Juana', 'Miguel'])
# Añadiendo
cola.append('Maria')
cola.append('Armando')
# result => deque(['Hector', 'Juana', 'Miguel', 'Maria', 'Armando'])
print(cola)
# sacar al 1°
primero = cola.popleft()
print(primero)  # result => Hector
print(cola)  # result => deque(['Juana', 'Miguel', 'Maria', 'Armando'])
