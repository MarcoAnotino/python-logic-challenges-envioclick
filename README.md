# Python Backend Logic Challenge

Caso Práctico Backend — Prueba técnica de habilidades y lógica en **Python 3.13**.

Este repositorio contiene tres ejercicios resueltos de manera independiente, cada uno con:

- Punto de entrada propio (`main.py`)
- Pruebas unitarias
- Documentación específica por ejercicio
- Cumplimiento estricto de restricciones técnicas

---

## Reglas cumplidas

- Python **3.13**
- Sin librerías externas (solo librería estándar)
- Sin funciones facilitadoras prohibidas:
  - `in`
  - `find`
  - `index`
  - `sort`
  - `sorted`
  - Expresiones regulares

- Implementaciones manuales donde fue requerido
- Código alineado a estándares **PEP8**
- Uso de tipado estático
- Documentación con **docstrings**
- Separación clara de responsabilidades
- Pruebas unitarias con `unittest`

---

# Estructura del repositorio

```
.
├── ejercicio_01_contar_ocurrencias/
│   ├── main.py
│   ├── ocurrencias.py
│   ├── test_ocurrencias.py
│   └── README.md
│
├── ejercicio_02_ordenar_por_prioridad/
│   ├── main.py
│   ├── filtros.py
│   ├── ordenamiento.py
│   ├── input.py
│   ├── prioridad.py
│   ├── test_prioridad.py
│   └── README.md
│
├── ejercicio_03_hoja_excel/
│   ├── main.py
│   ├── hoja_excel.py
│   ├── test_hoja_excel.py
│   └── README.md
│
├── .gitignore
└── README.md
```

Cada ejercicio es completamente independiente.

---

# Ejercicio 01 — Contar ocurrencias

Implementación manual para contar ocurrencias completas de una palabra dentro de un párrafo.

Características:

- Comparación carácter por carácter
- Insensible a mayúsculas/minúsculas
- Validación de límites de palabra
- Sin uso de `in`, `find`, `index`, etc.

### Ejecutar

```
python3 ejercicio_01_contar_ocurrencias/main.py
```

### Pruebas

```
python3 ejercicio_01_contar_ocurrencias/test_ocurrencias.py
```

---

# Ejercicio 02 — Ordenamiento por prioridad con filtros dinámicos

Sistema que:

1. Filtra elementos según N filtros dinámicos.
2. Ordena solo los elementos filtrados por `priority`.
3. Permite orden ASC / DESC.
4. Mantiene estabilidad.
5. Conserva el orden original de los elementos no filtrados.

Incluye implementación manual de **Merge Sort estable**.

### Ejecutar

```
python3 ejercicio_02_ordenar_por_prioridad/main.py
```

### Pruebas

```
python3 ejercicio_02_ordenar_por_prioridad/test_prioridad.py
```

---

# Ejercicio 03 — Representación básica de hoja de Excel

Clase que simula una hoja con:

- Inserción de celdas
- Actualización de celdas
- Validación de contenido
- Preview completo
- Suma por fila
- Suma por columna

Sin uso de funciones prohibidas y con validaciones robustas.

### Ejecutar

```
python3 ejercicio_03_hoja_excel/main.py
```

### Pruebas

```
python3 ejercicio_03_hoja_excel/test_hoja_excel.py
```

---

# Pruebas unitarias

Todos los ejercicios incluyen pruebas con `unittest`.

Las pruebas cubren:

- Casos nominales
- Casos límite
- Manejo de errores
- Validación de restricciones

---

# Diseño y principios aplicados

- Separación de responsabilidades
- Encapsulamiento
- Validaciones defensivas
- Manejo explícito de errores
- Algoritmos implementados manualmente cuando fue requerido
- Complejidad controlada
- Código legible y mantenible
