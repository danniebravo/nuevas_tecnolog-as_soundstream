import pandas as pd
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# =============================================
# TABLA: USUARIOS
# =============================================

datos = {
    'id_usuario': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'nombre_usuario': [
        'admin_daniela', 'admin_carlos', 'maria_music', 'juan_rocks',
        'lucia_beats', 'pedro_jazz', 'ana_pop', 'diego_rap',
        'sofia_electro', 'miguel_latin'
    ],
    'correo': [
        'daniela@soundstream.com', 'carlos@soundstream.com', 'maria@gmail.com',
        'juan@gmail.com', 'lucia@hotmail.com', 'pedro@yahoo.com',
        'ana@gmail.com', 'diego@outlook.com', 'sofia@gmail.com', 'miguel@gmail.com'
    ],
    'contrasena_hash': [f'$2a$10$hash{i}' for i in range(1, 11)],
    'rol': ['ADMIN', 'ADMIN', 'USUARIO', 'USUARIO', 'USUARIO',
            'USUARIO', 'USUARIO', 'USUARIO', 'USUARIO', 'USUARIO'],
    'imagen_perfil_url': [
        f'https://img.soundstream.com/u{i}.jpg' if i not in [6, 8]
        else None for i in range(1, 11)
    ],
    'activo': [True, True, True, True, True, True, False, True, True, True],
    'fecha_registro': pd.to_datetime([
        '2026-01-15 10:30', '2026-01-15 11:00', '2026-02-01 14:20',
        '2026-02-10 09:15', '2026-02-14 16:45', '2026-03-01 12:00',
        '2026-03-05 08:30', '2026-03-10 20:10', '2026-03-15 17:25',
        '2026-04-01 11:40'
    ])
}

df = pd.DataFrame(datos)


def t(dataframe, fmt='grid'):
    """Imprime un DataFrame como tabla bonita."""
    print(tabulate(dataframe, headers='keys', tablefmt=fmt, showindex=False))


def ver_estructura():
    print('\n  ESTRUCTURA DE LA TABLA')
    t(pd.DataFrame({
        'Campo': ['id_usuario', 'nombre_usuario', 'correo', 'contrasena_hash',
                  'rol', 'imagen_perfil_url', 'activo', 'fecha_registro'],
        'Tipo': ['INT (PK)', 'VARCHAR', 'VARCHAR', 'VARCHAR',
                 'ENUM', 'VARCHAR', 'BIT', 'DATETIME'],
        'Descripcion': [
            'Identificador unico del usuario', 'Nombre de usuario para login',
            'Correo electronico unico', 'Contrasena encriptada (BCrypt)',
            'Rol: ADMIN o USUARIO', 'URL imagen de perfil',
            'Cuenta activa o no', 'Fecha de creacion de cuenta'
        ]
    }))
    print('\n  RELACIONES')
    t(pd.DataFrame({
        'Relacion': ['usuarios -> listas_reproduccion', 'usuarios -> canciones', 'usuarios <-> canciones'],
        'Tipo': ['1:N', '1:N', 'N:M'],
        'Descripcion': ['Un usuario crea muchas listas', 'Un admin sube muchas canciones', 'Favoritos via canciones_favoritas']
    }))


def ver_datos():
    print('\n  DATOS SIMULADOS')
    vista = df[['id_usuario', 'nombre_usuario', 'correo', 'rol', 'activo', 'fecha_registro']].copy()
    vista['fecha_registro'] = vista['fecha_registro'].dt.strftime('%Y-%m-%d %H:%M')
    t(vista)
    print(f'\n  Total registros: {len(df)}')


def ver_tipos_y_forma():
    print('\n  FORMA DEL DATAFRAME (df.shape)')
    t(pd.DataFrame({'Filas': [df.shape[0]], 'Columnas': [df.shape[1]]}))
    print('\n  TIPOS DE DATOS (df.dtypes)')
    t(df.dtypes.reset_index().rename(columns={'index': 'Columna', 0: 'Tipo'}))


