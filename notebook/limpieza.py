import pandas as pd

def limpiar_datos(data_frame):
    # Se elimina cualquier fila que tenga campos críticos nulos
    df = data_frame.dropna(subset=["id", "trackName", "trackTimeMillis", "fecha"]).copy()

    # Se filtran solo las canciones reales del catálogo (sin podcasts ni audiolibros)
    canciones_validas = [
        "bohemian rhapsody", "blinding lights", "shape of you",
        "billie jean", "rolling in the deep"
    ]
    df = df[df["trackName"].isin(canciones_validas)]

    # Se elimina cualquier reproducción con duración inválida (cero o negativa)
    df = df[df["trackTimeMillis"] > 0]

    # Se normalizan los nombres de artista: quitar espacios y pasar a minúsculas
    df["artistName"] = df["artistName"].str.strip().str.lower()

    # Se aseguran los tipos de dato
    df["id"] = df["id"].astype(int)
    df["trackTimeMillis"] = df["trackTimeMillis"].astype(int)
    df["fecha"] = pd.to_datetime(df["fecha"])

    # Se ordena por fecha para análisis temporales
    df = df.sort_values("fecha").reset_index(drop=True)

    print(f"Limpieza completada: {len(data_frame)} registros iniciales → {len(df)} válidos")
    return df