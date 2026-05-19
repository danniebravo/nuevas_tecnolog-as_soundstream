import pandas as pd

from notebook.consumo import consumir_servicios
from notebook.limpieza import limpiar_datos
from notebook.transformacion import transformar_datos
from notebook.graficacion import graficar_lineas, graficar_barras, graficar_torta, graficar_mapa_calor

datos_tabla_servicios=consumir_servicios()
data_frame_servicios=pd.DataFrame(datos_tabla_servicios)
data_frame_limpio_servicios=limpiar_datos(data_frame_servicios)
agrupaciones=transformar_datos(data_frame_limpio_servicios)

# Gráfico de líneas: esterilizaciones por fecha
graficar_lineas(
    agrupaciones["agrupacion1"],
    columna_eje_x="fecha",
    columna_eje_y="conteo",
    titulo="Esterilizaciones por fecha",
    color_linea="#2196F3",
    nombre_archivo="lineas_esterilizaciones.png"
)

# Gráfico de barras: servicios con costo >= 250.000
graficar_barras(
    agrupaciones["agrupacion2"],
    columna_categorias="servicio",
    columna_valores="conteo",
    titulo="Servicios con costo mayor o igual a 250.000",
    color_barras="#4CAF50",
    nombre_archivo="barras_servicios.png"
)

# Gráfico de torta: proporción de servicios costosos
graficar_torta(
    agrupaciones["agrupacion2"],
    columna_etiquetas="servicio",
    columna_valores="conteo",
    titulo="Proporción de servicios con costo alto",
    nombre_archivo="torta_servicios.png"
)

# Mapa de calor: cantidad de registros por servicio vs código
graficar_mapa_calor(
    agrupaciones["agrupacion3"],
    columna_filas="servicio",
    columna_columnas="codigo",
    columna_valores="conteo",
    titulo="Cantidad de servicios por tipo y código",
    paleta_color="YlOrRd",
    nombre_archivo="mapa_calor_servicio_codigo.png"
)
