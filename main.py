import pandas as pd

#zona para importar simulaciones
from utils.simulacion import generar_simulacion

#zona para importar limpiezas
from notebook.limpieza import limpiar_datos

#Creando las simulaciones
simulaciones=generar_simulacion(10)

#Ordenando las simulaciones
simulaciones_ordenadas=pd.DataFrame(simulaciones)

#limpiando el set de datos
simulaciones_limpias=limpiar_datos(simulaciones_ordenadas)
print(simulaciones_limpias)
