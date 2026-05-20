import pandas as pd

def describir_datos(data_frame_limpio):
    print("*** DESCRIPCION DEL DATASET ***")
    print(f"Numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"Tipos de dato de cada atributo:\n{data_frame_limpio.dtypes}")

    # Estadísticas (solo aplica para datos numéricos)
    print("\n*** ESTADISTICAS ***")
    print(f"{data_frame_limpio[['id', 'trackTimeMillis']].describe()}")

    # Información de conteos valiosos
    print("\n*** CONTEOS ***")
    print(f"Conteo por canción:\n{data_frame_limpio['trackName'].value_counts()}")
    print(f"\nConteo por artista:\n{data_frame_limpio['artistName'].value_counts()}")

    # Descripción de fechas
    print("\n*** DESCRIPCION DE FECHAS ***")
    print(f"Fecha más antigua: {data_frame_limpio['fecha'].min()}")
    print(f"Fecha más reciente: {data_frame_limpio['fecha'].max()}")