import pandas as pd
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# =============================================
# TABLA: ARTISTAS (derivada de canciones)
# =============================================

canciones_data = {
    'id_canciones': list(range(1, 16)),
    'nombre_artista': ['The Weeknd','Ed Sheeran','Queen','Billie Eilish','Luis Fonsi','Adele','Dua Lipa',
        'Bruno Mars','Adele','Michael Jackson','Eagles','Eminem','Shakira','Imagine Dragons','OneRepublic'],
    'nombre_genero': ['Pop','Pop','Rock','Pop','Reggaeton','Pop','Pop','Funk','Pop','Pop','Rock','Hip-Hop','Latin','Rock','Pop'],
    'total_reproduccion': [1520,2340,890,1100,3200,1780,960,2100,1450,1890,750,1300,2800,680,0]
}

df_c = pd.DataFrame(canciones_data)
df = df_c.groupby('nombre_artista').agg(
    total_canciones=('id_canciones','count'), total_reproducciones=('total_reproduccion','sum'),
    generos=('nombre_genero', lambda x: ', '.join(x.unique()))
).reset_index()
df.insert(0, 'id_artista', range(1, len(df)+1))
df = df.rename(columns={'nombre_artista': 'nombre'})


def t(dataframe, fmt='grid'):
    print(tabulate(dataframe, headers='keys', tablefmt=fmt, showindex=False))


def ver_estructura():
    print('\n  ESTRUCTURA DE LA TABLA')
    t(pd.DataFrame({
        'Campo': ['id_artista','nombre','total_canciones','total_reproducciones','generos'],
        'Tipo': ['INT (PK)','VARCHAR','INT','INT','VARCHAR'],
        'Descripcion': ['ID unico','Nombre artista/banda','Canciones en plataforma','Suma reproducciones','Generos musicales']
    }))

def ver_datos():
    print('\n  DATOS SIMULADOS (ordenados por reproducciones)')
    t(df.sort_values('total_reproducciones', ascending=False))
    print(f'\n  Total artistas: {len(df)}')

def ver_tipos_y_forma():
    print('\n  FORMA Y TIPOS (df.shape, df.dtypes)')
    t(pd.DataFrame({'Filas': [df.shape[0]], 'Columnas': [df.shape[1]]}))
    print()
    t(df.dtypes.reset_index().rename(columns={'index': 'Columna', 0: 'Tipo'}))

def ver_describe():
    print('\n  ESTADISTICAS DE REPRODUCCIONES (describe, mean, median, std)')
    t(pd.DataFrame({
        'Metrica': ['count','mean','median','std','min','max','suma'],
        'Valor': [len(df), f'{df["total_reproducciones"].mean():.2f}', f'{df["total_reproducciones"].median():.2f}',
                  f'{df["total_reproducciones"].std():.2f}', df['total_reproducciones'].min(),
                  df['total_reproducciones'].max(), f'{df["total_reproducciones"].sum():,}']
    }))

def ver_rankings():
    print('\n  TOP 5 ARTISTAS (df.nlargest)')
    t(df.nlargest(5, 'total_reproducciones')[['nombre','total_reproducciones','generos']])
    print('\n  ARTISTAS SIN REPRODUCCIONES (filtro)')
    sin = df[df['total_reproducciones']==0][['nombre','generos']]
    if len(sin)>0: t(sin)
    else: print('  Todos tienen reproducciones')

def ver_porcentajes():
    print('\n  PORCENTAJE DE REPRODUCCIONES POR ARTISTA')
    total = df['total_reproducciones'].sum()
    res = df[['nombre','total_reproducciones']].copy()
    res['Porcentaje'] = (res['total_reproducciones']/total*100).map(lambda x: f'{x:.1f}%')
    t(res.sort_values('total_reproducciones', ascending=False))

def ver_promedio():
    print('\n  PROMEDIO REPRODUCCIONES POR CANCION (columna calculada)')
    res = df[['nombre','total_canciones','total_reproducciones']].copy()
    res['Promedio/cancion'] = (res['total_reproducciones']/res['total_canciones']).map(lambda x: f'{x:.0f}')
    t(res.sort_values('total_reproducciones', ascending=False))

def ver_generos():
    print('\n  ARTISTAS POR GENERO (value_counts)')
    vc = df['generos'].value_counts().reset_index(); vc.columns = ['Genero','Artistas']
    t(vc)

opciones = {
    '1': ('Estructura de la tabla', ver_estructura),
    '2': ('Datos simulados', ver_datos),
    '3': ('Forma y tipos (shape, dtypes)', ver_tipos_y_forma),
    '4': ('Estadisticas (describe, mean, median, std)', ver_describe),
    '5': ('Rankings top 5 (nlargest, filtro)', ver_rankings),
    '6': ('Porcentaje de reproducciones', ver_porcentajes),
    '7': ('Promedio por cancion (columna calculada)', ver_promedio),
    '8': ('Distribucion por genero (value_counts)', ver_generos),
}

while True:
    print()
    print('  ARTISTAS - Analisis disponibles')
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
