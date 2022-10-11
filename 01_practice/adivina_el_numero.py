from random import randint

intentos = 0
numero_usuario = 0
numero_secreto = randint(1, 100)
print(numero_secreto)
nombre = input('¿Quién eres?\n')

print(f"Hola {nombre}, tienes 8 intentos para adivinar el número")

while intentos < 8:
    numero_usuario = int(input("ingresa tu número:"))
    intentos += 1

    if numero_usuario < numero_secreto:
        print("El número es mayor a esa cantidad")
    elif numero_usuario > numero_secreto:
        print("El número es menor a esa cantidad")
    else:
        print(
            f"Felicitaciones {nombre}, acertaste con el número {numero_usuario}")
        break

if numero_usuario != numero_secreto:
    print(f"Perdiste, el número era {numero_secreto}")
