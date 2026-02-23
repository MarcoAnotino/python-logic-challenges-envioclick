def particion_estable(data, filtros, cumple_todos_los_filtros):
    """
    Divide en:
    - filtrados: cumplen TODOS los filtros
    - restantes: no cumplen filtros

    Mantiene el orden original dentro de cada grupo (partición estable).
    """
    filtrados = []
    restantes = []

    i = 0
    while i < len(data):
        item = data[i]

        if cumple_todos_los_filtros(item, filtros):
            filtrados.append(item)
        else:
            restantes.append(item)

        i += 1

    return filtrados, restantes


def procesar(data, filtros, order, cumple_todos_los_filtros, stable_merge_sort):
    """
    Flujo completo:
    1) Partición estable (filtrados / restantes)
    2) Ordena SOLO filtrados por priority (ASC/DESC) de forma estable
    3) Retorna: filtrados_ordenados + restantes (restantes sin alterar)
    """
    filtrados, restantes = particion_estable(data, filtros, cumple_todos_los_filtros)
    filtrados_ordenados = stable_merge_sort(filtrados, order)

    resultado = []
    i = 0
    while i < len(filtrados_ordenados):
        resultado.append(filtrados_ordenados[i])
        i += 1

    j = 0
    while j < len(restantes):
        resultado.append(restantes[j])
        j += 1

    return resultado