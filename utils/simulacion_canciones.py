import pandas as pd
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# =============================================
# TABLA: CANCIONES
# =============================================

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
        1488408568, 1193701079, 1440806041, 1450695723, 1447566956,
        1544494882, 1510821962, 1440860301, 1544494858, 269572810,
        1458330560, 560097651, 635285084, 1510821890, 1510821945
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

df = pd.DataFrame(datos)


def t(dataframe, fmt='grid'):
    print(tabulate(dataframe, headers='keys', tablefmt=fmt, showindex=False))


def ver_estructura():
    print('\n  ESTRUCTURA DE LA TABLA')
    t(pd.DataFrame({
        'Campo': ['id_canciones', 'titulo', 'nombre_artista', 'nombre_genero',
                  'itunes_track_id', 'preview_url', 'portada_url', 'album',
                  'fecha_lanzamiento', 'subido_por', 'activo', 'total_reproduccion', 'fecha_creacion'],
        'Tipo': ['INT (PK)', 'VARCHAR', 'VARCHAR', 'VARCHAR', 'INT', 'VARCHAR', 'VARCHAR',
                 'VARCHAR', 'DATE', 'INT (FK)', 'BIT', 'INT', 'DATETIME'],
        'Descripcion': [
            'ID unico de la cancion', 'Nombre de la cancion', 'Artista o banda',
            'Genero musical', 'ID en iTunes', 'URL preview 30s', 'URL portada',
            'Nombre del album', 'Fecha lanzamiento', 'Admin que la subio',
            'Disponible o no', 'Contador reproducciones', 'Fecha registro en sistema'
        ]
    }))


def ver_datos():
    print('\n  DATOS SIMULADOS')
    vista = df[['id_canciones', 'titulo', 'nombre_artista', 'nombre_genero', 'album', 'total_reproduccion', 'activo']].copy()
    t(vista)
    print(f'\n  Total canciones: {len(df)}')


def ver_tipos_y_forma():
    print('\n  FORMA DEL DATAFRAME (df.shape)')
    t(pd.DataFrame({'Filas': [df.shape[0]], 'Columnas': [df.shape[1]]}))
    print('\n  TIPOS DE DATOS (df.dtypes)')
    t(df.dtypes.reset_index().rename(columns={'index': 'Columna', 0: 'Tipo'}))


def ver_describe():
    print('\n  ESTADISTICAS DE REPRODUCCIONES (df.describe, mean, median, std, var)')
    t(pd.DataFrame({
        'Metrica': ['count', 'mean', 'median', 'std', 'var', 'min', 'max', 'rango', 'suma'],
        'Valor': [
            len(df),
            f'{df["total_reproduccion"].mean():.2f}',
            f'{df["total_reproduccion"].median():.2f}',
            f'{df["total_reproduccion"].std():.2f}',
            f'{df["total_reproduccion"].var():.2f}',
            df['total_reproduccion'].min(),
            df['total_reproduccion'].max(),
            df['total_reproduccion'].max() - df['total_reproduccion'].min(),
            f'{df["total_reproduccion"].sum():,}'
        ]
    }))


def ver_nulos():
    print('\n  VALORES NULOS (df.isnull().sum())')
    nulos = df.isnull().sum().reset_index().rename(columns={'index': 'Columna', 0: 'Nulos'})
    t(nulos)


def ver_distribucion():
    print('\n  DISTRIBUCION POR GENERO (value_counts)')
    vc = df['nombre_genero'].value_counts().reset_index()
    vc.columns = ['Genero', 'Cantidad']
    vc['Porcentaje'] = (vc['Cantidad'] / len(df) * 100).map(lambda x: f'{x:.1f}%')
    t(vc)
    print('\n  CANCIONES POR ARTISTA (value_counts)')
    va = df['nombre_artista'].value_counts().reset_index()
    va.columns = ['Artista', 'Canciones']
    t(va)


def ver_rankings():
    print('\n  TOP 5 MAS REPRODUCIDAS (df.nlargest)')
    t(df.nlargest(5, 'total_reproduccion')[['titulo', 'nombre_artista', 'nombre_genero', 'total_reproduccion']])
    print('\n  5 MENOS REPRODUCIDAS (df.nsmallest)')
    t(df.nsmallest(5, 'total_reproduccion')[['titulo', 'nombre_artista', 'nombre_genero', 'total_reproduccion']])


