import utileria as util #ut a util
import bosque_aleatorio as BA #ba a BA
import os
import random

# Fuente = https://archive.ics.uci.edu/dataset/58/lenses
url = "https://archive.ics.uci.edu/static/public/58/lenses.zip"
archivo = "datos/lentes.zip"
archivo_datos = "datos/lenses.data"
atributos = ['Lentes'] + [f'feature_{i}' for i in range(1, 24)]

# Descarga datos
if not os.path.exists("datos"):
    os.makedirs("datos")
if not os.path.exists(archivo):
    util.descarga_datos(url, archivo)
    util.descomprime_zip(archivo)


'''

'''
#Extrae datos
datos = util.lee_csv(
    archivo_datos,
    atributos=atributos,
    separador=","
)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for d in datos:
    print(f"Lentes: {d['Lentes']}")  # 👀 Ver qué valores tiene antes de la conversión
    if d['Lentes'] not in alphabet:
        print(f"❌ Valor inesperado en 'Lentes': {d['Lentes']}")
'''
for d in datos:
    d['Lentes'] = alphabet.index(d['Lentes'])
    for i in range(1, 24):
        d[f'feature_{i}'] = float(d[f'feature_{i}'])

# Selecciona los artributos
target = 'Lentes'
atributos = [target] + [f'feature_{i}' for i in range(1, 17)]
'''