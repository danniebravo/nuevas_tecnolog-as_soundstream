import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 40)

# =============================================
# TABLA: LISTA_CANCIONES (Tabla Pivote N:M)
# =============================================
# Conecta las playlists con sus canciones.
# Almacena el orden de reproduccion (posicion) de cada cancion en la lista.
#
# Relaciones:
# - N:1 con listas_reproduccion (FK a id_lista)
# - N:1 con canciones (FK a id_canciones)

datos = {
    'id_lista':   [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 8],
    'id_cancion': [1, 5, 9, 7, 8, 12, 14, 6, 9, 7, 3, 11, 10, 5, 13, 8, 1, 2, 6, 9, 7, 3, 11, 1, 14],
    'posicion':   [1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 1, 2, 3, 1, 2, 3, 4],
    'fecha_agregado': pd.to_datetime([
        '2026-02-05 10:05', '2026-02-06 14:35', '2026-02-10 09:20', '2026-04-05 11:05',
        '2026-02-12 15:35', '2026-02-15 20:50', '2026-03-05 19:25',
        '2026-02-20 20:05', '2026-02-20 20:10', '2026-03-25 12:20',
        '2026-03-01 09:05', '2026-03-02 08:05', '2026-04-12 10:20',
        '2026-03-08 22:20', '2026-03-10 13:05', '2026-04-11 23:05',
        '2026-03-15 14:05', '2026-03-20 16:50',
        '2026-04-01 08:35', '2026-04-01 08:40', '2026-04-10 09:05',
        '2026-04-05 11:50', '2026-04-05 11:55', '2026-04-05 12:00', '2026-04-10 14:35'
    ])
}

df_lista_canciones = pd.DataFrame(datos)

# --- Descripcion de la estructura ---
descripcion = pd.DataFrame({
    'Campo': ['id_lista', 'id_cancion', 'posicion', 'fecha_agregado'],
    'Tipo': ['INT (PK, FK)', 'INT (PK, FK)', 'INT', 'DATETIME'],
    'Descripcion': [
        'ID de la lista de reproduccion',
        'ID de la cancion',
        'Orden de la cancion en la lista',
        'Cuando se agrego la cancion'
    ]
})

# --- Mostrar resultados ---
print('=' * 70)
print('TABLA: LISTA_CANCIONES (Tabla Pivote N:M)')
print('=' * 70)

print('\nEstructura de la tabla:')
print(descripcion.to_string(index=False))

print(f'\nTotal registros: {len(df_lista_canciones)}')
print(f'Listas con canciones: {df_lista_canciones["id_lista"].nunique()}')
print(f'Canciones en al menos una lista: {df_lista_canciones["id_cancion"].nunique()}')

print('\nDatos simulados:')
print(df_lista_canciones.to_string(index=False))

print('\nCanciones por lista (id_lista):')
print(df_lista_canciones.groupby('id_lista')['id_cancion'].count().sort_values(ascending=False))

print('\nCanciones que aparecen en mas listas (id_cancion):')
print(df_lista_canciones['id_cancion'].value_counts().head())
