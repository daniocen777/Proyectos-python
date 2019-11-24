class A:
    def __init__(self):
        print('Soy de la ckase A')

    def a(self):
        print('Este método lo heredo de A')


class B:
    def __init__(self):
        print('Soy de ka ckase B')

    def b(self):
        print('Este método lo heredo de B')


class C(A, B):
    def c(self):
        print('Este método es de C')
    pass


c = C()  # result => Soy de la ckase A (da prioridad a la superclase)
c.a()  # Este método lo heredo de A
c.b()  # Este método lo heredo de B
c.c()  # Este método es de C
