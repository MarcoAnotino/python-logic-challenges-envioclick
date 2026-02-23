# Ejercicio 1 — Contar ocurrencias en un párrafo

## Descripción

Dado un **párrafo** y un **texto**, el programa cuenta cuántas veces aparece el texto dentro del párrafo.

### Criterio de conteo

1. Comparación **insensible a mayúsculas/minúsculas**.
2. Solo se cuentan **coincidencias completas** (no subcadenas).
3. La coincidencia debe estar delimitada por:
   - Inicio/fin de la cadena, o
   - Un carácter separador (espacio, puntuación, etc.).

4. La comparación se realiza carácter por carácter.

---

## Arquitectura de la solución

### 1. ocurrencias.py

Función principal:

```
contar_ocurrencias(parrafo, texto)
```

- Normaliza ambos textos a minúsculas.
- Recorre el párrafo carácter por carácter.
- Verifica coincidencia manual.
- Valida límites de palabra usando:
  `es_separador(caracter)`

---

## Flujo general

1. Recibir `parrafo` y `texto`
2. Comparar carácter por carácter
3. Validar límites de palabra
4. Contar coincidencias válidas
5. Retornar total

---

## Ejecución

`python3 main.py`

---

## Pruebas unitarias

`python3 test_ocurrencias.py`

---

## Complejidad

- Tiempo: `O(n × m)`
- Espacio: `O(1)`

---

## Resultado esperado

Devuelve el número de coincidencias válidas del texto como palabra completa, respetando todas las restricciones del ejercicio.
