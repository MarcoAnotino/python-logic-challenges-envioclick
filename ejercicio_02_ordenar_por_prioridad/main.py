from filtros import cumple_todos_los_filtros
from ordenamiento import stable_merge_sort
from prioridad import particion_estable
from input import data


def main():
    filtros = [
        ("weight", "=", 3),
        ("width", ">", 2),
    ]

    order = "ASC"  # o "DESC"

    filtrados, restantes = particion_estable(data, filtros, cumple_todos_los_filtros)
    filtrados_ordenados = stable_merge_sort(filtrados, order)

    print("=== FILTRADOS ===")
    i = 0
    while i < len(filtrados_ordenados):
        item = filtrados_ordenados[i]
        try:
            pri = item["priority"]
        except KeyError:
            pri = 0
        print("id:", item["id"], "| priority:", pri)
        i += 1

    print("=== RESTANTES ===")
    j = 0
    while j < len(restantes):
        item = restantes[j]
        try:
            pri = item["priority"]
        except KeyError:
            pri = 0
        print("id:", item["id"], "| priority:", pri)
        j += 1


if __name__ == "__main__":
    main()