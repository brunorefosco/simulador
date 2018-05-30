from proc import carga_proceso


def ejecutar(procesos, bloqueados, terminados):
    tiempo_total = 0
    while len(procesos) > 0:
        if len(bloqueados) != 0:  # and procesos[0].entrada > tiempo_total:
            final_listo = bloqueados.pop(0)
            listos.append(final_listo)

        print("Comienza ejecución de {n}".format(n=procesos[0].nombre))
        print("------------------")

        for r in range(0, procesos[0].rafagas[0].duracion):
            procesos[0].estado = 2
            procesos[0].contador += 1
            procesos[0].tiempo += 1
            # proc = actualizar_bcp(procesos[0])
            tiempo_total += 1
            print("ejecutando {}".format(r))

        print("-----ejecucion terminada-----")

        print("Proceso ejecutado: {n}".format(n=procesos[0].nombre))
        print("tiempo de proceso: {p}".format(p=procesos[0].tiempo))
        print("estado de proceso: {p}".format(p=procesos[0].estado))
        print("tiempo total: {p}".format(p=tiempo_total))

        procesos[0].rafagas.pop(0)  # elimino la ráfaga ya ejecutada

        if len(procesos[0].rafagas) == 0:
            procesos[0].estado = 4  # cambio el estado del proceso a ejecutado si ya se terminó
            terminados.append(procesos[0])  # lo agrego a la lista terminados
            procesos.pop(0)  # lo elimino de la lista procesos
        elif len(procesos[0].rafagas) > 0:
            bloqueados.append(procesos[0])  # lo envío a bloqueados
            procesos.pop(0)

    return terminados


if __name__ == '__main__':
    listos = carga_proceso()
    ejecutar(listos, [], [])
