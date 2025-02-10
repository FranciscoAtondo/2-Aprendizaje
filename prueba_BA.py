import utileria as util
import bosque_aleatorio as BA
import os
import random

# Fuente = https://archive.ics.uci.edu/dataset/58/lenses
url = "https://archive.ics.uci.edu/static/public/58/lenses.zip"
archivo = "datos/lentes.zip"
archivo_datos = "datos/lenses.data"
atributos = ['Lentes', 'Edad', 'Prescripcion', 'Astigmatico', 'Tasa_Tira']

# Descarga datos
if not os.path.exists("datos"):
    os.makedirs("datos")
if not os.path.exists(archivo):
    util.descarga_datos(url, archivo)
    util.descomprime_zip(archivo)

# Cargar los datos
datos = util.lee_csv(
    archivo_datos,
    atributos=atributos,
    separador=","
)

'''
a. Clase de Paciente
    1- Paciente debe tener Lentes Duros
    2- Paciente debe tener Lentes Suaves
    3- Paciente no necesita lentes.
b. Edad
    1- Joven
    2- Pre-Presbicio
    3- Presbicio
c. Prescripcion
    1- Miope
    2- Hipermiope
d. Astigmatico
    1- No
    2- Si
e. Tasa de Tira
    1- Reducido
    2- Normal

for d in datos:
    print(f"Lentes: {d['Lentes']}") # Revision de valores
'''

# Convertir los datos a enteros (si no lo están)
for d in datos:
    for key in atributos:
        d[key] = int(d[key])

target = 'Lentes'
atributos_entrada = ['Edad', 'Prescripcion', 'Astigmatico', 'Tasa_Tira']

