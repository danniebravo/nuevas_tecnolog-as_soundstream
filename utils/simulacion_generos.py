import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 40)

# =============================================
# TABLA: GENEROS (derivada de canciones)
# =============================================
# Generos musicales extraidos del campo nombre_genero de la tabla canciones.
# Permite analizar la distribucion de generos en la plataforma.

# Datos de canciones necesarios para derivar generos
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

# Derivar tabla generos
df_generos = df_canciones.groupby('nombre_genero').agg(
    total_canciones=('id_canciones', 'count'),
    total_reproducciones=('total_reproduccion', 'sum'),
    artistas=('nombre_artista', lambda x: ', '.join(x.unique()))
).reset_index()

df_generos.insert(0, 'id_genero', range(1, len(df_generos) + 1))
df_generos = df_generos.rename(columns={'nombre_genero': 'nombre'})

# --- Descripcion de la estructura ---
descripcion = pd.DataFrame({
    'Campo': ['id_genero', 'nombre', 'total_canciones', 'total_reproducciones', 'artistas'],
    'Tipo': ['INT (PK)', 'VARCHAR', 'INT', 'INT', 'VARCHAR'],
    'Descripcion': [
        'Identificador unico del genero',
        'Nombre del genero musical',
        'Cantidad de canciones del genero',
        'Suma de reproducciones del genero',
        'Artistas que pertenecen al genero'
    ]
})

# --- Mostrar resultados ---
print('=' * 70)
print('TABLA: GENEROS (derivada de canciones)')
print('=' * 70)

print('\nEstructura de la tabla:')
print(descripcion.to_string(index=False))

print(f'\nTotal generos: {len(df_generos)}')

print('\nDatos simulados (ordenados por reproducciones):')
print(df_generos.sort_values('total_reproducciones', ascending=False).to_string(index=False))
