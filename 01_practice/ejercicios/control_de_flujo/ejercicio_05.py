''' Realiza un programa que pida al usuario cuantos números 
quiere introducir. Luego lee todos los números y realiza 
una media aritmética. '''

suma = 0
cantidadNumeros = int(
    input("Ingrese la cantidad de números que quiere introducir \n"))
    
for x in range(cantidadNumeros):
    suma += float(input("Ingrese el número \n"))

promedio = suma / cantidadNumeros
print("El promedio es:", promedio)
