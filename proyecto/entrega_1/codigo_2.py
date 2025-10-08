"""
Kiosco Aurelion - Sistema de Gestión
Este programa permite visualizar y gestionar la estructura de datos de un kiosco
a través de una interfaz de consola interactiva.

Autor: [Tu nombre]
Fecha: Octubre 2025
"""

from typing import Dict, Any
from dataclasses import dataclass
from enum import Enum
import sys
from colorama import init, Fore, Style

# Inicializar colorama para colores en la consola
init()

class EscalaMedicion(Enum):
    """Tipos de escalas de medición disponibles"""
    NOMINAL = "nominal"
    ORDINAL = "ordinal"
    INTERVALO = "intervalo"
    RATIO = "ratio"

@dataclass
class CampoTabla:
    """Estructura para definir campos de las tablas"""
    tipo: str
    escala: EscalaMedicion
    descripcion: str = ""

# Definición de la estructura de las tablas
ESTRUCTURA_PRODUCTOS = {
    'id_producto': CampoTabla('int', EscalaMedicion.NOMINAL, 'Identificador único del producto'),
    'nombre': CampoTabla('str', EscalaMedicion.NOMINAL, 'Nombre del producto'),
    'precio': CampoTabla('float', EscalaMedicion.RATIO, 'Precio unitario del producto'),
    'categoria': CampoTabla('str', EscalaMedicion.NOMINAL, 'Categoría del producto'),
    'stock': CampoTabla('int', EscalaMedicion.RATIO, 'Cantidad disponible')
}

ESTRUCTURA_CLIENTES = {
    'id_cliente': CampoTabla('int', EscalaMedicion.NOMINAL, 'Identificador único del cliente'),
    'nombre': CampoTabla('str', EscalaMedicion.NOMINAL, 'Nombre completo del cliente'),
    'email': CampoTabla('str', EscalaMedicion.NOMINAL, 'Correo electrónico del cliente'),
    'telefono': CampoTabla('str', EscalaMedicion.NOMINAL, 'Número de contacto')
}

ESTRUCTURA_VENTAS = {
    'id_venta': CampoTabla('int', EscalaMedicion.NOMINAL, 'Identificador único de la venta'),
    'id_cliente': CampoTabla('int', EscalaMedicion.NOMINAL, 'Cliente que realizó la compra'),
    'fecha': CampoTabla('datetime', EscalaMedicion.ORDINAL, 'Fecha y hora de la venta'),
    'total': CampoTabla('float', EscalaMedicion.RATIO, 'Monto total de la venta')
}

class DocumentacionKiosco:
    """Clase para manejar la documentación del sistema"""
    
    @staticmethod
    def tema_problema_solucion() -> str:
        return f"""{Fore.CYAN}
## 1. Tema, Problema y Solución{Style.RESET_ALL}

{Fore.GREEN}Tema:{Style.RESET_ALL} 
Sistema de gestión para kiosco "Aurelion"

{Fore.GREEN}Problema:{Style.RESET_ALL}
- Necesidad de gestionar inventario de productos
- Control de ventas y clientes
- Seguimiento de transacciones

{Fore.GREEN}Solución:{Style.RESET_ALL}
Sistema interactivo que permite:
- Visualizar estructura de datos
- Gestionar información de productos, clientes y ventas
- Consultar documentación técnica
"""

    @staticmethod
    def dataset_referencia() -> str:
        return f"""{Fore.CYAN}
## 2. Dataset de Referencia{Style.RESET_ALL}

{Fore.GREEN}Fuente:{Style.RESET_ALL} Datos generados con fines educativos
{Fore.GREEN}Definición:{Style.RESET_ALL} Base que representa la gestión de un kiosco

{Fore.YELLOW}Estructura de Tablas:{Style.RESET_ALL}

1. Productos (productos.xlsx):
   - Almacena información de los productos disponibles
   - Aproximadamente 100 registros
   
2. Clientes (clientes.xlsx):
   - Registro de clientes del kiosco
   - Datos de contacto y seguimiento
   
3. Ventas (ventas.xlsx):
   - Registro de transacciones
   - Relación entre productos y clientes
"""

    @staticmethod
    def mostrar_estructura_tabla(nombre: str, estructura: Dict[str, CampoTabla]) -> str:
        resultado = f"\n{Fore.YELLOW}Estructura de {nombre}:{Style.RESET_ALL}\n"
        resultado += f"\n{'Campo':<15} {'Tipo':<10} {'Escala':<10} {'Descripción':<30}\n"
        resultado += "-" * 65 + "\n"
        
        for campo, info in estructura.items():
            resultado += f"{campo:<15} {info.tipo:<10} {info.escala.value:<10} {info.descripcion:<30}\n"
        
        return resultado

    @staticmethod
    def informacion_tecnica() -> str:
        return f"""{Fore.CYAN}
## 3. Información Técnica{Style.RESET_ALL}

{Fore.GREEN}Pseudocódigo:{Style.RESET_ALL}

1. INICIAR_PROGRAMA
2. MIENTRAS opcion != salir:
   2.1 MOSTRAR_MENU_PRINCIPAL
   2.2 LEER opcion
   2.3 SEGÚN opcion:
       - 1: MOSTRAR_TEMA_PROBLEMA
       - 2: MOSTRAR_DATASET
       - 3: MOSTRAR_ESTRUCTURAS
       - 4: MOSTRAR_AYUDA
       - 0: SALIR
3. FIN

{Fore.GREEN}Diagrama de Flujo:{Style.RESET_ALL}
El diagrama de flujo se encuentra en el archivo 'diagrama.png'
"""

    @staticmethod
    def ayuda_copilot() -> str:
        return f"""{Fore.CYAN}
## 4. Uso de Copilot{Style.RESET_ALL}

{Fore.GREEN}Mejoras implementadas con Copilot:{Style.RESET_ALL}

1. Estructuración del código:
   - Uso de dataclasses para definir estructuras
   - Implementación de enumeraciones
   
2. Documentación:
   - Docstrings generados automáticamente
   - Comentarios explicativos
   
3. Manejo de errores:
   - Implementación de try-except
   - Validaciones de entrada

{Fore.GREEN}Sugerencias aceptadas:{Style.RESET_ALL}
- Uso de tipos de datos estáticos
- Implementación de clases para mejor organización
- Uso de colorama para mejor visualización
"""

