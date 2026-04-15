import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 40)

# =============================================
# TABLA: CANCIONES_FAVORITAS (Tabla Pivote N:M)
# =============================================
# Tabla pivote que registra la relacion N:M entre usuarios y canciones.
# Permite a los usuarios marcar canciones como favoritas.
#
# Relaciones:
# - N:1 con usuarios (FK a id_usuario)
# - N:1 con canciones (FK a id_canciones)

datos = {
    'id_usuario': [3, 3, 3, 4, 4, 5, 5, 5, 6, 8, 8, 9, 9, 9, 10, 10, 3, 4, 5, 6],
    'id_cancion':  [1, 5, 9, 2, 8, 3, 11, 14, 1, 5, 12, 1, 6, 7, 4, 10, 7, 13, 1, 5],
    'fecha_me_gusta': pd.to_datetime([
        '2026-02-05 12:00', '2026-02-06 14:30', '2026-02-10 09:15',
        '2026-02-12 16:00', '2026-02-15 20:45', '2026-03-01 11:30',
        '2026-03-02 08:00', '2026-03-05 19:20', '2026-03-10 13:00',
        '2026-03-12 22:30', '2026-03-15 10:00', '2026-03-20 15:45',
        '2026-03-22 17:00', '2026-03-25 12:15', '2026-04-01 09:30',
        '2026-04-02 14:00', '2026-04-05 11:00', '2026-04-06 16:30',
        '2026-04-08 10:45', '2026-04-10 21:00'
    ])
}

df_favoritas = pd.DataFrame(datos)

# --- Descripcion de la estructura ---
descripcion = pd.DataFrame({
    'Campo': ['id_usuario', 'id_cancion', 'fecha_me_gusta'],
    'Tipo': ['INT (PK, FK)', 'INT (PK, FK)', 'DATETIME'],
    'Descripcion': [
        'ID del usuario que marco favorito',
        'ID de la cancion marcada',
        'Fecha y hora del me gusta'
    ]
})

# --- Mostrar resultados ---
print('=' * 70)
print('TABLA: CANCIONES_FAVORITAS (Tabla Pivote N:M)')
print('=' * 70)

print('\nEstructura de la tabla:')
print(descripcion.to_string(index=False))

print(f'\nTotal "me gusta": {len(df_favoritas)}')
print(f'Usuarios que han dado like: {df_favoritas["id_usuario"].nunique()}')
print(f'Canciones con al menos un like: {df_favoritas["id_cancion"].nunique()}')

print('\nDatos simulados:')
print(df_favoritas.to_string(index=False))

print('\nCanciones mas gustadas (por id_cancion):')
print(df_favoritas['id_cancion'].value_counts())

print('\nFavoritas por usuario (por id_usuario):')
print(df_favoritas['id_usuario'].value_counts())

print(f'\nPromedio de favoritas por usuario: {len(df_favoritas) / df_favoritas["id_usuario"].nunique():.2f}')
