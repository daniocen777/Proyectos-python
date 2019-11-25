from collections import Counter
lista = [1, 2, 3, 4, 1, 2, 3, 2, 1]
''' Cuenta la cantidad de veces que se repite un elemento '''
print(Counter(lista))  # Counter({1: 3, 2: 3, 3: 2, 4: 1})
cadena = 'Una palabra'
# Counter({'a': 4, 'U': 1, 'n': 1, ' ': 1, 'p': 1, 'l': 1, 'b': 1, 'r': 1})
print(Counter(cadena))

