import random


def generar_lista_aleatoria():
    lista = []
    for _ in range(10):
        numero = random.randint(1, 50)
        lista.append(numero)
    print("Lista de números aleatorios:", lista)
    return lista


def obtener_numeros_no_repetidos(lista):
    numeros_no_repetidos = []
    for numero in lista:
        if numero not in numeros_no_repetidos:
            numeros_no_repetidos.append(numero)
    print("Números no repetidos:", numeros_no_repetidos)
    return numeros_no_repetidos


def ordenar_lista(numeros_no_repetidos):
    orden_ascendente = sorted(numeros_no_repetidos)
    orden_descendente = sorted(numeros_no_repetidos, reverse=True)

    print("Ordenado de mayor a menor:", orden_descendente)
    print("Ordenado de menor a mayor:", orden_ascendente)
    return orden_ascendente, orden_descendente


def mayor_par(numeros_no_repetidos):
    mayor_par = None
    for numero in numeros_no_repetidos:
        if numero % 2 == 0:
            if mayor_par is None or numero > mayor_par:
                mayor_par = numero
    print("Mayor número par:", mayor_par)
    return mayor_par


def main():
    lista_aleatoria = generar_lista_aleatoria()
    numeros_no_repetidos = obtener_numeros_no_repetidos(lista_aleatoria)
    ordenar_lista(numeros_no_repetidos)
    mayor_par(numeros_no_repetidos)


if __name__ == "__main__":
    main()
