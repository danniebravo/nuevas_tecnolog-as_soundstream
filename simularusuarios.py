import random

from datetime import datetime,timedelta

#codigo de JJ
def generar_simulacion(numeroSimulaciones):

    nombres=["esterilizacion","corte uñas","vacunacion"]
    codigos=["am001","am045","am300"]
    costos=[350000,100000,250000]
    fechaInicio=datetime(2026,1,2)

    simulaciones=[]
    for _ in range(numeroSimulaciones):

        simulacion={
            "id":random.randint(0,200),
            "servicio":random.choice(nombres),
            "costo":random.choice(costos),
            "codigo":random.choice(codigos),
            "fecha":fechaInicio+timedelta(days=random.randint(0,60))
        }

        simulaciones.add(simulacion)
    return simulaciones
