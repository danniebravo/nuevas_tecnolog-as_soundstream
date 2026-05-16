import pandas as pd

from notebook.consumo import consumir_servicios
from notebook.limpieza import limpiar_datos
from notebook.transformacion import transformar_datos

datos_tabla_servicios=consumir_servicios()
data_frame_servicios=pd.DataFrame(datos_tabla_servicios)
data_frame_limpio_servicios=limpiar_datos(data_frame_servicios)
agrupaciones=transformar_datos(data_frame_limpio_servicios)
print(agrupaciones)