def ver_agrupaciones():
    print('\n  REPRODUCCIONES POR GENERO (df.groupby + agg)')
    repro = df.groupby('nombre_genero')['total_reproduccion'].agg(['sum', 'mean', 'count']).reset_index()
    repro.columns = ['Genero', 'Total', 'Promedio', 'Canciones']
    repro['Promedio'] = repro['Promedio'].map(lambda x: f'{x:.0f}')
    t(repro.sort_values('Total', ascending=False))
    print('\n  CANCIONES POR ADMIN QUE LAS SUBIO (df.groupby)')
    admin = df.groupby('subido_por').agg(
        Canciones=('id_canciones', 'count'),
        Reproducciones=('total_reproduccion', 'sum'),
        Promedio=('total_reproduccion', 'mean')
    ).reset_index().rename(columns={'subido_por': 'Admin ID'})
    admin['Promedio'] = admin['Promedio'].map(lambda x: f'{x:.0f}')
    t(admin)


def ver_filtrados():
    print('\n  CANCIONES CON MAS DE 1500 REPRODUCCIONES (df.query)')
    t(df.query('total_reproduccion > 1500')[['titulo', 'nombre_artista', 'total_reproduccion']])
    print('\n  CANCIONES DE ROCK (filtro booleano)')
    t(df[df['nombre_genero'] == 'Rock'][['titulo', 'nombre_artista', 'album', 'total_reproduccion']])
    print(f'\n  Activas: {df["activo"].sum()} | Inactivas: {(~df["activo"]).sum()}')


def ver_temporal():
    print('\n  CANCIONES POR DECADA (dt.year + groupby)')
    temp = df.copy()
    temp['decada'] = (temp['fecha_lanzamiento'].dt.year // 10) * 10
    dec = temp.groupby('decada').agg(Canciones=('id_canciones', 'count'), Promedio_repro=('total_reproduccion', 'mean')).reset_index()
    dec.columns = ['Decada', 'Canciones', 'Promedio Repro']
    dec['Promedio Repro'] = dec['Promedio Repro'].map(lambda x: f'{x:.0f}')
    t(dec)
    print('\n  CORRELACION ANTIGUEDAD vs REPRODUCCIONES (df.corr)')
    antiguedad = (pd.Timestamp('2026-04-15') - df['fecha_lanzamiento']).dt.days / 365.25
    corr = antiguedad.corr(df['total_reproduccion'])
    t(pd.DataFrame({'Metrica': ['Pearson'], 'Valor': [f'{corr:.4f}'], 'Interpretacion': ['Negativa = mas nuevas tienen mas repros']}))
    print('\n  ALBUMS (df.nunique + value_counts)')
    alb = df['album'].value_counts().reset_index()
    alb.columns = ['Album', 'Canciones']
    t(alb)


opciones = {
    '1': ('Estructura de la tabla', ver_estructura),
    '2': ('Datos simulados', ver_datos),
    '3': ('Forma y tipos (shape, dtypes)', ver_tipos_y_forma),
    '4': ('Estadisticas (describe, mean, median, std, var)', ver_describe),
    '5': ('Valores nulos (isnull)', ver_nulos),
    '6': ('Distribucion genero/artista (value_counts)', ver_distribucion),
    '7': ('Rankings top/bottom 5 (nlargest, nsmallest)', ver_rankings),
    '8': ('Agrupaciones genero/admin (groupby, agg)', ver_agrupaciones),
    '9': ('Filtrados (query, filtro booleano)', ver_filtrados),
    '10': ('Temporal y correlacion (corr, dt)', ver_temporal),
}

while True:
    print()
    print('  CANCIONES - Analisis disponibles')
    print('  ' + '-' * 50)
    for key, (nombre, _) in opciones.items():
        print(f'  {key}. {nombre}')
    print(f'  0. Ver todo')
    print(f'  s. Salir')

    opcion = input('\n  Selecciona: ').strip().lower()

    if opcion == 's':
        break
    elif opcion == '0':
        for _, (_, func) in opciones.items():
            func()
    elif opcion in opciones:
        opciones[opcion][1]()
    else:
        print('  Opcion no valida.')

    input('\n  Enter para continuar...')
