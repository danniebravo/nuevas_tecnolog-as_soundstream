import pandas as pd

def limpiar_simulacion(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #Rutina para evaluar textos
    #seleccionar todas las columnas de tipo texto y eliminar sus espacios y poner todo en minuscula
    columnas_texto=["servicio","codigo"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip().str.lower()

    #limpiar los textos solo con valores esperados
    servicios_esperados=["esterilizacion","corte uñas","vacunacion"]
    data_frame_limpio["servicio"]=data_frame_limpio["servicio"].where(
        data_frame_limpio["servicio"].isin(servicios_esperados),
        pd.NA
    )    

    #rutina para evaluar numeros
    #evaluar que las columnas numericas si son numeros
    data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])
    data_frame_limpio["costo"]=pd.to_numeric(data_frame_limpio["costo"])

    #evaluar solo valores numericos permitidos
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["costo"]>100000]

    #rutina para evaluar fechas
    #evaluemos que una fecha si es una fecha
    data_frame_limpio["fecha"]=pd.to_datetime(data_frame_limpio["fecha"])

    #reemplazar una fecha por defecto si el campo llega vacio
    fecha_default=pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha"]=data_frame_limpio["fecha"].fillna(fecha_default)

    #rutina para evalaur novedades
    #rutina para evalaur campos obligatorios que vienen vacios
    columnas_obligatorias=["id","servicio","costo","codigo"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio
