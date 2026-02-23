import unittest

from filtros import cumple_todos_los_filtros
from ordenamiento import stable_merge_sort
from prioridad import procesar


class TestPrioridad(unittest.TestCase):

    def test_filtro_basico(self):
        item = {"weight": 3}
        self.assertTrue(cumple_todos_los_filtros(item, [("weight", "=", 3)]))
        self.assertFalse(cumple_todos_los_filtros(item, [("weight", "=", 2)]))

    def test_merge_sort_asc(self):
        data = [
            {"id": 1, "priority": 2},
            {"id": 2, "priority": 1},
            {"id": 3, "priority": 2},
        ]
        ordenado = stable_merge_sort(data, "ASC")
        self.assertEqual([x["id"] for x in ordenado], [2, 1, 3])

    def test_merge_sort_desc(self):
        data = [
            {"id": 1, "priority": 2},
            {"id": 2, "priority": 1},
            {"id": 3, "priority": 2},
        ]
        ordenado = stable_merge_sort(data, "DESC")
        self.assertEqual([x["id"] for x in ordenado], [1, 3, 2])

    def test_orden_invalido(self):
        data = [
            {"id": 1, "priority": 1},
            {"id": 2, "priority": 2},
        ]
        with self.assertRaises(ValueError):
            stable_merge_sort(data, "UP")

    def test_flujo_completo(self):
        data = [
            {"id": 1, "weight": 3, "width": 3, "priority": 5},
            {"id": 2, "weight": 1, "width": 3, "priority": 0},
            {"id": 3, "weight": 3, "width": 3, "priority": -1},
        ]

        filtros = [("weight", "=", 3), ("width", ">", 2)]

        resultado = procesar(
            data,
            filtros,
            "ASC",
            cumple_todos_los_filtros,
            stable_merge_sort,
        )

        # Filtrados: [1,3] -> orden ASC => [3,1]
        # Restante: [2]
        self.assertEqual([x["id"] for x in resultado], [3, 1, 2])


if __name__ == "__main__":
    unittest.main()