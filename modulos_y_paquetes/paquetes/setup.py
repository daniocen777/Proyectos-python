from setuptools import setup
setup(
    name="paquete",
    version="0.1",
    description="Este es un paquete de ejemplo",
    author="danicode",
    author_email="danicode@gmail.com",
    url="http://danicode.com",
    scripts=[],
    packages=["paquete", "paquete.adios", "paquete.hola"]
)

# python setup.py sdist
# Para instalar el paquete en otro lado, ir a dist:
''' pip3 install nombre-paquete.zip '''
# Consultar todos los paquetes instalados
''' pip3 list '''  ''' pip list '''