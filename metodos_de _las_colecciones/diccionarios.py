colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'grenn'}
print(colores.get('amarillo', 'No se seencuentra'))  # yellow
print(colores.get('negro', 'No se seencuentra'))  # No se seencuentra
""" Si una clave está dentro de un diccionari """
flag = 'amarillo' in colores
print(flag)  # True
""" Para iterar """
# Solo las claves
print(colores.keys())  # dict_keys(['amarillo', 'azul', 'verde'])
# Los valores
print(colores.values())  # dict_values(['yellow', 'blue', 'grenn'])
# Claves y valores
# dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'grenn')])
print(colores.items())

for clave, valor in colores.items():
    print(clave, ' | ', valor)

""" amarillo  |  yellow
azul  |  blue
verde  |  grenn """
""" Quitar elemento """
colores.pop('amarillo', 'No se encontró color')
print(colores)  # {'azul': 'blue', 'verde': 'grenn'}
""" Vaciar el diccionario """
colores.clear()
