import math


def merge_sort(arr, coord):
    if len(arr) == 1:
        return arr

    meio = len(arr) // 2
    pontos_da_esq = arr[:meio]
    pontos_da_dir = arr[meio:]

    esq_ordenada = merge_sort(pontos_da_esq, coord)
    dir_ordenada = merge_sort(pontos_da_dir, coord)
    cmbo = merge(esq_ordenada, dir_ordenada, coord)
    return cmbo


def merge(A, B, coord):
    i = j = 0
    C = []

    if coord == 'x':
        coord = 0
    elif coord == 'y':
        coord = 1

    while i < len(A) and j < len(B):
        if A[i][coord] <= B[j][coord]:
            C.append(A[i])
            i += 1

        elif B[j][coord] < A[i][coord]:
            C.append(B[j])
            j += 1

    while i < len(A) and j == len(B):
        C.append(A[i])
        i += 1

    while j < len(B) and i == len(A):
        C.append(B[j])
        j += 1

    return C


def first_sort(points):
    Px = merge_sort(points, 'x')
    Py = merge_sort(points, 'y')
    return Px, Py


def encontrar_distancia(p1, p2):
    """ Aplicação do cálculo da distância Euclidiana"""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def frc_brt(arr):
    size = len(arr)
    menor_distancia = encontrar_distancia(arr[0], arr[1])
    par_analisado = (arr[0], arr[1])

    if len(arr) == 2:
        return encontrar_distancia(arr[0], arr[1]), arr[0], arr[1]

    for i in range(0, size):
        for j in range(i + 1, size):
            distance = encontrar_distancia(arr[i], arr[j])
            if distance < menor_distancia:
                menor_distancia = distance
                par_analisado = (arr[i], arr[j])

    return menor_distancia, par_analisado


def par_mais_proximo(Px, Py):
    if len(Px) <= 3:
        return frc_brt(Px)

    midpoint_x = len(Px) // 2
    Qx = Px[:midpoint_x]
    Rx = Px[midpoint_x:]
    median_x = Px[midpoint_x]
    Qy, Ry = [], []

    for ponto in Py:
        if ponto[0] < int(median_x[0]):
            Qy.append(ponto)
        else:
            Ry.append(ponto)

    menor_dist_esq = par_mais_proximo(Qx, Qy)
    menor_dist_dir = par_mais_proximo(Rx, Ry)
    menor_distancia = min(menor_dist_esq, menor_dist_dir)
    x_bar = Qx[-1][0]
    Sy = []

    for y in Py:
        if x_bar - menor_distancia[0] < y[0] < x_bar + menor_distancia[0]:
            Sy.append(y)

    for i in range(len(Sy) - 1):
        for j in range(i + 1, min(i + 7, len(Sy))):
            pontos = Sy[i]
            points_close = Sy[j]
            dist = encontrar_distancia(pontos, points_close)

            if dist < menor_distancia[0]:
                menor_distancia = (dist, pontos, points_close)

    return menor_distancia
