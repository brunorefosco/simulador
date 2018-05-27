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


def ejecutar(procesos, bloqueados, terminados):
    tiempo_total = 0
    while len(procesos) > 0:
        if len(bloqueados) != 0:
            final_listo = bloqueados.pop(0)
            listos.append(final_listo)

        for r in range(0, procesos[0].rafagas[0].duracion):
            procesos[0].estado = 2
            procesos[0].contador += 1
            procesos[0].tiempo += 1
            # proc = actualizar_bcp(procesos[0])
            tiempo_total += 1
            print("ejecutando {}".format(r))

        procesos[0].rafagas[0].ejecutado = 1
        ejecutando = 0

        print("-----ejecucion terminada-----")
        print("Proceso ejecutado: {n}".format(n=procesos[0].nombre))
        print("tiempo de proceso: {p}".format(p=procesos[0].tiempo))
        print("estado de proceso: {p}".format(p=procesos[0].estado))
        print("tiempo total: {p}".format(p=tiempo_total))

        procesos[0].rafagas.pop(0)

        if len(procesos[0].rafagas) == 0:
            procesos[0].estado = 4
            terminados.append(procesos[0])
            procesos.pop(0)
        elif len(procesos[0].rafagas) > 0:
            bloqueados.append(procesos[0])
            procesos.pop(0)

    return terminados


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
    ejecutar(listos, [], [])
# print("terminados {}".format(terminados))
# print("bloqueados {}".format(bloqueados))
# print("listos {}".format(listos))
