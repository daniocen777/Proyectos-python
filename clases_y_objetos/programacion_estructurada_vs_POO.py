''' Ejemplo de programación estructurada '''
''' clientes = [{'Nombre': 'Héctor', 'Apellidos': 'Peña Cabrera', 'dni': '34433333'},
            {'Nombre': 'María', 'Apellidos': 'Llena es de Gracia', 'dni': '11111111'}] '''


''' def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c['dni']):
            print('{} {}'.format(c['Nombre'], c['Apellidos']))
            return
    print('Cliente NO encontrado') '''


''' mostrar_cliente(clientes, '11111111') '''
''' result = [(0, {'Nombre': 'Héctor', 'Apellidos': 'Peña Cabrera', 'dni': '34433333'}), (1, {'Nombre': 'María', 'Apellidos': 'Llena es de Gracia', 'dni': '11111111'})] '''
''' print(list(enumerate(clientes))) '''

# ELiminar
''' def borrar_cliente(clientes, dni):
    for i, c in enumerate(clientes):
        if (dni == c['dni']):
            del clientes[i]
            print('Cliente', c['Nombre'], 'eliminado')
            return
    print('Usuario no encontrado')

borrar_cliente(clientes,'11111111')
print(clientes) '''

''' Ejemplo de POO '''
class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)

class Empresa:
    def __init__(self, clientes = []):
        self.clientes = clientes
    
    def mostrar_cliente_poo(self, dni):
        for c in self.clientes:
            if (dni == c.dni):
                print(c)
                return
        print('No se ha encontrado cliente')
    
    def eliminar_cliente(self, dni):
        for i, c in enumerate(self.clientes):
            if (dni == c.dni):
                del (self.clientes[i])
                print(str(c), '> eliminado')
                return
        print('No se ha encontrado cliente')

mario = Cliente(nombre='Mario', apellidos='Pérez Gómez', dni='11111111')
lucia = Cliente('22222222', 'Lucía', 'Carranza Peña')

empresa = Empresa(clientes=[mario, lucia])
empresa.mostrar_cliente_poo('22222222')