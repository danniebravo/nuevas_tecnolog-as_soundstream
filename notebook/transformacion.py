import pandas as pd

def transformar_datos(data_frame_limpio):

    # transformación 1: cantidad de reproducciones de 'bohemian rhapsody' por fecha (para gráfico de líneas)
    filtro1 = data_frame_limpio.query("trackName == 'bohemian rhapsody'")
    agrupacion1 = filtro1.groupby("fecha")["id"].count().reset_index(name="conteo")

    # transformación 2: cantidad de reproducciones por artista (para gráfico de barras)
    filtro2 = data_frame_limpio.copy()
    agrupacion2 = filtro2.groupby("artistName")["id"].count().reset_index(name="conteo")

    # transformación 3: suma total de duración (en minutos) por canción (para gráfico de torta)
    filtro3 = data_frame_limpio.copy()
    filtro3["minutos"] = filtro3["trackTimeMillis"] / 60000
    agrupacion3 = filtro3.groupby("trackName")["minutos"].sum().reset_index(name="minutos_totales")

    # transformación 4: solo canciones largas (más de 4 minutos = 240000 ms) por artista (para barras)
    filtro4 = data_frame_limpio.query("trackTimeMillis > 240000")
    agrupacion4 = filtro4.groupby("artistName")["id"].count().reset_index(name="conteo")

    # transformación 5: artista vs canción con conteo (para mapa de calor)
    filtro5 = data_frame_limpio.copy()
    agrupacion5 = filtro5.groupby(["artistName", "trackName"])["id"].count().reset_index(name="conteo")

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4,
        "agrupacion5": agrupacion5
    }

    return agrupacion_resumen