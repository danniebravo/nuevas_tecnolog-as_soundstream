import pandas as pd

def limpiar_datos(data_frame_sucio):
    
    data_frame_limpio=data_frame_sucio.copy()

    #1. Limpiar las columnas String del DF
    columnas_texto=["codigo","servicio"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip().str.lower()
    
    #1.1 Definir valores de String esperados
    valores_validos_servicios=["esterilizacion","corte uñas","vacunacion"]
    data_frame_limpio["servicio"]=data_frame_limpio["servicio"].where(
        data_frame_limpio["servicio"].isin(valores_validos_servicios),
        pd.NA
    )

    #2. Limpiar las columnas numericas del DF
    data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])
    data_frame_limpio["costo"]=pd.to_numeric(data_frame_limpio["costo"])

    #2.1 Limpiando campos numericos que no tengan valores validos
    data_frame_limpio=data_frame_limpio[data_frame_limpio["costo"]>=100000]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>0]

    #3. Organizar las columnas de tipo fecha
    data_frame_limpio["fecha"]=pd.to_datetime(data_frame_limpio["fecha"])

    #3.1 Si una fecha no viene la reemplazamos por un valor por defecto
    fecha_default=pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha"]=data_frame_limpio["fecha"].fillna(fecha_default)

    #4. Eliminar registros que tengan datos obligatorios vacios
    columnas_obligtorias=["id","servicio","costo","codigo"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligtorias)

    #5. ELiminar registros duplicados
    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio
