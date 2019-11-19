''' Realiza un programa que sume todos los números enteros 
pares desde el 0 hasta el 100. '''

numero = int(input("Ingrese el número \n"))
suma = 0
''' conteo = 1
while (conteo <= numero):
    if (conteo % 2 == 0):
        suma += conteo
    conteo += 1

print("La suma es:", suma) '''

''' Otra forma '''
suma = sum(range(0, numero + 1, 2))
print("La suma es:", suma)
