""" Utilizando todo lo que sabes sobre cadenas, listas, sus
 métodos internos... Transforma este texto: """

""" un día que el viento soplaba con fuerza#mira como se mueve aquella banderola
 -dijo un monje#lo que se mueve es el viento
  -respondió otro monje#ni las banderolas ni el viento, lo 
  que se mueve son vuestras mentes -dijo el maestro """

""" Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro. """

texto = 'un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro'

lineas = texto.split('#')
for index, linea in enumerate(lineas):
    lineas[index] = linea.capitalize()
    if (index == 0):
        lineas[index] = lineas[index] + '...'
    else:
        lineas[index] = '- ' + lineas[index] + '.'

for linea in lineas:
    print(linea)
