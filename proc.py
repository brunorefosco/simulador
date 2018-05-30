class Rafaga:
    def __init__(self, duracion):
        self.duracion = duracion
        self.ejecutado = 0


class Proceso:
    def __init__(self, nombre, rafagas):
        self.nombre = nombre
        self.rafagas = rafagas
        self.estado = 0  # 0 = no cargado, 1 = listo, 2 = ejecutando, 3 = bloqueado, 4 = terminado
        self.contador = 0
        self.tiempo = 0
        self.entrada = 0


def carga_rafaga(otra):
    rafagas = []
    print('Carga de ráfaga')

    while (otra == '1'):
        print('Qué duracion tiene la ráfaga?')

        duracion = int(input())
        raf = Rafaga(duracion)
        rafagas.append(raf)

        print('Desea cargar otra ráfaga? Presione 1 para cargar ')

        otra = input()

    return rafagas


def carga_proceso():
    procesos = []

    print("------------")
    print("Carga procesos")
    print("Cuántos procesos?")

    cantidad = int(input())
    for p in range(0, cantidad):
        print("Cargando {}".format(p))
        print("Ingrese el nombre del proceso")

        nombre = input()

        raf = carga_rafaga('1')

        proc = Proceso(nombre, raf)

        print("nombre del proceso: {}".format(proc.nombre))
        print("rafagas del proceso: {} ".format(proc.rafagas))
        print("----------")
        print("Carga finalizada")

        procesos.append(proc)

    return procesos
