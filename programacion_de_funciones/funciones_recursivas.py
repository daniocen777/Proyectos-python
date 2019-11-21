def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print('Boooooooom!')
    print('Fin de la función', num)
cuenta_atras(5)
''' result:
4
3
2
1
Boooooooom! 
Fin de la función 0
Fin de la función 1
Fin de la función 2
Fin de la función 3
Fin de la función 4'''

''' Factorial de un número '''
def factorial(num):
    print('valor inicial =>', num)
    if num > 1:
        num = num * factorial(num -1)
    print('valor final =>', num)
    return num

print(factorial(5))  #  = 120
''' result:
valor inicial => 5
valor inicial => 4
valor inicial => 3
valor inicial => 2
valor inicial => 1
valor final => 1
valor final => 2
valor final => 6
valor final => 24
valor final => 120 '''