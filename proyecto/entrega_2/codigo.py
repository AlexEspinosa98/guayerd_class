# kiosco_Aurelion.py
# Programa en consola que muestra exactamente los textos de Documentación.md

def imprimir_seccion(op):
    if op == 1:
        print("""
## 1. Tema, problema y solución

""")

    elif op == 2:
        print("""
## 2. Dataset de referencia: fuente, definición, estructura, tipos y **escala de medición**
**Fuente:** datos generados con fines educativos.  
**Definición:** base que representa un kiosco, con catálogo de productos, registro de clientes y operaciones de venta.  

**Productos (`productos.csv`)** — ~100 filas  
| Campo             | Tipo | Escala   |
|-------------------|------|----------|
| `id_producto`     | int  | Nominal  |


**Clientes (`clientes.csv`)** — ~100 filas  
| Campo            | Tipo | Escala   |
|------------------|------|----------|
| `id_cliente`     | int  | Nominal  |


**Ventas (`ventas.csv`)** — ~120 filas  
| Campo            | Tipo | Escala    |
|------------------|------|-----------|
| `id_venta`       | int  | Nominal   |


""")

    elif op == 3:
        print("""
## 3. Información, pasos, pseudocódigo y diagrama del programa (Sprint 1)
En esta etapa, el programa funciona como un **visor interactivo de la documentación**, para que el usuario obtenga rápidamente la información clave del proyecto desde la terminal.

### 3.1 Contenidos accesibles desde el menú
1. **Tema, problema y solución.**  
2. **Dataset de referencia.** Resumen de fuente y definición.  
3. **Estructura por tabla.** Columnas, tipo y escala de medición.  
4. **Escalas de medición.** Descripción y ejemplos.  
Fin

### 3.4 Diagrama de flujo: en carpeta
""")

    elif op == 4:
        print("""
## 4. Sugerencias y mejoras aplicadas con Copilot
- Separar la documentación en **plantillas** reutilizables (por ejemplo, `textos.py`) y desacoplarla del código del menú.  
- Proveer un modo “**búsqueda**” para localizar palabras clave dentro de la documentación (e.g., “precio”, “escala”).  
- Agregar una opción “**exportar sección**” para guardar en `.txt`/`.md` lo mostrado por pantalla.  
- Incluir tests mínimos para el router de opciones (verifica que cada número abra la sección correcta).
""")
    
    elif op == 5:
        print("""
## 5. Estadísticas descriptivas (detalle_ventas)

Columnas analizadas: `cantidad`, `precio_unitario`, `importe`.

**Resultados:**

|       |   cantidad |   precio_unitario |   importe |
|:------|-----------:|------------------:|----------:|
| count |    343     |            343    |    343    |
| mean  |      2.962 |           2654.5  |   7730.08 |
| std   |      1.366 |           1308.69 |   5265.54 |
| min   |      1     |            272    |    272    |
| 25%   |      2     |           1618.5  |   3489    |
| 50%   |      3     |           2512    |   6702    |
| 75%   |      4     |           3876    |  10231.5  |
| max   |      5     |           4982    |  24865    |


**Código utilizado:**

```python
import pandas as pd
detalle = pd.read_csv('detalle_ventas....
""")

    elif op == 6:
        print("""
## 6. Correlaciones

Columnas analizadas: `cantidad`, `precio_unitario`, `importe`.

**Resultados:**

|                 |   cantidad |   precio_unitario |   importe |
|:----------------|-----------:|------------------:|----------:|
| cantidad        |      1     |            -0.074 |     0.6   |     |


**Código utilizado:**

```python
import pandas as pd
detalle = pd.read_csv('detalle_ventas.csv')
""")
        
    elif op == 7:
        print("""
## 7. Valores extremos

Para este sprint, se observan **valores muy altos o muy bajos** usando mínimos/máximos y listados ordenados.

**Mínimos y máximos:**

|   cantidad_min_val |   cantidad_max_val |   precio_unitario_min_val |   precio_unitario_max_val |   importe_min_val |   importe_max_val |
|-------------------:|-------------------:|--------------------------:|--------------------------:|------------------:|------------------:|
|                  1 |                  5 |                       272 |                      4982 |               272 |             24865 |


**Top 5 y Bottom 5 de `cantidad`:**

*Bottom 5*

|   cantidad |
|-----------:|
|          1 |
|          1 |



*Top 5*

|   cantidad |
|-----------:|
|          5 |
|          5 |



**Top 5 y Bottom 5 de `precio_unitario`:**

*Bottom 5*

|   precio_unitario |
|------------------:|
|               272 |
|               272 |



*Top 5*

|   precio_unitario |
|------------------:|
|              4982 |
|              4982 |



**Top 5 y Bottom 5 de `importe`:**

*Bottom 5*

|   importe |
|----------:|
|       272 |
|       503 |



*Top 5*

|   importe |
|----------:|
|     24865 |
|     23760 |



**Código utilizado:**

```python
import pandas as pd
detalle = pd.read_csv('detalle_ventas.csv')
....
```
""")
        
    elif op == 8:
        print("""
## 8. Gráficos

A continuación, se incluyen tres gráficos que permiten visualizar la información de la base de datos del Tienda.

### 8.1 Histograma de cantidades

```python
import pandas as pd
import matplotlib.pyplot as plt

detalle = pd.read_csv("detalle_ventas.csv")

# Histograma de cantidades
detalle["cantidad"].plot(kind="h.....
plt.xlabel("Ca.....
plt.ylabel("F...
plt.show()
```

### 8.2 Dispersión precio unitario vs importe

```python
import pandas as pd
import matplotlib.pyplot as plt

detalle = pd.read_csv("detalle_ventas.csv")

# Dispersión precio unitario vs importe
plt.sca...
plt.t....
plt.x....
plt.yl...
plt.show()
```

### 8.3 Boxplot de importes

```python
import pandas as pd
import matplotlib.pyplot as plt

detalle = pd.read_csv("detalle_ventas.csv")

# Boxplot de importes
detalle["...
plt.ylabel(...
plt.show()
```
""")
        
    elif op == 9:
        print("""
## 9. Interpretación de resultados

Al analizar los resultados de la **2° demo: asincrónica** (estadísticas descriptivas, correlaciones, valores extremos y gráficos) se observa lo siguiente:

- Las **estadísticas descriptivas** muestran que la cantidad más común de productos por venta está en torno a 2 o 3 unidades, y que el importe promedio de cada línea de venta es de aproximadamente $7.730, con una dispersión considerable

""")
        
    elif op == 10:
        print("""
## 10. Limpieza y preparación de la base de datos

Este sección describe las **operaciones realizadas** para dejar lista la base del Tienda y el **código** utilizado.

Archivos de entrada:
- `produ...
- `cli..v`
- `ve...
- `detalle...

Archivos de salida (limpios):
- `produc...
- `clie..
- `ven...v`
- `detall..

### 10.1 Operaciones aplicadas

**a. Textos y espacios**
- Quitar espacios al inicio/fin en columnas de texto de todas las tablas.
- Estandarizar forma de escritura en columnas de texto clave:
  - `categoria` (Productos) → Título (ej.: "Golosinas")
  - `ciudad` (Clientes) → Título (ej.: "Córdoba")

**b. Duplicados y faltantes**
- Eliminar filas con valores faltantes en claves mínimas:
  - Productos: `...
  - Clientes: `id_..`
  - Ventas: ...
  - Detalle_Ventas: `....
- Quitar duplicados:
  - Productos por `i..
  - Clientes por `i.
  - Ventas por ...
  - Detalle_Ventas....

**c. Fechas**
- Normalizar `fecha` (Ventas) al formato ISO `YYYY-MM-DD` (cuando es posible).

**d. Consistencia de importe**
- Asegurar `importe = cantidad * precio_unitario` en Detalle_Ventas.

**e. Corección de categorías en Productos**
- Unificar variantes/sinónimos (p. ej., “bebida”, “gaseosas” → Bebidas; “aseo” → Limpieza; “dulces/snacks” → Golosinas).

**f. Reemplazo de caracteres erróneos en todas las tablas**
- Reemplazar texto mal decodificado por letras con tilde/ñ correctas (p. ej., CÃ³rdoba → Córdoba, PeÃ±a → Peña).

### 10.2 Código

```Python
import pandas as pd

# Mapeo de categorías
CATEGORIAS_MAP = {
    "bebida": "Bebidas",....
    "limpieza": "Limp....
    "golosinas": "Golos
    "alimentos": "Ali

# Reemplazos de caracteres mal decodificados (mojibake)
REEMPLAZOS = {
    "Ã¡": "á", "Ã©": "é", "Ãí": "í", "Ã³": "ó", "Ãº": "ú",
    "ÃÁ": "Á", "Ã‰": "É", "ÃÍ": "Í", "Ã“": "Ó", "Ãš": "Ú",
    "Ã±": "ñ", "Ã‘": "Ñ",
    "Ã¼": "ü", "Ãœ": "Ü",
    "â€“": "-", "â€”": "-", "â€˜": "'", "â€™": "'",
    "â€œ": '"', "â€ ": '"',
    "Â°": "°", "Â·": "·", "Â": ""
}

def limpiar_objetos(df: pd.DataFrame) -> pd.DataFrame:
    Quita espacios y corrige caracteres extraños en columnas de texto (object).
    obj_cols = df.select_dtypes(include=["object"]).columns
    for c in obj_cols:
        #.....
    return df

# --------------------------
# 2) Carga de archivos
# --------------------------
productos = pd.read_csv("pro...
clientes  = pd.read_csv("cl..
ventas    = pd.read_csv("v...
detalle   = pd.read_csv("d...

# --------------------------
# 3) Limpieza básica de texto
# --------------------------
productos = limpiar_objetos(pro...
clientes  = limpiar_objetos(clie..
...

# --------------------------
# 4) Duplicados y faltantes
# --------------------------
if "id_producto" in productos.columns:
    productos = productos.dropna(subset=["id_producto"]).dro...

if {"id_cliente","nombre_cliente"}.issubset(clientes.columns):
    clientes = clientes.dropna(subset=["id_cliente","nombre_cli..
if {"id_venta","id_cliente"}.issubset(ventas.columns):
    ventas = ventas.dropna(subset=["id_venta","id_cliente"]).drop..

if {"id_venta","id_producto","cantidad","precio_unitario"}.issubset(detalle.columns):
    detalle = detalle.dropna(subset=["id_venta","id_produ..

# --------------------------
# 5) Fechas en ventas (ISO)
# --------------------------
if "fecha" in ventas.columns:
    ventas["fecha"] = pd.to_datetime(ventas["fecha"], errors="coerce").dt.date.astype("string")

# --------------------------
# 6) Importe consistente
# --------------------------
if {"cantidad","precio_unitario"}.issubset(detalle.columns):
    detalle["cantidad"] = pd.to_....

# --------------------------
# 7) Categorías en productos
# --------------------------
if "categoria" in productos.columns:
    # pasamos a mi...)

# --------------------------
# 8) Guardado final
# --------------------------
productos.to_csv("....
```
""")

    else:
        print("Opción inválida.")

def mostrar_menu():
    while True:
        print("\n=== Menú de secciones ===")
        print("1) Tema, problema y solución")
        print("2) Dataset de referencia")
        print("3) Información, pasos, pseudocódigo y diagrama")
        print("4) Sugerencias y mejoras")
        print("5) Estadísticas descriptivas")
        print("6) Correlaciones")
        print("7) Valores extremos")
        print("8) Gráficos")
        print("9) Interpretación de resultados")
        print("10) Limpieza y preparación de la base de datos")
        print("0) Salir")
        try:
            op = int(input("Elegí una opción: "))
        except ValueError:
            print("Entrada inválida.")
            continue
        if op == 0:
            print("Fin.")
            break
        imprimir_seccion(op)

if __name__ == "__main__":
    mostrar_menu()