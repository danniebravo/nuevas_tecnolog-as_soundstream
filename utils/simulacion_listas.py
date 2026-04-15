import pandas as pd
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# =============================================
# TABLA: LISTAS_REPRODUCCION
# =============================================

datos = {
    'id_lista': [1, 2, 3, 4, 5, 6, 7, 8],
    'nombre': ['Mis Favoritas', 'Workout Mix', 'Chill Vibes', 'Rock Clasico',
               'Reggaeton Party', 'Pop Hits 2026', 'Para Estudiar', 'Road Trip'],
    'descripcion': ['Las canciones que mas me gustan', 'Musica para entrenar',
                    'Para relajarse', 'Lo mejor del rock', 'Puro perreo',
                    'Los exitos pop del momento', None, 'Musica para viajes largos'],
    'url_portada': [f'https://img.soundstream.com/pl{i}.jpg' if i not in [3, 6] else None for i in range(1, 9)],
    'id_usuario': [3, 4, 3, 5, 8, 9, 10, 4],
    'es_publica': [True, True, False, True, True, False, True, True],
    'fecha_creacion': pd.to_datetime(['2026-02-05 10:00', '2026-02-12 15:30', '2026-02-20 20:00',
        '2026-03-01 09:00', '2026-03-08 22:15', '2026-03-15 14:00', '2026-04-01 08:30', '2026-04-05 11:45']),
    'fecha_actualizacion': pd.to_datetime(['2026-04-10 18:00', '2026-04-08 07:00', '2026-03-25 21:30',
        '2026-04-12 10:15', '2026-04-11 23:00', '2026-03-20 16:45', '2026-04-10 09:00', '2026-04-10 14:30'])
}

df = pd.DataFrame(datos)


def t(dataframe, fmt='grid'):
    print(tabulate(dataframe, headers='keys', tablefmt=fmt, showindex=False))


def ver_estructura():
    print('\n  ESTRUCTURA DE LA TABLA')
    t(pd.DataFrame({
        'Campo': ['id_lista', 'nombre', 'descripcion', 'url_portada', 'id_usuario', 'es_publica', 'fecha_creacion', 'fecha_actualizacion'],
        'Tipo': ['INT (PK)', 'VARCHAR', 'VARCHAR', 'VARCHAR', 'INT (FK)', 'BIT', 'DATETIME', 'DATETIME'],
        'Descripcion': ['ID unico de la lista', 'Nombre de la playlist', 'Descripcion opcional', 'URL portada',
                        'Usuario creador', 'Visible para otros', 'Fecha creacion', 'Ultima modificacion']
    }))

def ver_datos():
    print('\n  DATOS SIMULADOS')
    vista = df[['id_lista', 'nombre', 'id_usuario', 'es_publica']].copy()
    vista['creacion'] = df['fecha_creacion'].dt.strftime('%Y-%m-%d')
    t(vista)

def ver_tipos_y_forma():
    print('\n  FORMA Y TIPOS (df.shape, df.dtypes)')
    t(pd.DataFrame({'Filas': [df.shape[0]], 'Columnas': [df.shape[1]]}))
    print()
    t(df.dtypes.reset_index().rename(columns={'index': 'Columna', 0: 'Tipo'}))

def ver_describe():
    print('\n  ESTADISTICAS DESCRIPTIVAS (df.describe)')
    t(df.describe(include='all').reset_index().rename(columns={'index': 'Metrica'}))

def ver_nulos():
    print('\n  VALORES NULOS (df.isnull().sum())')
    nulos = df.isnull().sum().reset_index().rename(columns={'index': 'Columna', 0: 'Nulos'})
    nulos['Porcentaje'] = (nulos['Nulos'] / len(df) * 100).map(lambda x: f'{x:.0f}%')
    t(nulos)

def ver_distribucion():
    print('\n  DISTRIBUCION PUBLICA/PRIVADA (value_counts)')
    vc = df['es_publica'].value_counts().reset_index()
    vc.columns = ['Tipo', 'Cantidad']
    vc['Tipo'] = vc['Tipo'].map({True: 'Publica', False: 'Privada'})
    vc['Porcentaje'] = (vc['Cantidad'] / len(df) * 100).map(lambda x: f'{x:.0f}%')
    t(vc)

def ver_agrupaciones():
    print('\n  LISTAS POR USUARIO (df.groupby + agg)')
    grupo = df.groupby('id_usuario').agg(Total=('id_lista', 'count'), Publicas=('es_publica', 'sum')).reset_index()
    grupo.columns = ['ID Usuario', 'Total Listas', 'Publicas']
    t(grupo)
    print('\n  LISTAS POR MES (dt.month_name + value_counts)')
    meses = df['fecha_creacion'].dt.month_name().value_counts().reset_index()
    meses.columns = ['Mes', 'Listas creadas']
    t(meses)

def ver_filtrados():
    print('\n  FILTRADO: LISTAS PUBLICAS')
    t(df[df['es_publica'] == True][['id_lista', 'nombre', 'id_usuario']])
    print('\n  FILTRADO: LISTAS PRIVADAS')
    t(df[df['es_publica'] == False][['id_lista', 'nombre', 'id_usuario']])

def ver_temporal():
    print('\n  DIAS ACTIVA CADA LISTA (operacion con fechas)')
    resultado = df[['nombre']].copy()
    resultado['Creacion'] = df['fecha_creacion'].dt.strftime('%Y-%m-%d')
    resultado['Ult. actualizacion'] = df['fecha_actualizacion'].dt.strftime('%Y-%m-%d')
    resultado['Dias activa'] = (df['fecha_actualizacion'] - df['fecha_creacion']).dt.days
    t(resultado)
    dias = (df['fecha_actualizacion'] - df['fecha_creacion']).dt.days
    print(f'\n  Promedio dias activa: {dias.mean():.1f}')

opciones = {
    '1': ('Estructura de la tabla', ver_estructura),
    '2': ('Datos simulados', ver_datos),
    '3': ('Forma y tipos (shape, dtypes)', ver_tipos_y_forma),
    '4': ('Estadisticas descriptivas (describe)', ver_describe),
    '5': ('Valores nulos (isnull)', ver_nulos),
    '6': ('Distribucion publica/privada (value_counts)', ver_distribucion),
    '7': ('Agrupaciones usuario/mes (groupby, dt)', ver_agrupaciones),
    '8': ('Filtrados publicas/privadas (filtro)', ver_filtrados),
    '9': ('Analisis temporal (operaciones fechas)', ver_temporal),
}

while True:
    print()
    print('  LISTAS_REPRODUCCION - Analisis disponibles')
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
