import pandas as pd

from utils.simulacion import generar_simulacion

from notebook.limpieza import limpiar_simulacion

simulaciones=generar_simulacion(10)

simulaciones_ordenadas=pd.DataFrame(simulaciones)

simulaciones_limpias=limpiar_simulacion(simulaciones_ordenadas)
print(simulaciones_limpias)