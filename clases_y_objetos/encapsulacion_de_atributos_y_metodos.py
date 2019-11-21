class Ejemplo:
    __atributo_privado = 'Inalcanzable desde fuera'

    def __metodo_privado(self):
        print('Método inalcanzable desde fuera')
    
    def atributo_publico(self):
        return self.__atributo_privado

ejemplo = Ejemplo()
print(ejemplo.atributo_publico())
