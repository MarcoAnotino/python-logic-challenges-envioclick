# Ejercicio 03 — Representación básica de hoja de Excel

## Descripción

Se debe crear una representación básica de una hoja de Excel utilizando filas y columnas.

La solución debe implementar 6 funcionalidades principales:

1. Insertar información en una celda.
2. Actualizar información en una celda.
3. Validar si una celda contiene información.
4. Mostrar un preview completo de la hoja.
5. Dada una fila, recuperar los elementos e imprimir la suma de los valores numéricos.
6. Dada una columna, recuperar los elementos e imprimir la suma de los valores numéricos.

---

## Arquitectura de la solución

La implementación está encapsulada en una única clase:

### hoja_excel.py

Clase principal:

```
HojaExcel
```

Responsabilidades:

- Gestión de dimensiones (filas y columnas).
- Validación de coordenadas.
- Manejo interno de celdas mediante un diccionario.
- Operaciones de inserción y actualización.
- Generación de preview.
- Cálculo de sumas por fila y columna.

Internamente utiliza:

```
_celdas: dict[(fila, columna)] -> valor
```

No se utiliza `in` para validaciones; se emplea manejo de excepciones (`try / except KeyError`).

---

## Funcionalidades implementadas

### 1. Insertar valor

```
insertar(fila, columna, valor)
```

- Inserta un valor en una celda vacía.
- Lanza `ValueError` si la celda ya contiene información.

---

### 2. Actualizar valor

```
actualizar(fila, columna, valor)
```

- Modifica el valor de una celda existente.
- Lanza `ValueError` si la celda está vacía.

---

### 3. Validar si una celda contiene información

```
tiene_valor(fila, columna) -> bool
```

- Retorna `True` si la celda tiene contenido.
- Retorna `False` si está vacía.

---

### 4. Obtener valor de una celda

```
obtener(fila, columna)
```

- Retorna el valor almacenado.
- Retorna `None` si la celda está vacía.

---

### 5. Preview de la hoja completa

```
preview() -> str
```

- Genera representación textual completa.
- Las celdas vacías se muestran como `.`.
- Separación por tabulaciones.
- Cada fila separada por salto de línea.

Ejemplo:

```
10    20    60    .
6.5   .     .     .
.     .     .     7
.     .     .     .
```

---

### 6. Suma por fila

```
suma_fila(fila) -> float
```

- Recorre todas las columnas de la fila.
- Suma únicamente valores numéricos (`int` y `float`).
- Lanza `TypeError` si encuentra un valor no numérico.
- Imprime el total y lo retorna.

---

### 7. Suma por columna

```
suma_columna(columna) -> float
```

- Recorre todas las filas de la columna.
- Suma únicamente valores numéricos.
- Lanza `TypeError` si encuentra valor no numérico.
- Imprime el total y lo retorna.

---

## Flujo general

1. Crear instancia `HojaExcel(filas, columnas)`
2. Insertar valores
3. Actualizar valores si es necesario
4. Visualizar preview
5. Ejecutar sumas por fila o columna

---

## Ejecución

Desde la carpeta del ejercicio:

```
python3 main.py
```

Salida esperada:

- Preview completo
- Validaciones de celdas
- Suma por fila
- Suma por columna

---

## Pruebas unitarias

Archivo:

```
test_hoja.py
```

Ejecutar:

```
python3 test_hoja.py
```

Las pruebas validan:

- Inserción correcta
- Error al insertar en celda ocupada
- Error al actualizar celda vacía
- Preview correcto
- Suma por fila
- Suma por columna
- Error al sumar valores no numéricos
- Validación de rangos inválidos

---

## Complejidad

- Inserción / actualización: O(1)
- Validación de celda: O(1)
- Preview: O(n × m)
- Suma por fila: O(m)
- Suma por columna: O(n)

Donde:

- n = número de filas
- m = número de columnas
