from io import open

fichero = open('fichero.txt', 'r')
# Caracter 10
fichero.seek(10)  # lee desde la posición 10
''' con texto
 Otra línea con texto
 Tercera línea del fichero '''
# Luego de leer, el puntero se coloca al final
''' print(fichero.read()) '''
# Colocando el puntero al inicio nuevamnete
fichero.seek(0)
''' Una línea con texto
 Otra línea con texto
 Tercera línea del fichero '''
''' print(fichero.read()) '''
# Colocando el puntero al inicio nuevamnete
fichero.seek(0)
# Leyendo 5 caracteres
''' print(fichero.read(5))  # Una l => puntero en la posición 5 '''
''' Ejemplo: Saber la cantidad de texto, posicionarse a la mitad  '''
fichero.seek(0)
texto = fichero.read()
fichero.seek(len(texto) / 2)
''' con texto
 Tercera línea del fichero '''
''' print(fichero.read()) '''
''' Ejemplo: 1° línea  '''
fichero.seek(0)
# readline => lee la 1° línea y se posiciona el puntero al final de esta
# readlines => lee todas las líneas
fichero.seek(len(fichero.readline()))  # final de la 1° línea
''' Otra línea con texto
 Tercera línea del fichero '''
''' print(fichero.read()) '''
fichero.close()
''' Lectura y escritura a la vez => r+ = lectura y escritura'''
# r => El puntero se posiciona al inicio, si escribo, se chancará el inicio
fichero = open('fichero.txt', 'r+')
fichero.close()
''' Modificar fichero en una línea específica '''
fichero = open('fichero.txt', 'r+')
lineas = fichero.readlines()
# Modificando la 2° línea
lineas[1] = 'Esta línea se ha modificado en memoria\n'
# ['Una línea con texto \n', 'Esta línea se ha modificado en memoria\n', ' Tercera línea del fichero'] F
print(lineas)
# Colocando las nuevas líneas al fichero
fichero.seek(0)  # al inicio
fichero.writelines(lineas)
fichero.close()
