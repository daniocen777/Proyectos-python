''' Realiza un programa que lea dos números por teclado y
 permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de introducir una opción inválida, el programa informará de que no es correcta. '''

primer_numero = float(input("Ingrese el primer número \n"))
segundo_numero = float(input("Ingrese el segundo número \n"))
opcion = 0

print(''' Menú 
1 => Sumar los dos números
2 => Restar los dos números
3 => Multiplicar los dos números
''')

opcion = int(input("Ingrese la opción que desea: \n"))

if (opcion == 1):
    print("La suma es: ", primer_numero + segundo_numero)
elif (opcion == 2):
    print("La resta es: ", primer_numero - segundo_numero)
elif (opcion == 3):
    print("La multiplicación es: ", primer_numero * segundo_numero)
else:
    print("La opción es inválida")
