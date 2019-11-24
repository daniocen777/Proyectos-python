print('Holas mundos perdidos'.upper())  # HOLAS MUNDOS PERDIDOS
print('Holas mundos perdidos'.lower())  # holas mundos perdidos
print('holas mundos perdidos'.capitalize())  # Holas mundos perdidos
print('holas mundos perdidos'.title())  # Holas Mundos Perdidos
print('holas mundos perdidos'.count('o'))  # 3
print('holas mundos perdidos'.count('mundos'))  # 1
print('holas mundos perdidos'.find('mundos'))  # 6 (índice)
print('holas mundos mundos mundos perdidos'.rfind(
    'mundos'))  # 20 (última aparición)

cadena = '100'  # todos los caracteres son números
print(cadena.isdigit())  # True

cadena_2 = 'ABc100po'  # caracteres alfanuméricos
print(cadena_2.isalnum())  # True

cadena_3 = 'ABc100po-'  # caracteres alfanuméricos y expresiones !=
print(cadena_3.isalnum())  # False

cadena_4 = 'ABc100po'  # solo caracteres alfabéticos
print(cadena_4.isalpha())  # False (los espacios NO SON alfabéticos)

cadena_5 = 'HOLAS mundos'
print(cadena_5.isupper())  # False

cadena_5 = 'holas mundos'
print(cadena_5.islower())  # True

cadena_6 = '    '
print(cadena_6.isspace())  # True

cadena_7 = 'holas mundos'
print(cadena_7.startswith('holas'))  # True

cadena_8 = 'holas mundos'
print(cadena_8.endswith('s'))  # True

""" Separar una cadena a partir de espacios o símbolos """
cadena_9 = 'holas mundos perdidos'
print(cadena_9.split())  # lista => ['holas', 'mundos', 'perdidos']

cadena_10 = 'holas mundos perdidos'
print(cadena_10.split()[-1])  # perdidos

cadena_11 = 'holas mundos perdidos'
print(cadena_11.split()[0])  # holas

cadena_12 = 'holas-mundos perdidos'
print(cadena_12.split('-'))  # lista => ['holas', 'mundos perdidos']

""" Unir una cadena a partir de espacios o símbolos """
separador = ','
cadena_13 = 'holas-mundos perdidos'
print(separador.join(cadena_13))  # h,o,l,a,s,-,m,u,n,d,o,s, ,p,e,r,d,i,d,o,s
cadena_14 = 'holas-mundos perdidos'
print(separador.join(cadena_14)[5:10])  # ,a,s, (cuenta con las comas)

""" Quitar caracteres al inicio y final"""
cadena_15 = '---holas-mundos perdidos-'
print(cadena_15.strip('-'))  # holas-mundos perdidos

""" Reemplazar cadenas """
cadena_16 = 'holas mundos mundos mundos mundos mundos perdidos'
# holas mundos perdidos (4 => reemp. 4 veces)
print(cadena_16.replace(' mundos', '', 4))
