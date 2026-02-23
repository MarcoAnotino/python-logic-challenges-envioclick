from ocurrencias import contar_ocurrencias

def main() -> None:
    print("=== Ejercicio 1: Contar ocurrencias ===")
    parrafo = input("Párrafo: ")
    texto = input("Texto: ")

    ocurrencias = contar_ocurrencias(parrafo, texto)
    print(f"{ocurrencias} ocurrencias encontradas")

if __name__ == "__main__":
    main()