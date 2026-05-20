from utils.simulacion import generar_simulacion
import requests

def consumir_servicios(numero_simulaciones=500):
    # Por defecto, se consume la simulación local
    # Esto permite trabajar sin depender de MySQL ni del backend Spring Boot
    datos = generar_simulacion(numero_simulaciones)
    return datos


def consumir_backend_real():
    # Recorre el backend real para obtener todas las canciones
    # Requiere que Spring Boot esté corriendo en localhost:8080 y MySQL activo
    url_base = "http://localhost:8080/api"
    canciones_totales = []

    # 1. Se obtienen todos los usuarios
    respuesta_usuarios = requests.get(f"{url_base}/usuarios")
    respuesta_usuarios.raise_for_status()
    usuarios = respuesta_usuarios.json()

    # 2. Por cada usuario se buscan sus playlists
    for usuario in usuarios:
        respuesta_playlists = requests.get(f"{url_base}/playlists/usuario/{usuario['id']}")
        respuesta_playlists.raise_for_status()
        playlists = respuesta_playlists.json()

        # 3. Por cada playlist se buscan sus canciones
        for playlist in playlists:
            respuesta_canciones = requests.get(f"{url_base}/playlists/{playlist['id']}/canciones")
            respuesta_canciones.raise_for_status()
            canciones = respuesta_canciones.json()

            # Se enriquecen las canciones con el contexto de usuario y playlist
            for cancion in canciones:
                cancion["playlistId"] = playlist["id"]
                cancion["playlistNombre"] = playlist["nombre"]
                cancion["usuarioId"] = usuario["id"]
                cancion["usuarioNombre"] = usuario["nombreUsuario"]
                canciones_totales.append(cancion)

    return canciones_totales