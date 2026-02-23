import unittest

from hoja_excel import HojaExcel


class TestHojaExcel(unittest.TestCase):
    def test_insertar_y_tiene_valor(self) -> None:
        hoja = HojaExcel(3, 3)
        self.assertEqual(hoja.tiene_valor(1, 1), False)
        hoja.insertar(1, 1, "hola")
        self.assertEqual(hoja.tiene_valor(1, 1), True)
        self.assertEqual(hoja.obtener(1, 1), "hola")

    def test_insertar_en_celda_ocupada_falla(self) -> None:
        hoja = HojaExcel(2, 2)
        hoja.insertar(1, 1, 123)
        with self.assertRaises(ValueError):
            hoja.insertar(1, 1, 999)

    def test_actualizar_en_celda_vacia_falla(self) -> None:
        hoja = HojaExcel(2, 2)
        with self.assertRaises(ValueError):
            hoja.actualizar(1, 1, 10)

    def test_actualizar_funciona(self) -> None:
        hoja = HojaExcel(2, 2)
        hoja.insertar(1, 1, 10)
        hoja.actualizar(1, 1, 20)
        self.assertEqual(hoja.obtener(1, 1), 20)

    def test_preview_basico(self) -> None:
        hoja = HojaExcel(2, 3)
        hoja.insertar(1, 2, "X")
        esperado = ".\tX\t.\n.\t.\t."
        self.assertEqual(hoja.preview(), esperado)

    def test_suma_fila(self) -> None:
        hoja = HojaExcel(2, 3)
        hoja.insertar(1, 1, 10)
        hoja.insertar(1, 2, 2.5)
        hoja.insertar(2, 1, 100)
        total = hoja.suma_fila(1)
        self.assertEqual(total, 12.5)

    def test_suma_columna(self) -> None:
        hoja = HojaExcel(3, 2)
        hoja.insertar(1, 2, 1)
        hoja.insertar(2, 2, 2)
        hoja.insertar(3, 2, 3)
        total = hoja.suma_columna(2)
        self.assertEqual(total, 6.0)

    def test_suma_falla_con_texto(self) -> None:
        hoja = HojaExcel(1, 3)
        hoja.insertar(1, 1, 1)
        hoja.insertar(1, 2, "no-num")
        with self.assertRaises(TypeError):
            hoja.suma_fila(1)

    def test_rangos_invalidos(self) -> None:
        hoja = HojaExcel(2, 2)
        with self.assertRaises(ValueError):
            hoja.insertar(0, 1, 1)
        with self.assertRaises(ValueError):
            hoja.insertar(1, 3, 1)
        with self.assertRaises(ValueError):
            hoja.tiene_valor(99, 1)


if __name__ == "__main__":
    unittest.main()