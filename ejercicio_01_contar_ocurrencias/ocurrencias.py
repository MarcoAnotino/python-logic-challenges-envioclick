def es_separador(caracter: str) -> bool:
    """
        Determina si un carácter se considera separador de palabras.

        Un separador es cualquier carácter que delimita palabras para validar
        coincidencias completas (no subcadenas). Se consideran separadores:
        - Espacio (" ").
        - Caracteres de control tipo espacio/tabulación/salto de línea (códigos 9 a 13).
        - Signos de puntuación: ., , ; :
        - Signos de interrogación y exclamación: ¡ ! ¿ ?
        - Paréntesis, comillas y guion: ( ) " ' -

        :param caracter: Carácter individual a evaluar.
        :return: True si es separador; False en caso contrario.
    """
    codigo = ord(caracter)

    if caracter == " ":
        return True

    if 9 <= codigo <= 13:
        return True

    if caracter == "." or caracter == "," or caracter == ";" or caracter == ":":
        return True

    if caracter == "¡" or caracter == "!" or caracter == "¿" or caracter == "?":
        return True

    if caracter == "(" or caracter == ")" or caracter == "\"" or caracter == "'" or caracter == "-":
        return True

    return False


def contar_ocurrencias(parrafo: str, texto:str) -> int:
    """
        Cuenta cuántas veces aparece una palabra/expresión dentro de un párrafo,
        comparando carácter por carácter y validando límites de palabra.

        Reglas:
        - La comparación es insensible a mayúsculas/minúsculas.
        - Solo cuenta coincidencias completas: el match debe estar delimitado por
        separadores (inicio/fin de cadena o un carácter considerado separador).
        - No usa funciones facilitadoras como 'in', 'find', 'index', regex, etc.

        :param parrafo: Texto donde se buscarán las ocurrencias.
        :param texto: Texto a buscar dentro del párrafo.
        :return: Número total de ocurrencias válidas encontradas.
    """
    parrafo_normalizado = parrafo.lower()
    texto_normalizado = texto.lower()

    largo_parrafo = len(parrafo_normalizado)
    largo_texto = len(texto_normalizado)

    if largo_texto > largo_parrafo:
        return 0
    if largo_texto == 0 or largo_parrafo == 0:
        return 0
    
    total = 0
    i = 0

    while i <= largo_parrafo - largo_texto:
        j = 0
        coincide = True

        while j < largo_texto:
            if parrafo_normalizado[i + j] != texto_normalizado[j]:
                coincide = False
                break
            j += 1
        
        if coincide:
            inicio_ok = False
            fin_ok = False

            if i == 0:
                inicio_ok = True
            else:
                inicio_ok = es_separador(parrafo_normalizado[i - 1])
            
            final_index = i + largo_texto
            if final_index == largo_parrafo:
                fin_ok = True
            else:
                fin_ok = es_separador(parrafo_normalizado[final_index])
            
            if inicio_ok and fin_ok:
                total += 1
            
        i += 1
    
    return total
