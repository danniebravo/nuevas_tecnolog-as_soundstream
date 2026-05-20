import pandas as pd
from notebook.consumo import consumir_servicios
from notebook.limpieza import limpiar_datos
from notebook.descripcion import describir_datos
from notebook.transformacion import transformar_datos
from notebook.graficacion import (
    graficar_lineas,
    graficar_barras,
    graficar_torta,
    graficar_mapa_calor
)

def ejecutar_analisis():
    # 1. Consumo
    print("→ Consumiendo datos...")
    datos_crudos = consumir_servicios(500)
    data_frame = pd.DataFrame(datos_crudos)

    # 2. Limpieza
    print("→ Limpiando datos...")
    data_frame_limpio = limpiar_datos(data_frame)

    # 3. Descripción
    print("→ Describiendo dataset...")
    describir_datos(data_frame_limpio)

    # 4. Transformación
    print("→ Transformando datos...")
    resultados = transformar_datos(data_frame_limpio)

    # 5. Graficación
    print("→ Generando gráficos...")

    graficar_lineas(
        resultados["agrupacion1"],
        columna_eje_x="fecha",
        columna_eje_y="conteo",
        titulo="Reproducciones de Bohemian Rhapsody por fecha",
        nombre_archivo="lineas_bohemian_por_fecha.png"
    )

    graficar_barras(
        resultados["agrupacion2"],
        columna_categorias="artistName",
        columna_valores="conteo",
        titulo="Total de reproducciones por artista",
        nombre_archivo="barras_reproducciones_por_artista.png"
    )

    graficar_torta(
        resultados["agrupacion3"],
        columna_etiquetas="trackName",
        columna_valores="minutos_totales",
        titulo="Distribución de minutos totales escuchados por canción",
        nombre_archivo="torta_minutos_por_cancion.png"
    )

    graficar_barras(
        resultados["agrupacion4"],
        columna_categorias="artistName",
        columna_valores="conteo",
        titulo="Reproducciones de canciones largas (más de 4 min) por artista",
        color_barras="#9C27B0",
        nombre_archivo="barras_canciones_largas_por_artista.png"
    )

    graficar_mapa_calor(
        resultados["agrupacion5"],
        columna_filas="artistName",
        columna_columnas="trackName",
        columna_valores="conteo",
        titulo="Mapa de calor: artista vs canción",
        nombre_archivo="mapa_calor_artista_cancion.png"
    )

    print("\n✓ Análisis completado.")
    print("✓ Gráficos guardados en: Sound_Stream/src/assets/graficos/")

if __name__ == "__main__":
    ejecutar_analisis()