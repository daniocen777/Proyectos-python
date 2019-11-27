from io import open

texto = 'Una línea con texto \n Otra línea con texto'
# Creando fichero (open('nombre_fichero', 'modos'))
fichero = open('fichero.txt', 'w')
fichero.write(texto)
fichero.close()  # Simpre se debe cerrar para guardar los cambios
''' del(fichero) '''
''' Modo lectura '''
fichero = open('fichero.txt', 'r')
texto = fichero.read()
fichero.close()
''' Una línea con texto
 Otra línea con texto '''
print(texto)
''' del(fichero) '''
''' Leer líneas '''
fichero = open('fichero.txt', 'r')
lineas = fichero.readlines()
fichero.close()
print(lineas)  # ['Una línea con texto \n', ' Otra línea con texto']
''' Extender el fichero (colocar otra línea al final) => Modo: a => append'''
fichero = open('fichero.txt', 'a')
fichero.write('\n Tercera línea del fichero')
fichero.close()
''' Leer las líneas '''
''' Una línea con texto

 Otra línea con texto

 Tercera línea del fichero '''
with open('fichero.txt', 'r') as fichero:
    for linea in fichero:
        print(linea)
