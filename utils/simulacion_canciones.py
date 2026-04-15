import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 40)

# =============================================
# TABLA: CANCIONES
# =============================================
# Catalogo de canciones disponibles en SoundStream.
# Registradas por admins, con datos de la API de iTunes. Preview de 30s.
#
# Relaciones:
# - N:1 con usuarios via subido_por (muchas canciones subidas por un admin)
# - N:M con usuarios via canciones_favoritas
# - N:M con listas_reproduccion via lista_canciones

datos = {
    'id_canciones': list(range(1, 16)),
    'titulo': [
        'Blinding Lights', 'Shape of You', 'Bohemian Rhapsody', 'Bad Guy',
        'Despacito', 'Rolling in the Deep', 'Levitating', 'Uptown Funk',
        'Someone Like You', 'Thriller', 'Hotel California', 'Lose Yourself',
        'Hips Dont Lie', 'Radioactive', 'Counting Stars'
    ],
    'nombre_artista': [
        'The Weeknd', 'Ed Sheeran', 'Queen', 'Billie Eilish',
        'Luis Fonsi', 'Adele', 'Dua Lipa', 'Bruno Mars',
        'Adele', 'Michael Jackson', 'Eagles', 'Eminem',
        'Shakira', 'Imagine Dragons', 'OneRepublic'
    ],
    'nombre_genero': [
        'Pop', 'Pop', 'Rock', 'Pop', 'Reggaeton', 'Pop', 'Pop', 'Funk',
        'Pop', 'Pop', 'Rock', 'Hip-Hop', 'Latin', 'Rock', 'Pop'
    ],
    'itunes_track_id': [
        1488408568, 1193701079, 1440806041, 1450695723,
        1447566956, 1544494882, 1510821962, 1440860301,
        1544494858, 269572810, 1458330560, 560097651,
        635285084, 1510821890, 1510821945
    ],
    'preview_url': [f'https://audio-ssl.itunes.apple.com/preview{i}.m4a' for i in range(1, 16)],
    'portada_url': [f'https://is1-ssl.mzstatic.com/image/thumb{i}.jpg' for i in range(1, 16)],
    'album': [
        'After Hours', 'Divide', 'A Night at the Opera', 'When We All Fall Asleep',
        'Vida', '21', 'Future Nostalgia', 'Uptown Special',
        '21', 'Thriller', 'Hotel California', '8 Mile Soundtrack',
        'Oral Fixation Vol. 2', 'Night Visions', 'Native'
    ],
    'fecha_lanzamiento': pd.to_datetime([
        '2020-03-20', '2017-01-06', '1975-10-31', '2019-03-29', '2017-01-12',
        '2011-01-19', '2020-10-01', '2014-11-10', '2011-01-24', '1982-11-30',
        '1977-02-22', '2002-10-28', '2005-11-28', '2012-10-29', '2013-06-21'
    ]),
    'subido_por': [1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2],
    'activo': [True] * 14 + [False],
    'total_reproduccion': [
        1520, 2340, 890, 1100, 3200, 1780, 960, 2100,
        1450, 1890, 750, 1300, 2800, 680, 0
    ],
    'fecha_creacion': pd.to_datetime([
        '2026-01-20 10:00', '2026-01-20 10:15', '2026-01-21 09:00',
        '2026-01-22 14:30', '2026-01-25 11:00', '2026-02-01 16:20',
        '2026-02-05 13:45', '2026-02-10 10:30', '2026-02-15 09:00',
        '2026-03-01 11:15', '2026-03-05 15:00', '2026-03-10 12:30',
        '2026-03-15 14:00', '2026-03-20 16:45', '2026-04-01 10:00'
    ])
}

df_canciones = pd.DataFrame(datos)

# --- Descripcion de la estructura ---
descripcion = pd.DataFrame({
    'Campo': [
        'id_canciones', 'titulo', 'nombre_artista', 'nombre_genero',
        'itunes_track_id', 'preview_url', 'portada_url', 'album',
        'fecha_lanzamiento', 'subido_por', 'activo', 'total_reproduccion', 'fecha_creacion'
    ],
    'Tipo': [
        'INT (PK)', 'VARCHAR', 'VARCHAR', 'VARCHAR',
        'INT', 'VARCHAR', 'VARCHAR', 'VARCHAR',
        'DATE', 'INT (FK)', 'BIT', 'INT', 'DATETIME'
    ],
    'Descripcion': [
        'Identificador unico de la cancion',
        'Nombre de la cancion',
        'Nombre del artista o banda',
        'Genero musical',
        'ID del track en iTunes',
        'URL del preview de 30s (m4a)',
        'URL de la imagen de portada',
        'Nombre del album',
        'Fecha de lanzamiento original',
        'ID del admin que registro la cancion',
        'Si la cancion esta disponible',
        'Contador de reproducciones',
        'Fecha de registro en el sistema'
    ]
})

# --- Mostrar resultados ---
print('=' * 70)
print('TABLA: CANCIONES')
print('=' * 70)

print('\nEstructura de la tabla:')
print(descripcion.to_string(index=False))

print(f'\nTotal canciones: {len(df_canciones)}')
print(f'Activas: {df_canciones["activo"].sum()} | Inactivas: {(~df_canciones["activo"]).sum()}')
print(f'Total reproducciones: {df_canciones["total_reproduccion"].sum():,}')
print(f'Generos unicos: {df_canciones["nombre_genero"].nunique()}')
print(f'Artistas unicos: {df_canciones["nombre_artista"].nunique()}')

print('\nDatos simulados:')
print(df_canciones.to_string(index=False))

print('\nTop 5 canciones mas reproducidas:')
top5 = df_canciones.nlargest(5, 'total_reproduccion')[['titulo', 'nombre_artista', 'total_reproduccion']]
print(top5.to_string(index=False))

print('\nDistribucion por genero:')
print(df_canciones['nombre_genero'].value_counts())

print('\nEstadisticas de reproducciones:')
print(df_canciones['total_reproduccion'].describe())
