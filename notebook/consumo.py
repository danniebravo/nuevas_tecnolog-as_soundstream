import requests

def consumir_servicios():
    url = "http://localhost:8080/api/servicios"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos