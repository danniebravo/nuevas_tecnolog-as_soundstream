import subprocess
import sys
import os

# Proyecto Integrador - SoundStream
# Menu interactivo para ver las simulaciones de cada tabla

archivos = {
    '1': ('Usuarios', 'utils/simulacion_usuarios.py'),
    '2': ('Canciones', 'utils/simulacion_canciones.py'),
    '3': ('Listas de Reproduccion', 'utils/simulacion_listas.py'),
    '4': ('Canciones Favoritas', 'utils/simulacion_favoritas.py'),
    '5': ('Lista Canciones', 'utils/simulacion_lista_canciones.py'),
    '6': ('Artistas', 'utils/simulacion_artistas.py'),
    '7': ('Generos', 'utils/simulacion_generos.py'),
}

while True:
    print()
    print('#' * 50)
    print('#  SOUNDSTREAM - Simulaciones con Pandas')
    print('#  Proyecto Integrador - Daniela Bravo')
    print('#' * 50)
    print()
    for key, (nombre, _) in archivos.items():
        print(f'  {key}. {nombre}')
    print(f'  8. Ver todas')
    print(f'  0. Salir')
    print()

    opcion = input('Selecciona una opcion: ').strip()

    if opcion == '0':
        print('Saliendo...')
        break
    elif opcion == '8':
        for key, (_, ruta) in archivos.items():
            print()
            subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), ruta)])
    elif opcion in archivos:
        nombre, ruta = archivos[opcion]
        print()
        subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), ruta)])
    else:
        print('Opcion no valida, intenta de nuevo.')

    input('\nPresiona Enter para volver al menu...')
