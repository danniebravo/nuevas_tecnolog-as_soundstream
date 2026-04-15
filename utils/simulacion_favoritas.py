import pandas as pd
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# =============================================
# TABLA: CANCIONES_FAVORITAS (Pivote N:M)
# =============================================

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

df = pd.DataFrame(datos)


def t(dataframe, fmt='grid'):
    print(tabulate(dataframe, headers='keys', tablefmt=fmt, showindex=False))


def ver_estructura():
    print('\n  ESTRUCTURA DE LA TABLA')
    t(pd.DataFrame({
        'Campo': ['id_usuario', 'id_cancion', 'fecha_me_gusta'],
        'Tipo': ['INT (PK, FK)', 'INT (PK, FK)', 'DATETIME'],
        'Descripcion': ['Usuario que marco favorito', 'Cancion marcada', 'Fecha y hora del me gusta']
    }))

def ver_datos():
    print('\n  DATOS SIMULADOS')
    vista = df.copy()
    vista['fecha_me_gusta'] = vista['fecha_me_gusta'].dt.strftime('%Y-%m-%d %H:%M')
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
    info = pd.DataFrame({'Columna': df.columns, 'Nulos': df.isnull().sum().values, 'Unicos': df.nunique().values})
    t(info)

def ver_rankings():
    print('\n  CANCIONES MAS GUSTADAS (value_counts)')
    vc = df['id_cancion'].value_counts().reset_index()
    vc.columns = ['ID Cancion', 'Likes']
    t(vc)
    print('\n  USUARIOS CON MAS FAVORITAS (value_counts)')
    vu = df['id_usuario'].value_counts().reset_index()
    vu.columns = ['ID Usuario', 'Favoritas']
    t(vu)

def ver_agrupaciones():
    print('\n  ESTADISTICAS POR USUARIO (df.groupby + agg)')
    grupo = df.groupby('id_usuario').agg(
        Total=('id_cancion', 'count'),
        Primer_like=('fecha_me_gusta', 'min'),
        Ultimo_like=('fecha_me_gusta', 'max')
    ).reset_index()
    grupo['Primer_like'] = grupo['Primer_like'].dt.strftime('%Y-%m-%d')
    grupo['Ultimo_like'] = grupo['Ultimo_like'].dt.strftime('%Y-%m-%d')
    grupo.columns = ['ID Usuario', 'Total', 'Primer Like', 'Ultimo Like']
    t(grupo)
    sizes = df.groupby('id_usuario').size()
    print(f'\n  Promedio por usuario: {sizes.mean():.2f} | Max: {sizes.max()} | Min: {sizes.min()}')

def ver_temporal():
    print('\n  LIKES POR MES (dt.month_name)')
    meses = df['fecha_me_gusta'].dt.month_name().value_counts().reset_index()
    meses.columns = ['Mes', 'Likes']
    t(meses)
    print('\n  HORA MAS COMUN PARA DAR LIKE (dt.hour)')
    horas = df['fecha_me_gusta'].dt.hour.value_counts().reset_index()
    horas.columns = ['Hora', 'Likes']
    t(horas.head())

def ver_crosstab():
    print('\n  TABLA CRUZADA: USUARIO vs CANCION (pd.crosstab)')
    cross = pd.crosstab(df['id_usuario'], df['id_cancion'])
    cross = cross.reset_index().rename(columns={'id_usuario': 'Usuario \\ Cancion'})
    t(cross)

opciones = {
    '1': ('Estructura de la tabla', ver_estructura),
    '2': ('Datos simulados', ver_datos),
    '3': ('Forma y tipos (shape, dtypes)', ver_tipos_y_forma),
    '4': ('Estadisticas descriptivas (describe)', ver_describe),
    '5': ('Valores nulos y unicos (isnull, nunique)', ver_nulos),
    '6': ('Rankings canciones/usuarios (value_counts)', ver_rankings),
    '7': ('Agrupaciones por usuario (groupby, agg)', ver_agrupaciones),
    '8': ('Analisis temporal (dt.month_name, dt.hour)', ver_temporal),
    '9': ('Tabla cruzada (pd.crosstab)', ver_crosstab),
}

while True:
    print()
    print('  CANCIONES_FAVORITAS - Analisis disponibles')
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
