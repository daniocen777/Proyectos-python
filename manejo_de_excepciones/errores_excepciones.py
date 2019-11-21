while (True):
    try:
        n = float(input('Introduce un número\n'))
        m = 4
        print('{}/{}={}'.format(n, m, n/m))
    except:
        print('Ha ocurrido un error, introduce un número')
    # else => se ejecutará si no hay excepción
    else:
        print('Todo OK')
        break  # Romper la iterción cuando se pueda dividir
    finally:
        print('Fin de la iteración')
