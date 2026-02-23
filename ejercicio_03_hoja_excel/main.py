from hoja_excel import HojaExcel


def main() -> None:
    hoja = HojaExcel(filas=4, columnas=4)

    hoja.insertar(1, 1, 10)
    hoja.insertar(1, 2, 20)
    hoja.insertar(1, 3, 60)
    hoja.insertar(2, 1, 5.5)
    hoja.insertar(3, 4, 7)

    print("PREVIEW:")
    print(hoja.preview())
    print("")

    print("¿Celda (1,1) tiene valor?:", hoja.tiene_valor(1, 1))
    print("¿Celda (4,4) tiene valor?:", hoja.tiene_valor(4, 4))
    print("")

    hoja.actualizar(2, 1, 6.5)

    print("Suma fila 1:")
    hoja.suma_fila(1)

    print("Suma columna 1:")
    hoja.suma_columna(1)


if __name__ == "__main__":
    main()