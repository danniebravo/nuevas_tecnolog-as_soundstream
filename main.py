import subprocess
import sys
import os

archivos = {
    '1': ('Usuarios',                'utils/simulacion_usuarios.py'),
    '2': ('Canciones',               'utils/simulacion_canciones.py'),
    '3': ('Listas de Reproduccion',  'utils/simulacion_listas.py'),
    '4': ('Canciones Favoritas',     'utils/simulacion_favoritas.py'),
    '5': ('Lista Canciones',         'utils/simulacion_lista_canciones.py'),
    '6': ('Artistas',                'utils/simulacion_artistas.py'),
    '7': ('Generos',                 'utils/simulacion_generos.py'),
}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print()
    print('  SOUNDSTREAM - Simulaciones de BD con Pandas')
    print('  Materia:     Nuevas Tecnologias')
    print('  Integrante:  Daniela Bravo')
    print('  ' + '-' * 45)

    print()
    for key, (nombre, _) in archivos.items():
        print(f'  {key}. {nombre}')
    print(f'  8. Ver todas las tablas')
    print(f'  0. Salir')

    opcion = input('\n  Selecciona una tabla: ').strip()

    if opcion == '0':
        print('\n  Saliendo...\n')
        break
    elif opcion == '8':
        for key, (_, ruta) in archivos.items():
            subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), ruta)])
    elif opcion in archivos:
        subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), archivos[opcion][1])])
    else:
        print('\n  Opcion no valida.')

    input('\n  Enter para volver al menu...')
