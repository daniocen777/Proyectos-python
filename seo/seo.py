# Auditoría SEO
# Imports #
import urllib.request as request
from urllib.request import urlopen
import os  # Sistema operativo
from bs4 import BeautifulSoup
import re  # Expresiones regulares

# ******************* Verificar https #******************* #
print(" ************AUDITORÍA A 'python.org' ************")
req = request.Request("http://www.python.org/")
resultado = request.urlopen(req)
# Http or Https: https://www.python.org/
print('Http or Https: {}'.format(resultado.geturl()))

# ******************* Peso de la página #******************* #
url = "http://www.python.org/"
print("Url: {}".format(url))
site = request.urlopen(url)
meta = site.info()  # metadata
# Content-length: 49659
print("Content-length: {}".format(site.headers["content-length"]))
# Descargando el sitio
file = open("out.txt", "a")
file.close()
file = open("out.txt", "wb")
file.write(site.read())
site.close()
file.close()
file = open("out.txt", "r")
print("File on disk: {}".format(len(file.read())))  # File on disk: 49725
file.close()
print("Status: {}".format(os.stat("out.txt").st_size))  # Status: 49800

# ******************* Verificar www de la página #******************* #
req = request.Request("http://python.org/")
resultado = request.urlopen(req)
print('Verificar www: {}'.format(resultado.geturl()))

# ******************* Verificar meta description de la página #******************* #
# Import BeautifulSoup
site = request.urlopen("http://python.org/")
soup = BeautifulSoup(site)  # Te da el html
# Dentro de meta (html), buscar la descripción
description = soup.find("meta", attrs={"name": "description"})
print("Tamaño de descripción es: {}".format(
    len(description.get("content"))))  # Tamaño de descripción es: 52
if (len(description.get("content")) < 154):
    print("La descripción es menor a 154")

# ******************* Verificar meta title de la página #******************* #
# Otra manera
html = urlopen("http://python.org")
soup = BeautifulSoup(html.read())
print("El título dice: {}".format(soup.html.head.title.string))
print("El tamaño del título es: {}".format(len(soup.html.head.title.string)))
html.close()

# ******************* Palabras clave #******************* #
site = request.urlopen("http://python.org/")
soup = BeautifulSoup(site)  # Te da el html
keywords = soup.find("meta", attrs={"name": "keywords"})
print("Python keywords:", keywords.get('content'))  # cadena
words = keywords.get("content").split()
print(words)  # ['Python', 'programming', 'language',...]
# Cantidad de veces que se repite la palbra clave => con re (regular expresion)
for word in words:
    print(word, len(soup.findAll(text=re.compile(word))))

# Resultado:
""" Python 59
programming 4
language 5
object 0
oriented 0
web 3
free 0
open 0
source 1
software 0
license 0
documentation 0
download 1
community 2 """

# ******************* Alt en imágenes #******************* #
site = request.urlopen("http://python.org/")
soup = BeautifulSoup(site)  # Te da el html
count = 1
for image in soup.findAll("img"):
    print("Imagen #{}: {}".format(count, image["src"]))
    print("Alt de imagen #{}: {}".format(count, image.get("alt", "None")))
    count += 1
