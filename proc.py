
class Rafaga:
    def __init__(self, duracion):
        self.duracion = duracion
        self.ejecutado = 0
        self.entrada = 0


class Proceso:
    def __init__(self, nombre, rafagas):
        self.nombre = nombre
        self.rafagas = rafagas
        self.estado = 0  # 0 = no cargado, 1 = listo, 2 = ejecutando, 3 = bloqueado, 4 = terminado
        self.contador = 0
        self.tiempo = 0