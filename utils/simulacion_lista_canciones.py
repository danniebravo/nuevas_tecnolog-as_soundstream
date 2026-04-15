import pandas as pd
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# =============================================
# TABLA: LISTA_CANCIONES (Pivote N:M)
# =============================================

datos = {
    'id_lista':   [1,1,1,1, 2,2,2, 3,3,3, 4,4,4, 5,5,5, 6,6, 7,7,7, 8,8,8,8],
    'id_cancion': [1,5,9,7, 8,12,14, 6,9,7, 3,11,10, 5,13,8, 1,2, 6,9,7, 3,11,1,14],
    'posicion':   [1,2,3,4, 1,2,3, 1,2,3, 1,2,3, 1,2,3, 1,2, 1,2,3, 1,2,3,4],
    'fecha_agregado': pd.to_datetime([
        '2026-02-05 10:05','2026-02-06 14:35','2026-02-10 09:20','2026-04-05 11:05',
        '2026-02-12 15:35','2026-02-15 20:50','2026-03-05 19:25',
        '2026-02-20 20:05','2026-02-20 20:10','2026-03-25 12:20',
        '2026-03-01 09:05','2026-03-02 08:05','2026-04-12 10:20',
        '2026-03-08 22:20','2026-03-10 13:05','2026-04-11 23:05',
        '2026-03-15 14:05','2026-03-20 16:50',
        '2026-04-01 08:35','2026-04-01 08:40','2026-04-10 09:05',
        '2026-04-05 11:50','2026-04-05 11:55','2026-04-05 12:00','2026-04-10 14:35'
    ])
}

df = pd.DataFrame(datos)


def t(dataframe, fmt='grid'):
    print(tabulate(dataframe, headers='keys', tablefmt=fmt, showindex=False))


def ver_estructura():
    print('\n  ESTRUCTURA DE LA TABLA')
    t(pd.DataFrame({
        'Campo': ['id_lista', 'id_cancion', 'posicion', 'fecha_agregado'],
        'Tipo': ['INT (PK, FK)', 'INT (PK, FK)', 'INT', 'DATETIME'],
        'Descripcion': ['ID de la playlist', 'ID de la cancion', 'Orden en la lista', 'Fecha en que se agrego']
    }))

def ver_datos():
    print('\n  DATOS SIMULADOS')
    vista = df.copy(); vista['fecha_agregado'] = vista['fecha_agregado'].dt.strftime('%Y-%m-%d %H:%M')
    t(vista)
    print(f'\n  Total registros: {len(df)}')

def ver_tipos_y_forma():
    print('\n  FORMA Y TIPOS (df.shape, df.dtypes)')
    t(pd.DataFrame({'Filas': [df.shape[0]], 'Columnas': [df.shape[1]]}))
    print()
    t(df.dtypes.reset_index().rename(columns={'index': 'Columna', 0: 'Tipo'}))

def ver_describe():
    print('\n  ESTADISTICAS DESCRIPTIVAS (df.describe)')
    t(df.describe().reset_index().rename(columns={'index': 'Metrica'}))

def ver_nulos():
    print('\n  VALORES NULOS Y UNICOS (isnull, nunique)')
    t(pd.DataFrame({'Columna': df.columns, 'Nulos': df.isnull().sum().values, 'Unicos': df.nunique().values}))

def ver_agrupaciones():
    print('\n  CANCIONES POR LISTA (df.groupby + agg)')
    grupo = df.groupby('id_lista').agg(Canciones=('id_cancion','count'), Max_pos=('posicion','max')).reset_index()
    grupo.columns = ['ID Lista', 'Canciones', 'Pos. Maxima']
    t(grupo)
    tamanos = df.groupby('id_lista')['id_cancion'].count()
    print(f'\n  Promedio: {tamanos.mean():.2f} | Max: {tamanos.max()} | Min: {tamanos.min()} | Std: {tamanos.std():.2f}')

def ver_rankings():
    print('\n  CANCIONES EN MAS LISTAS (value_counts)')
    vc = df['id_cancion'].value_counts().reset_index(); vc.columns = ['ID Cancion', 'Apariciones']
    t(vc)
    print('\n  DISTRIBUCION DE POSICIONES (value_counts + sort_index)')
    pos = df['posicion'].value_counts().sort_index().reset_index(); pos.columns = ['Posicion', 'Frecuencia']
    t(pos)

def ver_temporal():
    print('\n  AGREGADOS POR MES (dt.month_name)')
    meses = df['fecha_agregado'].dt.month_name().value_counts().reset_index(); meses.columns = ['Mes', 'Agregados']
    t(meses)

def ver_crosstab():
    print('\n  TABLA CRUZADA: LISTA vs CANCION (pd.crosstab)')
    cross = pd.crosstab(df['id_lista'], df['id_cancion']).reset_index().rename(columns={'id_lista': 'Lista \\ Cancion'})
    t(cross)

def ver_compartidas():
    print('\n  CANCIONES COMPARTIDAS ENTRE LISTAS (groupby + nunique)')
    comp = df.groupby('id_cancion')['id_lista'].nunique().reset_index()
    comp.columns = ['ID Cancion', 'En N listas']
    comp = comp[comp['En N listas'] > 1].sort_values('En N listas', ascending=False)
    t(comp)
    print(f'\n  Canciones en mas de 1 lista: {len(comp)}')

opciones = {
    '1': ('Estructura de la tabla', ver_estructura),
    '2': ('Datos simulados', ver_datos),
    '3': ('Forma y tipos (shape, dtypes)', ver_tipos_y_forma),
    '4': ('Estadisticas descriptivas (describe)', ver_describe),
    '5': ('Valores nulos y unicos (isnull, nunique)', ver_nulos),
    '6': ('Agrupaciones por lista (groupby, agg, mean)', ver_agrupaciones),
    '7': ('Rankings y posiciones (value_counts)', ver_rankings),
    '8': ('Analisis temporal (dt.month_name)', ver_temporal),
    '9': ('Tabla cruzada (pd.crosstab)', ver_crosstab),
    '10': ('Canciones compartidas (groupby, nunique)', ver_compartidas),
}

while True:
    print()
    print('  LISTA_CANCIONES - Analisis disponibles')
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
