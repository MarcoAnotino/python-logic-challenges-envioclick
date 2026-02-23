def stable_merge_sort(items, order):
    """
    Ordena de forma estable una lista de diccionarios por el campo 'priority'
    usando Merge Sort.

    Restricciones: no usar sort/sorted.
    order: "ASC" o "DESC"
    Si falta 'priority', se toma como 0.
    """
    if len(items) <= 1:
        return items

    if order != "ASC" and order != "DESC":
        raise ValueError("Orden no soportado: " + str(order))

    mitad = len(items) // 2
    izquierda = stable_merge_sort(items[:mitad], order)
    derecha = stable_merge_sort(items[mitad:], order)

    return _merge_estable(izquierda, derecha, order)


def _merge_estable(izquierda, derecha, order):
    """
    Mezcla dos listas ya ordenadas de forma estable, comparando por 'priority'.
    """
    resultado = []

    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        item_i = izquierda[i]
        item_j = derecha[j]

        pri_i = _obtener_prioridad(item_i)
        pri_j = _obtener_prioridad(item_j)

        if order == "ASC":
            # Estable: si son iguales, se elige el de la izquierda primero
            if pri_i <= pri_j:
                resultado.append(item_i)
                i += 1
            else:
                resultado.append(item_j)
                j += 1
        else:  # DESC
            # Estable: si son iguales, se elige el de la izquierda primero
            if pri_i >= pri_j:
                resultado.append(item_i)
                i += 1
            else:
                resultado.append(item_j)
                j += 1

    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado


def _obtener_prioridad(item):
    """
    Devuelve item['priority'] si existe; si no, retorna 0.
    No usa 'in' por restricciones.
    """
    try:
        return item["priority"]
    except KeyError:
        return 0