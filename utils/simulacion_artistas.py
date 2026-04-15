import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 40)

# =============================================
# TABLA: ARTISTAS (derivada de canciones)
# =============================================
# Artistas extraidos del campo nombre_artista de la tabla canciones.
# En el diagrama ER actual no es tabla independiente pero se puede
# derivar para analisis y en futuras iteraciones normalizarse.

# Datos de canciones necesarios para derivar artistas
canciones_data = {
    'id_canciones': list(range(1, 16)),
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
    'total_reproduccion': [
        1520, 2340, 890, 1100, 3200, 1780, 960, 2100,
        1450, 1890, 750, 1300, 2800, 680, 0
    ]
}

df_canciones = pd.DataFrame(canciones_data)

# Derivar tabla artistas
df_artistas = df_canciones.groupby('nombre_artista').agg(
    total_canciones=('id_canciones', 'count'),
    total_reproducciones=('total_reproduccion', 'sum'),
    generos=('nombre_genero', lambda x: ', '.join(x.unique()))
).reset_index()

df_artistas.insert(0, 'id_artista', range(1, len(df_artistas) + 1))
df_artistas = df_artistas.rename(columns={'nombre_artista': 'nombre'})

# --- Descripcion de la estructura ---
descripcion = pd.DataFrame({
    'Campo': ['id_artista', 'nombre', 'total_canciones', 'total_reproducciones', 'generos'],
    'Tipo': ['INT (PK)', 'VARCHAR', 'INT', 'INT', 'VARCHAR'],
    'Descripcion': [
        'Identificador unico del artista',
        'Nombre del artista o banda',
        'Cantidad de canciones en la plataforma',
        'Suma total de reproducciones',
        'Generos musicales del artista'
    ]
})

# --- Mostrar resultados ---
print('=' * 70)
print('TABLA: ARTISTAS (derivada de canciones)')
print('=' * 70)

print('\nEstructura de la tabla:')
print(descripcion.to_string(index=False))

print(f'\nTotal artistas: {len(df_artistas)}')
print(f'Total reproducciones globales: {df_artistas["total_reproducciones"].sum():,}')

print('\nDatos simulados (ordenados por reproducciones):')
print(df_artistas.sort_values('total_reproducciones', ascending=False).to_string(index=False))