class MenuKiosco:
    """Clase para manejar la interfaz del menú"""
    
    def __init__(self):
        self.doc = DocumentacionKiosco()
        self.opciones = {
            1: ("Tema, Problema y Solución", self.doc.tema_problema_solucion),
            2: ("Dataset de Referencia", self.doc.dataset_referencia),
            3: ("Estructura Productos", lambda: self.doc.mostrar_estructura_tabla("Productos", ESTRUCTURA_PRODUCTOS)),
            4: ("Estructura Clientes", lambda: self.doc.mostrar_estructura_tabla("Clientes", ESTRUCTURA_CLIENTES)),
            5: ("Estructura Ventas", lambda: self.doc.mostrar_estructura_tabla("Ventas", ESTRUCTURA_VENTAS)),
            6: ("Información Técnica", self.doc.informacion_tecnica),
            7: ("Ayuda y Copilot", self.doc.ayuda_copilot)
        }

    def mostrar_menu(self) -> None:
        """Muestra el menú principal"""
        print(f"\n{Fore.CYAN}=== Menú Principal ==={Style.RESET_ALL}")
        for num, (nombre, _) in self.opciones.items():
            print(f"{num}) {nombre}")
        print("0) Salir")

    def ejecutar(self) -> None:
        """Ejecuta el bucle principal del programa"""
        while True:
            try:
                self.mostrar_menu()
                opcion = input(f"\n{Fore.GREEN}Seleccione una opción: {Style.RESET_ALL}")
                
                if opcion == "0":
                    print(f"\n{Fore.YELLOW}¡Gracias por usar el sistema!{Style.RESET_ALL}")
                    break
                
                opcion = int(opcion)
                if opcion in self.opciones:
                    print(self.opciones[opcion][1]())
                else:
                    print(f"{Fore.RED}Error: Opción no válida{Style.RESET_ALL}")
                    
            except ValueError:
                print(f"{Fore.RED}Error: Por favor ingrese un número válido{Style.RESET_ALL}")
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}Programa terminado por el usuario{Style.RESET_ALL}")
                sys.exit(0)
            except Exception as e:
                print(f"{Fore.RED}Error inesperado: {str(e)}{Style.RESET_ALL}")

def main():
    """Función principal del programa"""
    try:
        print(f"""{Fore.CYAN}
╔══════════════════════════════════════╗
║     Bienvenido a Kiosco Aurelion     ║
║      Sistema de Gestión v2.0.0       ║
╚══════════════════════════════════════╝
{Style.RESET_ALL}""")
        
        menu = MenuKiosco()
        menu.ejecutar()
        
    except Exception as e:
        print(f"{Fore.RED}Error crítico: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()