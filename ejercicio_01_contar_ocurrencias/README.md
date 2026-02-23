# Ejercicio 1 — Contar ocurrencias en un párrafo

## Descripción

Dado un **párrafo** y un **texto**, el programa cuenta cuántas veces aparece el texto dentro del párrafo.

### Criterio de conteo

- La búsqueda es **insensible a mayúsculas/minúsculas** (se normaliza con `lower()`).
- Se cuentan **ocurrencias como palabra completa**, es decir:
  - Debe existir un **separador** antes y después de la coincidencia (o ser inicio/fin del párrafo).
  - Separadores considerados: espacio, tabulaciones/saltos de línea, signos de puntuación y algunos símbolos (`. , ; : ¡ ! ¿ ? ( ) " ' -`).
- No se usan funciones prohibidas para búsqueda como `in`, `find`, `index`, expresiones regulares, etc.  
  La comparación se realiza carácter por carácter.

---

## Archivos

- `ocurrencias.py`: contiene la lógica (`es_separador` y `contar_ocurrencias`).
- `main.py`: punto de entrada por consola.
- `test_ocurrencias.py`: pruebas unitarias con `unittest` (módulo estándar de Python).

---

## Requisitos

- Python **3.13**
- No requiere dependencias externas (solo librería estándar).

---

## Ejecución

Desde la carpeta `ejercicio_01_contar_ocurrencias/`:

```bash
python3 main.py
```
