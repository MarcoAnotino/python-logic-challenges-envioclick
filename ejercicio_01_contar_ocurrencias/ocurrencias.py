def es_separador(caracter: str) -> bool:
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