def ver_describe():
    print('\n  ESTADISTICAS DESCRIPTIVAS (df.describe)')
    desc = df.describe(include='all').reset_index().rename(columns={'index': 'Metrica'})
    t(desc)


def ver_nulos():
    print('\n  VALORES NULOS (df.isnull().sum())')
    nulos = df.isnull().sum().reset_index().rename(columns={'index': 'Columna', 0: 'Nulos'})
    nulos['Porcentaje'] = (nulos['Nulos'] / len(df) * 100).map(lambda x: f'{x:.0f}%')
    t(nulos)
    print('\n  USUARIOS SIN IMAGEN DE PERFIL')
    t(df[df['imagen_perfil_url'].isnull()][['id_usuario', 'nombre_usuario']])


def ver_distribucion_roles():
    print('\n  DISTRIBUCION DE ROLES (value_counts)')
    vc = df['rol'].value_counts().reset_index()
    vc.columns = ['Rol', 'Cantidad']
    vc['Porcentaje'] = (vc['Cantidad'] / len(df) * 100).map(lambda x: f'{x:.0f}%')
    t(vc)


def ver_filtrados():
    print('\n  FILTRADO: SOLO ADMINISTRADORES')
    t(df[df['rol'] == 'ADMIN'][['id_usuario', 'nombre_usuario', 'correo']])
    print('\n  FILTRADO: USUARIOS INACTIVOS')
    inactivos = df[df['activo'] == False][['id_usuario', 'nombre_usuario', 'rol']]
    if len(inactivos) > 0:
        t(inactivos)
    else:
        print('  Todos los usuarios estan activos')
    print('\n  FILTRADO: REGISTRADOS DESPUES DE MARZO 2026 (df.query)')
    recientes = df.query('fecha_registro >= "2026-03-01"')[['id_usuario', 'nombre_usuario', 'fecha_registro']].copy()
    recientes['fecha_registro'] = recientes['fecha_registro'].dt.strftime('%Y-%m-%d %H:%M')
    t(recientes)


def ver_agrupaciones():
    print('\n  AGRUPACION POR ROL Y ESTADO (df.groupby)')
    grupo = df.groupby(['rol', 'activo']).size().reset_index(name='Cantidad')
    t(grupo)
    print('\n  DOMINIOS DE CORREO (str.split + value_counts)')
    dominios = df['correo'].str.split('@').str[1].value_counts().reset_index()
    dominios.columns = ['Dominio', 'Cantidad']
    t(dominios)


def ver_ordenamiento():
    print('\n  ORDENAMIENTO POR FECHA (df.sort_values)')
    orden = df.sort_values('fecha_registro', ascending=False)[['nombre_usuario', 'rol', 'fecha_registro']].copy()
    orden['fecha_registro'] = orden['fecha_registro'].dt.strftime('%Y-%m-%d %H:%M')
    t(orden)
    print(f'\n  Primer registro: {df["fecha_registro"].min().strftime("%Y-%m-%d")}')
    print(f'  Ultimo registro: {df["fecha_registro"].max().strftime("%Y-%m-%d")}')


opciones = {
    '1': ('Estructura de la tabla', ver_estructura),
    '2': ('Datos simulados', ver_datos),
    '3': ('Forma y tipos (shape, dtypes)', ver_tipos_y_forma),
    '4': ('Estadisticas descriptivas (describe)', ver_describe),
    '5': ('Valores nulos (isnull)', ver_nulos),
    '6': ('Distribucion de roles (value_counts)', ver_distribucion_roles),
    '7': ('Filtrados (activos, admins, query)', ver_filtrados),
    '8': ('Agrupaciones (groupby, str.split)', ver_agrupaciones),
    '9': ('Ordenamiento por fecha (sort_values)', ver_ordenamiento),
}

while True:
    print()
    print('  USUARIOS - Analisis disponibles')
    print('  ' + '-' * 45)
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
