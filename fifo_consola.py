
listos = []
terminados = []
bloqueados = []


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


def ejecutar(proceso):
    if proceso.nombre in bloqueados:
        print("proceso bloqueado")

    ejecutando = 0
    if ejecutando == 0:
        proceso.estado = 1

        print("pasa el proceso ({p}) a listo".format(p=proceso.nombre))

        proceso.estado = 1
        for r in range(0, proceso.rafagas[0].duracion):
            ejecutando = 1

            proceso.estado = 2
            proceso.contador += 1
            proceso.tiempo += 1

            print("ejecutando {}".format(r))

        proceso.rafagas[0].ejecutado = 1
        ejecutando = 0

        print("ejecucion terminada")
        print("tiempo de proceso: {p}".format(p=proceso.tiempo))
        print("estado de proceso: {p}".format(p=proceso.estado))

        proceso.rafagas.pop(0)

        if len(proceso.rafagas) == 0:
            proceso.estado = 4
            terminados.append(proceso)

        elif len(proceso.rafagas) > 0:
            bloqueados.append(proceso)


def fifo(procesos):
    for p in procesos:
        for r in p.rafagas:
            ejecutar(p)


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


if __name__ == '__main__':
    listos = carga_proceso()
    fifo(listos)
    print("terminados {}".format(terminados))
    print("bloqueados {}".format(bloqueados))
    print("listos {}".format(listos))
