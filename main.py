import pandas as pd
from utils.simulacion import generar_simulacion

simulaciones=generar_simulacion(100000)
simulaciones_ordenadas=pd.DataFrame(simulaciones)
print(simulaciones_ordenadas)