def resta(a, b):
    return a - b


''' print(resta(b=2, a=10)) '''

# valores de los parámetros por defecto


def suma(a=0, b=0):
    return a + b


''' print(suma()) '''

# valores de los parámetros por defecto (Nones)


def resta_2(a=None, b=None):
    if a == None or b == None:
        print('Error, debe enviar los datos "a" y "b"')
        return
    else:
        return a - b


print(resta_2(2, 4))
