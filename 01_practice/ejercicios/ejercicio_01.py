''' Realiza un programa que lea 2 números por teclado y 
determine los siguientes aspectos (es suficiene con mostrar True o False):

Si los dos números son iguales
Si los dos números son diferentes
Si el primero es mayor que el segundo
Si el segundo es mayor o igual que el primero '''

number1 = float(input("Ingrese el primer número: "))
number2 = float(input("Ingrese el segundo número: "))
print("¿Son iguales? ", number1 == number2)
print("¿Son diferentes? ", number1 != number2)
print("¿El primero es mayor que el segundo? ", number1 > number2)
print("¿El segundo es mayor o igual que el primero? ", number2 >= number1)
