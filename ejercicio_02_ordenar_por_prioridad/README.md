# Ejercicio 02 — Ordenamiento por prioridad con filtros dinámicos

## Descripción

Dado un arreglo de diccionarios, se debe:

1. Filtrar elementos según N filtros dinámicos.
2. Ordenar únicamente los elementos filtrados por el campo `priority`.
3. Permitir orden ASC o DESC.
4. Conservar el orden original de los elementos no filtrados.
5. Retornar una lista final compuesta por:

   [Filtrados ordenados] + [Restantes sin alterar orden]

---

## Arquitectura de la solución

La solución se divide en tres módulos principales:

### 1. filtros.py

Función principal:

```
cumple_todos_los_filtros(item, filtros)
```

Evalúa filtros dinámicos con operadores:

`=`, `!=`, `>`, `<`, `>=`, `<=`

Formato:

```
[
    ("campo", "operador", valor)
]
```

---

### 2. prioridad.py

Función principal:

```
particion_estable(data, filtros, cumple_todos_los_filtros)
```

Divide en:

- filtrados
- restantes

Mantiene orden original.

Incluye:

`procesar(...)` → Orquesta partición + ordenamiento + concatenación.

---

### 3. ordenamiento.py

Función principal:

```
stable_merge_sort(items, order)
```

- Implementación manual de Merge Sort.
- Ordena por `priority`.
- Si no existe `priority`, se considera `0`.
- Garantiza estabilidad:
  - En empate conserva el orden original.

Complejidad: `O(n log n)`

---

## Flujo general

1. Recibir data
2. Aplicar filtros
3. Ordenar solo los filtrados
4. Concatenar con restantes
5. Retornar resultado final

---

## Ejecución

`python3 main.py`

---

## Pruebas unitarias

`python3 test_prioridad.py`

Valida filtros, orden ASC/DESC, orden inválido y flujo completo.

---

## Resultado esperado

La salida cumple:
`[Filtrados ordenados] + [Restantes en orden original]`

Se garantiza:

- Estabilidad
- Separación de responsabilidades
- Código limpio y reutilizable
