# kiosco_Aurelion.py
# Programa en consola que muestra exactamente los textos de Documentación.md

def imprimir_seccion(op):
    if op == 1:
        print("""
## 1. Tema, problema y solución
Este proyecto simula la gestión de un kiosco a partir de datos sintéticos. El objetivo es.... 
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

""")

    elif op == 3:
        print("""
## 3. Información, pasos, pseudocódigo y diagrama del programa (Sprint 1)
En esta etapa, el programa funciona como un **visor interactivo de la documentación**, para que el usuario obtenga rápidamente la información clave del proyecto desde la terminal.

### 3.1 Contenidos accesibles desde el menú


### 3.2 Pasos

### 3.3 Pseudocódigo

### 3.4 Diagrama de flujo: en carpeta
""")

    elif op == 4:
        print("""
## 4. Sugerencias y mejoras aplicadas con Copilot
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

