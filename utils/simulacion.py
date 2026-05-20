import random
from datetime import datetime, timedelta

def generar_simulacion(numero_simulaciones):
    # Canciones realistas con su artista correspondiente (como vienen de iTunes)
    catalogo = [
        {"trackName": "bohemian rhapsody", "artistName": "queen", "duracion": 354000},
        {"trackName": "blinding lights", "artistName": "the weeknd", "duracion": 200000},
        {"trackName": "shape of you", "artistName": "ed sheeran", "duracion": 233000},
        {"trackName": "billie jean", "artistName": "michael jackson", "duracion": 294000},
        {"trackName": "rolling in the deep", "artistName": "adele", "duracion": 228000},
    ]

    fecha_inicio = datetime(2026, 1, 2)
    simulaciones = []

    for _ in range(numero_simulaciones):
        cancion = random.choice(catalogo)
        simulacion = {
            "id": random.randint(1, 10000),
            "trackId": random.randint(100000, 999999),
            "trackName": cancion["trackName"],
            "artistName": cancion["artistName"],
            "trackTimeMillis": cancion["duracion"],
            "playlistId": random.randint(1, 20),
            "fecha": fecha_inicio + timedelta(days=random.randint(0, 60))
        }

        # Inyección de errores controlados (para mostrar la limpieza)
        probabilidad_error = random.random()
        if probabilidad_error < 0.15:
            simulacion["id"] = None
        elif probabilidad_error < 0.30:
            simulacion["trackName"] = random.choice(["podcast de cocina", "audiolibro de historia"])
        elif probabilidad_error < 0.45:
            simulacion["trackTimeMillis"] = random.choice([0, -1000, None])
        elif probabilidad_error < 0.65:
            simulacion["artistName"] = " " + simulacion["artistName"].upper()
        elif probabilidad_error < 0.75:
            simulacion["fecha"] = None

        simulaciones.append(simulacion)
    return simulaciones