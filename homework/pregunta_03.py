"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    with open("files/input/data.csv", "r") as f:
        data = f.readlines()
    sums = {}
    for line in data:
        parts = line.strip().split("\t")
        letter = parts[0]
        number = int(parts[1])
        if letter in sums:
            sums[letter] += number
        else:
            sums[letter] = number

    result = sorted((letter, sums[letter]) for letter in sums)
    return result
print(pregunta_03())
"""
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
