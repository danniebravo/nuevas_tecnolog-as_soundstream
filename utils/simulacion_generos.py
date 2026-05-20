import pandas as pd
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# =============================================
# TABLA: GENEROS (derivada de canciones)
# =============================================

canciones_data = {
    'id_canciones': list(range(1, 16)),
    'nombre_artista': ['The Weeknd','Ed Sheeran','Queen','Billie Eilish','Luis Fonsi','Adele','Dua Lipa',
        'Bruno Mars','Adele','Michael Jackson','Eagles','Eminem','Shakira','Imagine Dragons','OneRepublic'],
    'nombre_genero': ['Pop','Pop','Rock','Pop','Reggaeton','Pop','Pop','Funk','Pop','Pop','Rock','Hip-Hop','Latin','Rock','Pop'],
    'total_reproduccion': [1520,2340,890,1100,3200,1780,960,2100,1450,1890,750,1300,2800,680,0]
}

df_c = pd.DataFrame(canciones_data)
df = df_c.groupby('nombre_genero').agg(
    total_canciones=('id_canciones','count'), total_reproducciones=('total_reproduccion','sum'),
    artistas=('nombre_artista', lambda x: ', '.join(x.unique()))
).reset_index()
df.insert(0, 'id_genero', range(1, len(df)+1))
df = df.rename(columns={'nombre_genero': 'nombre'})


def t(dataframe, fmt='grid'):
    print(tabulate(dataframe, headers='keys', tablefmt=fmt, showindex=False))


def ver_estructura():
    print('\n  ESTRUCTURA DE LA TABLA')
    t(pd.DataFrame({
        'Campo': ['id_genero','nombre','total_canciones','total_reproducciones','artistas'],
        'Tipo': ['INT (PK)','VARCHAR','INT','INT','VARCHAR'],
        'Descripcion': ['ID unico','Genero musical','Canciones del genero','Suma reproducciones','Artistas del genero']
    }))

def ver_datos():
    print('\n  DATOS SIMULADOS (ordenados por reproducciones)')
    t(df.sort_values('total_reproducciones', ascending=False))
    print(f'\n  Total generos: {len(df)}')

def ver_tipos_y_forma():
    print('\n  FORMA Y TIPOS (df.shape, df.dtypes)')
    t(pd.DataFrame({'Filas': [df.shape[0]], 'Columnas': [df.shape[1]]}))
    print()
    t(df.dtypes.reset_index().rename(columns={'index': 'Columna', 0: 'Tipo'}))

def ver_describe():
    print('\n  ESTADISTICAS (describe, mean, median, std)')
    t(pd.DataFrame({
        'Metrica': ['count','mean','median','std','min','max','suma'],
        'Valor': [len(df), f'{df["total_reproducciones"].mean():.2f}', f'{df["total_reproducciones"].median():.2f}',
                  f'{df["total_reproducciones"].std():.2f}', df['total_reproducciones'].min(),
                  df['total_reproducciones'].max(), f'{df["total_reproducciones"].sum():,}']
    }))

def ver_ranking():
    print('\n  RANKING DE GENEROS (sort_values)')
    rank = df.sort_values('total_reproducciones', ascending=False).reset_index(drop=True)
    rank.insert(0, 'Ranking', range(1, len(rank)+1))
    t(rank[['Ranking','nombre','total_canciones','total_reproducciones']])

def ver_porcentajes():
    print('\n  PORCENTAJE DE REPRODUCCIONES')
    total = df['total_reproducciones'].sum()
    res = df[['nombre','total_reproducciones']].copy()
    res['Porcentaje'] = (res['total_reproducciones']/total*100).map(lambda x: f'{x:.1f}%')
    t(res.sort_values('total_reproducciones', ascending=False))
    print('\n  PORCENTAJE DE CANCIONES')
    total_c = df['total_canciones'].sum()
    res2 = df[['nombre','total_canciones']].copy()
    res2['Porcentaje'] = (res2['total_canciones']/total_c*100).map(lambda x: f'{x:.1f}%')
    t(res2.sort_values('total_canciones', ascending=False))

def ver_promedio():
    print('\n  PROMEDIO REPRODUCCIONES POR CANCION EN CADA GENERO')
    res = df[['nombre','total_canciones','total_reproducciones']].copy()
    res['Promedio/cancion'] = (res['total_reproducciones']/res['total_canciones']).map(lambda x: f'{x:.0f}')
    t(res.sort_values('total_reproducciones', ascending=False))

def ver_artistas():
    print('\n  ARTISTAS POR GENERO (str.split + len)')
    res = df[['nombre','artistas']].copy()
    res['Num. artistas'] = res['artistas'].str.split(', ').str.len()
    t(res.sort_values('Num. artistas', ascending=False))

def ver_dominante():
    print('\n  GENERO DOMINANTE (idxmax)')
    top = df.loc[df['total_reproducciones'].idxmax()]
    total = df['total_reproducciones'].sum()
    t(pd.DataFrame({
        'Dato': ['Nombre','Canciones','Reproducciones','Porcentaje','Artistas'],
        'Valor': [top['nombre'], top['total_canciones'], f'{top["total_reproducciones"]:,}',
                  f'{top["total_reproducciones"]/total*100:.1f}%', top['artistas']]
    }))

opciones = {
    '1': ('Estructura de la tabla', ver_estructura),
    '2': ('Datos simulados', ver_datos),
    '3': ('Forma y tipos (shape, dtypes)', ver_tipos_y_forma),
    '4': ('Estadisticas (describe, mean, median, std)', ver_describe),
    '5': ('Ranking de generos (sort_values)', ver_ranking),
    '6': ('Porcentajes reproducciones/canciones', ver_porcentajes),
    '7': ('Promedio por cancion (columna calculada)', ver_promedio),
    '8': ('Artistas por genero (str.split, len)', ver_artistas),
    '9': ('Genero dominante (idxmax)', ver_dominante),
}

while True:
    print()
    print('  GENEROS - Analisis disponibles')
    print('  ' + '-' * 50)
    for key, (nombre, _) in opciones.items():
        print(f'  {key}. {nombre}')
    print(f'  0. Ver todo')
    print(f'  s. Salir')
    opcion = input('\n  Selecciona: ').strip().lower()
    if opcion == 's': break
    elif opcion == '0':
        for _, (_, func) in opciones.items(): func()
    elif opcion in opciones: opciones[opcion][1]()
    else: print('  Opcion no valida.')
    input('\n  Enter para continuar...')
