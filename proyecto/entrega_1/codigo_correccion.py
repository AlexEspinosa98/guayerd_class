"""
Tienda Aurelion - Sistema de Visualización de Documentación
Este programa implementa una interfaz de usuario en terminal para visualizar
la documentación del proyecto Tienda Aurelion.
"""

# Constantes de texto para las secciones
TEMA_PROBLEMA = """
## 1. Tema, problema y solución
Este proyecto simula la gestión de un kiosco a partir de datos sintéticos. 
El objetivo es desarrollar un sistema de gestión que permita:
- Visualizar el catálogo de productos
- Consultar información de clientes
- Ver registro de ventas
- Analizar datos de operaciones

La solución propuesta es una interfaz de línea de comandos que permite
acceder a esta información de manera rápida y eficiente."""

DATASET_INFO = """
## 2. Dataset de referencia

**Fuente:** Datos generados con fines educativos
**Definición:** Base que representa un kiosco, con:
- Catálogo de productos
- Registro de clientes
- Operaciones de venta
- Detalles de transacciones

### Estructura de archivos:
1. productos.xlsx (~100 registros)
   - id_producto (int): Identificador único
   - nombre (str): Nombre del producto
   - precio (float): Precio unitario
   - categoria (str): Categoría del producto

2. clientes.xlsx
   - id_cliente (int): Identificador único
   - nombre (str): Nombre completo
   - email (str): Correo electrónico
   - telefono (str): Número de contacto

3. ventas.xlsx
   - id_venta (int): Identificador único
   - fecha (datetime): Fecha de la venta
   - id_cliente (int): Cliente que realizó la compra

4. detalle_ventas.xlsx
   - id_venta (int): Identificador de la venta
   - id_producto (int): Producto vendido
   - cantidad (int): Unidades vendidas
   - precio_unitario (float): Precio por unidad"""

INFORMACION_PROGRAMA = """
## 3. Información del Programa

### 3.1 Contenidos del Menú
1. Tema y Solución
2. Dataset de Referencia
3. Información del Programa
4. Sugerencias y Mejoras
0. Salir

### 3.2 Pasos del Programa
1. Mostrar menú principal
2. Capturar selección del usuario
3. Validar entrada
4. Mostrar información seleccionada
5. Volver al menú o salir

### 3.3 Pseudocódigo
```
INICIO
  MIENTRAS verdadero
    MOSTRAR menú_opciones
    LEER opción
    SI opción es válida ENTONCES
      SI opción es 0
        TERMINAR programa
      SINO
        MOSTRAR información_seleccionada
      FIN SI
    SINO
      MOSTRAR mensaje_error
    FIN SI
  FIN MIENTRAS
FIN
```"""

SUGERENCIAS = """
## 4. Sugerencias y Mejoras Aplicadas

1. Estructura del Código
   - Separación de contenido en constantes
   - Documentación completa de funciones
   - Manejo robusto de errores
   - Formato mejorado de presentación

2. Interfaz de Usuario
   - Menú claro y organizado
   - Validación de entradas
   - Mensajes informativos
   - Facilidad de navegación

3. Mejoras Futuras
   - Implementar colores en terminal
   - Agregar paginación para textos largos
   - Incluir submenús para más detalles
   - Mejorar formato de presentación"""

def imprimir_seccion(opcion):
    """
    Muestra el contenido de la sección seleccionada.
    
    Args:
        opcion (int): Número de sección a mostrar
    """
    secciones = {
        1: TEMA_PROBLEMA,
        2: DATASET_INFO,
        3: INFORMACION_PROGRAMA,
        4: SUGERENCIAS
    }
    
    if opcion in secciones:
        print(secciones[opcion])
    else:
        print("Error: Opción inválida.")

def mostrar_menu():
    """
    Muestra el menú principal y maneja la interacción con el usuario.
    """
    while True:
        print("\n=== Tienda Aurelion - Sistema de Documentación ===")
        print("1) Tema, problema y solución")
        print("2) Dataset de referencia")
        print("3) Información del programa")
        print("4) Sugerencias y mejoras")
        print("0) Salir")
        print("-" * 45)
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                print("\nGracias por usar el sistema. ¡Hasta pronto!")
                break
            elif 1 <= opcion <= 4:
                imprimir_seccion(opcion)
                input("\nPresione Enter para continuar...")
            else:
                print("\nError: Por favor seleccione una opción válida (0-4)")
        except ValueError:
            print("\nError: Por favor ingrese un número válido")

if __name__ == "__main__":
    print("Bienvenido al Sistema de Documentación de Tienda Aurelion")
    mostrar_menu()
