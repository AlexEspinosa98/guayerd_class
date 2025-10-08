# Análisis de Base de Datos - Kiosco

## Descripción General
Este documento presenta un análisis detallado de la estructura de la base de datos utilizada en el sistema de gestión del kiosco. La base de datos está implementada en archivos Excel y contiene información sobre clientes, productos, ventas y sus detalles. Cada campo en las tablas tiene una escala de medición específica que determina qué tipos de operaciones y análisis son válidos para ese dato.

## Estructura de Tablas

### 1. Tabla: clientes.xlsx
Esta tabla almacena la información de los clientes del kiosco.

| Campo | Tipo de Dato | Escala | Uso | 
|-------|-------------|---------|-----|
| id_cliente | entero | Nominal | Identificador único de cada cliente |
| nombre | texto | Nominal | Nombre completo del cliente |
| direccion | texto | Nominal | Ubicación física del cliente |
| telefono | texto | Nominal | Número de contacto del cliente |

### 2. Tabla: productos.xlsx
Contiene el catálogo de productos disponibles en el kiosco.

| Campo | Tipo de Dato | Escala | Uso |
|-------|-------------|---------|-----|
| id_producto | entero | Nominal | Identificador único del producto |
| nombre | texto | Nominal | Nombre del producto |
| precio | decimal | Razón | Precio unitario del producto |
| categoria | texto | Nominal | Clasificación del producto |
| stock | entero | Razón | Cantidad disponible en inventario |

### 3. Tabla: ventas.xlsx
Registra las transacciones principales de venta.

| Campo | Tipo de Dato | Escala | Uso |
|-------|-------------|---------|-----|
| id_venta | entero | Nominal | Identificador único de la venta |
| id_cliente | entero | Nominal | Referencia al cliente que realizó la compra |
| fecha | fecha/hora | Intervalo | Momento de la realización de la venta |
| total | decimal | Razón | Monto total de la transacción |

### 4. Tabla: detalle_ventas.xlsx
Almacena el detalle de los productos incluidos en cada venta.

| Campo | Tipo de Dato | Escala | Uso |
|-------|-------------|---------|-----|
| id_detalle | entero | Nominal | Identificador único del detalle |
| id_venta | entero | Nominal | Referencia a la venta principal |
| id_producto | entero | Nominal | Referencia al producto vendido |
| cantidad | entero | Razón | Cantidad de unidades vendidas |
| precio_unitario | decimal | Razón | Precio por unidad al momento de la venta |

## Relaciones entre Tablas
1. ventas ⟷ clientes: A través de id_cliente
2. detalle_ventas ⟷ ventas: A través de id_venta
3. detalle_ventas ⟷ productos: A través de id_producto

## Consideraciones Técnicas
- Los archivos están en formato Excel (.xlsx)
- Cada tabla está diseñada para mantener la integridad referencial
- Se utilizan identificadores numéricos para las relaciones entre tablas
- Los campos de fecha están en formato datetime
- Los campos monetarios están en formato decimal

## Recomendaciones de Uso
1. Mantener los identificadores únicos al agregar nuevos registros
2. Respetar los tipos de datos establecidos para cada campo
3. Verificar la integridad referencial al realizar operaciones entre tablas
4. Realizar respaldos periódicos de los archivos
5. Validar los datos antes de insertarlos en las tablas