''' Doblar valor de una lista de números '''
# Por referencia
def doblar_valor(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2
        print(numeros[i])


lista = [10, 50, 100]
doblar_valor(lista)
print(lista)
