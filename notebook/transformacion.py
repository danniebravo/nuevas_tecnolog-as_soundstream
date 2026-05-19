import pandas as pd

def transformar_datos(data_frame_limpio):

    #transformacion 1 (servicios por fecha)
    filtro1=data_frame_limpio.query("servicio=='esterilizacion'")
    agrupacion1=filtro1.groupby("fecha")["id"].count().reset_index(name="conteo")

    #transformacion 2 (servicios por costo)
    filtro2=data_frame_limpio.query("costo>=250000")
    agrupacion2=filtro2.groupby("servicio")["id"].count().reset_index(name="conteo")

    #transformacion 3 (servicio vs codigo para mapa de calor)
    filtro3=data_frame_limpio.query("costo>=150000")
    agrupacion3=filtro3.groupby(["servicio","codigo"])["id"].count().reset_index(name="conteo")

    agrupacion_resumen={
        "agrupacion1":agrupacion1,
        "agrupacion2":agrupacion2,
        "agrupacion3":agrupacion3
    }

    return agrupacion_resumen