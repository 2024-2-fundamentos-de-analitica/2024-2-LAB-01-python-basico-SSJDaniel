"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
def pregunta_12():
    with open("files/input/data.csv", "r") as f:
    #with open('data.csv', 'r') as f:
        data = f.readlines()
    
    result = {}
    
    for line in data:
        parts = line.strip().split("\t")
        key = parts[0]
        values = parts[4].split(",")
        value_sum = sum(int(v.split(":")[1]) for v in values)
        
        if key in result:
            result[key] += value_sum
        else:
            result[key] = value_sum
    
    return result
pregunta_12()
