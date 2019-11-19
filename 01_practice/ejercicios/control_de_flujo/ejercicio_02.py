''' Realiza un programa que lea un número impar por teclado.
Si el usuario no introduce un número impar, debe repetise 
el proceso hasta que lo introduzca correctamente. '''

numero = int(input("Ingrese un número \n"))
while (numero % 2 == 0):
    print("Error, introduzca un número impar \n")
    numero = int(input("Ingrese un número \n"))

print("El número ", numero, " es impar => ¡Correcto!")
