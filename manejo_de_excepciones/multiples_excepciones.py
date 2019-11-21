try:
    n = float(input('Introduce un número: '))
    print(5/n)
except TypeError:
    print('No se peude dividir un núemro con una cadena')
except ValueError:
    print('Se debe introducir un número')
except ZeroDivisionError:
    print('No se puede dividir por 0')
except Exception as e:
    print(type(e).__name__)
