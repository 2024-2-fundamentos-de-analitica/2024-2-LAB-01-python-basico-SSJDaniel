"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
      with open("files/input/data.csv", "r") as f:
      
        data = f.readlines()

      month_counts = {}
      for line in data:
          parts = line.strip().split("\t")
          date = parts[2]
          month = date.split("-")[1]
          if month in month_counts:
              month_counts[month] += 1
          else:
              month_counts[month] = 1

      result = sorted((month, month_counts[month]) for month in sorted(month_counts))
      return result
print(pregunta_04())        
"""
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
