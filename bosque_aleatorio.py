import random
import math
from collections import Counter
from arboles_numericos import entrena_arbol, predice_arbol

def entrena_bosqueA(datos, M, target, clase_default,
                    max_profundidad=None, acc_nodo=1.0, min_ejemplos=0,
                    variables_seleccionadas=None):
    """
    Entrena un árbol de desición aleatorio.
    
    1. Separar los datos en subconjuntos con selección aleatoria con repetición 
      (para `M` subconjuntos).
   2. Por cada subconjunto, entrenar un árbol con un número limitado de variables en cada 
      nodo. Un bosque se puede representar como una lista de nodos raíz (árboles).
   3. Una función para poder hacer predicciones a partir del bosque (lista de nodos raíz).
    
    """
    # Genera subconjuntos con muestras de repeticion
    subconjuntos = [random.choices(datos, k=len(datos)) for _ in range(M)]
    # Cada arbol es entrenado con su propio subconjunto
    bosque = [
        entrena_arbol(subset, target, clase_default,
                      max_profundidad, acc_nodo, min_ejemplos, variables_seleccionadas)
        for subset in subconjuntos
    ]
    return bosque

def predice_bosque(bosque, datos):
    """
    Predice la clase de cada instancia utilizando el bosque mediante votación mayoritaria.

    Parámetros:
    -----------
    bosque: list
        Lista de árboles entrenados.
    datos: list(dict)
        Lista de instancias a predecir.

    Regresa:
    --------
    predicciones: list
        Lista con la clase predicha para cada instancia.
    """
    predicciones = [predice_arbol(arbol, datos) for arbol in bosque]
    predicciones_transpuestas = list(zip(*predicciones))

    # Votación mayoritaria
    return [Counter(pred).most_common(1)[0][0] for pred in predicciones_transpuestas]

def evalua_bosque(bosque, datos, target):
    """
    Evalúa la precisión del bosque en los datos de prueba.

    Parámetros:
    -----------
    bosque: list
        Lista de árboles entrenados.
    datos: list(dict)
        Lista de instancias a evaluar.
    target: str
        Nombre del atributo objetivo.

    Regresa:
    --------
    exactitud: float
        Precisión del modelo en los datos de prueba.
    """
    predicciones = predice_bosque(bosque, datos)
    return sum(1 for p, d in zip(predicciones, datos) if p == d[target]) / len(datos)
    
   
# Prueba del bosque aleatorio
def main():
    datos = [
        {"atributo1": 1, "atributo2": 1, "clase": "positiva"},
        {"atributo1": 2, "atributo2": 1, "clase": "positiva"},
        {"atributo1": 3, "atributo2": 1, "clase": "positiva"},
        {"atributo1": 4, "atributo2": 1, "clase": "positiva"},
        {"atributo1": 1, "atributo2": 2, "clase": "positiva"},
        {"atributo1": 2, "atributo2": 2, "clase": "positiva"},
        {"atributo1": 3, "atributo2": 2, "clase": "positiva"},
        {"atributo1": 4, "atributo2": 2, "clase": "positiva"},
        {"atributo1": 1, "atributo2": 3, "clase": "negativa"},
        {"atributo1": 2, "atributo2": 3, "clase": "negativa"},
        {"atributo1": 3, "atributo2": 3, "clase": "negativa"},
        {"atributo1": 4, "atributo2": 3, "clase": "negativa"},
        {"atributo1": 1, "atributo2": 4, "clase": "positiva"},
        {"atributo1": 2, "atributo2": 4, "clase": "positiva"},
        {"atributo1": 3, "atributo2": 4, "clase": "positiva"},
        {"atributo1": 4, "atributo2": 4, "clase": "positiva"},
    ]

    M = 5  # Número de árboles en el bosque
    bosque = entrena_bosqueA(datos, M, "clase", "positiva")

    # Evaluación
    acc = evalua_bosque(bosque, datos, "clase")
    print(f"Precisión del bosque en los datos de entrenamiento: {acc:.2f}")

if __name__ == "__main__":
    main()