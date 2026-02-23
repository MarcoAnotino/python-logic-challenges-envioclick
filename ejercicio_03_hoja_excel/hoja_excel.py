class HojaExcel:
    """
    Representación básica de una hoja tipo Excel (filas y columnas).

    Reglas:
    - Coordenadas 1..N (fila y columna)
    - Insertar: falla si ya existe valor
    - Actualizar: falla si no existe valor
    - Validar si una celda tiene info (sin usar 'in')
    - Preview de toda la hoja
    - Suma por fila y por columna (solo valores numéricos)
    """

    def __init__(self, filas: int, columnas: int) -> None:
        self._validar_dimension("filas", filas)
        self._validar_dimension("columnas", columnas)
        self._filas = filas
        self._columnas = columnas
        self._celdas = {}  # dict[(int,int) -> object]

    @staticmethod
    def _validar_dimension(nombre: str, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError(f"{nombre} debe ser int.")
        if valor <= 0:
            raise ValueError(f"{nombre} debe ser > 0.")

    def _validar_coordenadas(self, fila: int, columna: int) -> None:
        if not isinstance(fila, int) or not isinstance(columna, int):
            raise TypeError("fila y columna deben ser int.")

        if fila < 1 or fila > self._filas:
            raise ValueError("fila fuera de rango.")

        if columna < 1 or columna > self._columnas:
            raise ValueError("columna fuera de rango.")

    def insertar(self, fila: int, columna: int, valor: object) -> None:
        """
        Inserta información en una celda.
        Falla si la celda ya tiene valor.
        """
        self._validar_coordenadas(fila, columna)
        clave = (fila, columna)

        try:
            _ = self._celdas[clave]
        except KeyError:
            self._celdas[clave] = valor
            return

        raise ValueError("La celda ya contiene información. Use actualizar().")

    def actualizar(self, fila: int, columna: int, valor: object) -> None:
        """
        Actualiza información en una celda.
        Falla si la celda está vacía (no existe).
        """
        self._validar_coordenadas(fila, columna)
        clave = (fila, columna)

        try:
            _ = self._celdas[clave]
        except KeyError as exc:
            raise ValueError("La celda no tiene información. Use insertar().") from exc

        self._celdas[clave] = valor

    def tiene_valor(self, fila: int, columna: int) -> bool:
        """
        Valida si una celda tiene información.
        """
        self._validar_coordenadas(fila, columna)
        clave = (fila, columna)

        try:
            _ = self._celdas[clave]
        except KeyError:
            return False

        return True

    def obtener(self, fila: int, columna: int):
        """
        Obtiene el valor de una celda.
        Retorna None si no existe.
        """
        self._validar_coordenadas(fila, columna)
        clave = (fila, columna)

        try:
            return self._celdas[clave]
        except KeyError:
            return None

    def preview(self) -> str:
        """
        Muestra un preview de la hoja completa.
        Celdas vacías se muestran como '.'.
        """
        partes = []
        fila = 1

        while fila <= self._filas:
            col = 1
            while col <= self._columnas:
                valor = self.obtener(fila, col)
                if valor is None:
                    partes.append(".")
                else:
                    partes.append(str(valor))

                if col < self._columnas:
                    partes.append("\t")
                col += 1

            if fila < self._filas:
                partes.append("\n")
            fila += 1

        return "".join(partes)

    @staticmethod
    def _asegurar_numero(valor: object) -> float:
        if isinstance(valor, bool):
            raise TypeError("Valor no numérico en suma.")
        if isinstance(valor, int) or isinstance(valor, float):
            return float(valor)
        raise TypeError("Valor no numérico en suma.")

    def suma_fila(self, fila: int) -> float:
        """
        Dada una fila, recupera todos los elementos e imprime la suma
        de los valores numéricos encontrados.
        Si hay un valor no numérico en la fila, lanza TypeError.
        """
        if not isinstance(fila, int):
            raise TypeError("fila debe ser int.")
        if fila < 1 or fila > self._filas:
            raise ValueError("fila fuera de rango.")

        total = 0.0
        col = 1
        while col <= self._columnas:
            valor = self.obtener(fila, col)
            if valor is not None:
                total += self._asegurar_numero(valor)
            col += 1

        return total

    def suma_columna(self, columna: int) -> float:
        """
        Dada una columna, recupera todos los elementos e imprime la suma
        de los valores numéricos encontrados.
        Si hay un valor no numérico en la columna, lanza TypeError.
        """
        if not isinstance(columna, int):
            raise TypeError("columna debe ser int.")
        if columna < 1 or columna > self._columnas:
            raise ValueError("columna fuera de rango.")

        total = 0.0
        fila = 1
        while fila <= self._filas:
            valor = self.obtener(fila, columna)
            if valor is not None:
                total += self._asegurar_numero(valor)
            fila += 1

        return total