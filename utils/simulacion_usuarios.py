import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 40)

# =============================================
# TABLA: USUARIOS
# =============================================
# Almacena la informacion de todos los usuarios registrados en SoundStream.
# Cada usuario tiene rol ADMIN (gestiona catalogo) o USUARIO (escucha musica).
#
# Relaciones:
# - 1:N con listas_reproduccion (un usuario crea muchas listas)
# - 1:N con canciones via subido_por (un admin sube muchas canciones)
# - N:M con canciones via canciones_favoritas

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

df_usuarios = pd.DataFrame(datos)

# --- Descripcion de la estructura ---
descripcion = pd.DataFrame({
    'Campo': ['id_usuario', 'nombre_usuario', 'correo', 'contrasena_hash',
              'rol', 'imagen_perfil_url', 'activo', 'fecha_registro'],
    'Tipo': ['INT (PK)', 'VARCHAR', 'VARCHAR', 'VARCHAR',
             'ENUM', 'VARCHAR', 'BIT', 'DATETIME'],
    'Descripcion': [
        'Identificador unico del usuario',
        'Nombre de usuario para login',
        'Correo electronico unico',
        'Contrasena encriptada con BCrypt',
        'Rol: ADMIN o USUARIO',
        'URL de la imagen de perfil',
        'Indica si la cuenta esta activa',
        'Fecha de creacion de la cuenta'
    ]
})

# --- Mostrar resultados ---
print('=' * 70)
print('TABLA: USUARIOS')
print('=' * 70)

print('\nEstructura de la tabla:')
print(descripcion.to_string(index=False))

print(f'\nTotal registros: {len(df_usuarios)}')
print(f'Admins: {(df_usuarios["rol"] == "ADMIN").sum()} | Usuarios: {(df_usuarios["rol"] == "USUARIO").sum()}')
print(f'Activos: {df_usuarios["activo"].sum()} | Inactivos: {(~df_usuarios["activo"]).sum()}')

print('\nDatos simulados:')
print(df_usuarios.to_string(index=False))

print('\nTipos de datos:')
print(df_usuarios.dtypes)

print('\nValores nulos por columna:')
print(df_usuarios.isnull().sum())

print('\nDistribucion de roles:')
print(df_usuarios['rol'].value_counts())

print(f'\nPrimer registro: {df_usuarios["fecha_registro"].min()}')
print(f'Ultimo registro: {df_usuarios["fecha_registro"].max()}')
