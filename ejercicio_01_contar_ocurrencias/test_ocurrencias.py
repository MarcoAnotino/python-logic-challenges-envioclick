import unittest

from ocurrencias import contar_ocurrencias

class TestContarOcurrencias(unittest.TestCase):
    def test_ejemplo_logistica(self) -> None:
        parrafo = (
            "La logística Digital es un concepto que surge de la integración entre "
            "la logística tradicional y la era digital. Con el auge del correo electrónico "
            "y las descargas digitales reemplazando productos físicos, podríamos estar "
            "hablando de un golpe devastador para la industria de la logística, pero, de hecho, "
            "ha ocurrido algo muy diferente. El sector de la logística ha introducido las innovaciones digitales."
        )
        self.assertEqual(contar_ocurrencias(parrafo, "logística"), 4)

    def test_solapadas(self) -> None:
        self.assertEqual(contar_ocurrencias("aa aa", "aa"), 2)

    def test_texto_mas_largo(self) -> None:
        self.assertEqual(contar_ocurrencias("abc def", "abc"), 1)

    def test_texto_vacio(self) -> None:
        self.assertEqual(contar_ocurrencias("abc", ""), 0)

if __name__ == "__main__":
    unittest.main()