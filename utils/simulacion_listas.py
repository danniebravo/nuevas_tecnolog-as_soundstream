import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 40)

# =============================================
# TABLA: LISTAS_REPRODUCCION
# =============================================
# Playlists creadas por los usuarios. Pueden ser publicas o privadas.
# Contienen canciones via tabla intermedia lista_canciones.
#
# Relaciones:
# - N:1 con usuarios (muchas listas pertenecen a un usuario)
# - N:M con canciones via lista_canciones

datos = {
    'id_lista': [1, 2, 3, 4, 5, 6, 7, 8],
    'nombre': [
        'Mis Favoritas', 'Workout Mix', 'Chill Vibes', 'Rock Clasico',
        'Reggaeton Party', 'Pop Hits 2026', 'Para Estudiar', 'Road Trip'
    ],
    'descripcion': [
        'Las canciones que mas me gustan', 'Musica para entrenar',
        'Para relajarse', 'Lo mejor del rock',
        'Puro perreo', 'Los exitos pop del momento',
        None, 'Musica para viajes largos'
    ],
    'url_portada': [
        f'https://img.soundstream.com/pl{i}.jpg' if i not in [3, 6]
        else None for i in range(1, 9)
    ],
    'id_usuario': [3, 4, 3, 5, 8, 9, 10, 4],
    'es_publica': [True, True, False, True, True, False, True, True],
    'fecha_creacion': pd.to_datetime([
        '2026-02-05 10:00', '2026-02-12 15:30', '2026-02-20 20:00',
        '2026-03-01 09:00', '2026-03-08 22:15', '2026-03-15 14:00',
        '2026-04-01 08:30', '2026-04-05 11:45'
    ]),
    'fecha_actualizacion': pd.to_datetime([
        '2026-04-10 18:00', '2026-04-08 07:00', '2026-03-25 21:30',
        '2026-04-12 10:15', '2026-04-11 23:00', '2026-03-20 16:45',
        '2026-04-10 09:00', '2026-04-10 14:30'
    ])
}

df_listas = pd.DataFrame(datos)

# --- Descripcion de la estructura ---
descripcion = pd.DataFrame({
    'Campo': ['id_lista', 'nombre', 'descripcion', 'url_portada',
              'id_usuario', 'es_publica', 'fecha_creacion', 'fecha_actualizacion'],
    'Tipo': ['INT (PK)', 'VARCHAR', 'VARCHAR', 'VARCHAR',
             'INT (FK)', 'BIT', 'DATETIME', 'DATETIME'],
    'Descripcion': [
        'Identificador unico de la lista',
        'Nombre de la playlist',
        'Descripcion opcional',
        'URL de la imagen de portada',
        'Usuario creador de la lista',
        'Si la lista es visible para otros',
        'Fecha de creacion',
        'Ultima modificacion'
    ]
})

# --- Mostrar resultados ---
print('=' * 70)
print('TABLA: LISTAS_REPRODUCCION')
print('=' * 70)

print('\nEstructura de la tabla:')
print(descripcion.to_string(index=False))

print(f'\nTotal listas: {len(df_listas)}')
print(f'Publicas: {df_listas["es_publica"].sum()} | Privadas: {(~df_listas["es_publica"]).sum()}')
print(f'Usuarios con listas: {df_listas["id_usuario"].nunique()}')

print('\nDatos simulados:')
print(df_listas.to_string(index=False))

print('\nValores nulos por columna:')
print(df_listas.isnull().sum())

print('\nListas por usuario (id):')
print(df_listas.groupby('id_usuario')['nombre'].count())
