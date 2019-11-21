''' Número indeterminado de argumentos '''
def indeterminados_por_posicion(*args):
    print(args)
# result => (5, 'Holas', [1, 2, 3, 4]) => tupla
indeterminados_por_posicion(5, 'Holas', [1, 2, 3, 4])

''' kwargs => Key word arguments '''
def indeterminados_por_nombre(**kwargs):
    print(kwargs)
# result => {'c': 3, 'n': 'Holas', 'lista': [4, 5, 6, 7]} => diccionario
indeterminados_por_nombre(c=3, n='Holas', lista=[4, 5, 6, 7])

def super_funcion(*args, **kwargs):
    t = 0
    for arg in args:
        t += arg
    print('Suma indeterminada es:', t)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

super_funcion(1, -1, 22, 144, 5, nombre='Dani', edad=34)
''' result:
Suma indeterminada es: 171
nombre Dani
edad 34 '''
