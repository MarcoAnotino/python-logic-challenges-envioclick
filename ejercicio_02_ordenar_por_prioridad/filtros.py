def cumple_todos_los_filtros(item, filtros):
    """
    Evalúa si un elemento cumple con todos los filtros proporcionados.

    :param item: Diccionario con atributos del elemento.
    :param filtros: Lista de tuplas (campo, operador, valor).
    :return: True si cumple todos los filtros, False en caso contrario.
    """

    if len(filtros) == 0:
        return True
    
    indice = 0

    while indice < len(filtros):
        campo, operador, valor_esperado = filtros[indice]

        try:
            valor_item = item[campo]
        except KeyError:
            return False
        
        if operador == "=":
            if not valor_item == valor_esperado:
                return False
        
        elif operador == "!=":
            if not valor_item != valor_esperado:
                return False
        
        elif operador == ">":
            if not valor_item > valor_esperado:
                return False
        
        elif operador == "<":
            if not valor_item < valor_esperado:
                return False
        
        elif operador == ">=":
            if not valor_item >= valor_esperado:
                return False

        elif operador == "<=":
            if not valor_item <= valor_esperado:
                return False
        
        else:
            raise ValueError("Operador no soportado: " + str(operador))
        
        indice += 1
    
    return True
        