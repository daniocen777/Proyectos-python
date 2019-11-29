''' from modulos import * Importar todas las funciones '''
''' saludar()  # Holas, te saludamos desde la función de módulo de saludos '''
''' import modulos
modulos.Saludo() '''
''' from modulos import Saludo  #Importando la clase desde el mismo path
Saludo() '''
''' ----- Desde otro path ------- '''
import sys
sys.path.insert(1, '..')
''' print(sys.path) '''
from modulos import Saludo
Saludo()