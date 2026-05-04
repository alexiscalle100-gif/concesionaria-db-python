# 🚗 Sistema de Concesionario de Autos

## Índice

* Introducción
* Objetivo del proyecto
* Justificación académica y técnica
* Análisis del repositorio de referencia
* Delimitación del alcance del proyecto
* Requerimientos del sistema
* Reglas de negocio
* Propuesta de modelo de datos
* Referencias
* Conclusión
* Anexos

---

## 1. Introducción

El presente documento desarrolla una propuesta formal para la asignatura Base de Datos II, orientada al diseño de un sistema de información para un concesionario de autos. La finalidad principal es estructurar una base de datos relacional que permita gestionar de manera eficiente la venta de vehículos, el control de clientes, la administración de empleados y los procesos de financiamiento.

El sistema busca representar fielmente las operaciones reales de un concesionario, asegurando consistencia, integridad y trazabilidad de la información.

---

## 2. Objetivo del proyecto

Diseñar e implementar una base de datos relacional para un concesionario de autos, capaz de registrar y gestionar clientes, empleados, vehículos, ventas y financiamiento.

### Objetivos específicos:

* Identificar requerimientos del sistema.
* Definir reglas de negocio claras.
* Diseñar un modelo entidad-relación normalizado.
* Implementar la base de datos en PostgreSQL.
* Realizar consultas SQL para análisis de ventas.

---

## 3. Justificación académica y técnica

El sistema de concesionario de autos representa un escenario real con una estructura de datos rica en relaciones, lo que permite aplicar conceptos fundamentales del modelado relacional.

Este tipo de sistema incluye:

* Gestión de empleados con jerarquía organizacional.
* Control de inventario de vehículos.
* Registro detallado de ventas.
* Procesos de financiamiento y pagos.

Esto lo convierte en un caso adecuado para demostrar competencias en:

* Diseño de bases de datos
* Normalización
* Integridad referencial
* Consultas SQL complejas

---

## 4. Análisis del repositorio de referencia

Repositorio analizado:
http://127.0.0.1:8000/admin/ventas/venta/

El repositorio proporciona una estructura base para sistemas de ventas, de la cual se adaptan los siguientes conceptos:

* Registro de clientes
* Gestión de transacciones (ventas)
* Manejo de detalle de ventas

Para el sistema de concesionario, se amplía el modelo incorporando:

* Gestión de empleados
* Jerarquía organizacional
* Vehículos en lugar de productos
* Financiamiento y pagos

---

## 5. Delimitación del alcance del proyecto

### 5.1 Alcance incluido

* Registro y gestión de clientes
* Gestión de autos (inventario)
* Gestión de empleados y cargos
* Registro de ventas
* Asociación de autos a ventas
* Gestión de financiamiento
* Registro de pagos
* Consultas de análisis de ventas

### 5.2 Alcance excluido

* Gestión de sucursales múltiples
* Módulo de compras a proveedores
* Facturación electrónica
* Seguridad avanzada
* Integraciones externas

---

## 6. Requerimientos del sistema

### 6.1 Requisitos funcionales

* El sistema debe permitir registrar clientes.
* El sistema debe permitir registrar autos disponibles.
* El sistema debe permitir registrar empleados y sus cargos.
* El sistema debe permitir generar ventas.
* El sistema debe permitir asociar autos a una venta.
* El sistema debe permitir gestionar financiamiento.
* El sistema debe permitir registrar pagos.

### 6.2 Requisitos no funcionales

* Implementación en PostgreSQL (PGAdmin).
* Uso de claves primarias y foráneas.
* Normalización hasta tercera forma normal (3FN).
* Integridad de datos garantizada.
* Consultas reproducibles.

---

## 7. Reglas de negocio

* Un cliente puede realizar una o varias ventas.
* Un empleado (vendedor) puede realizar múltiples ventas.
* Cada empleado pertenece a un cargo.
* Existe jerarquía organizacional entre empleados (supervisor/jefe).
* Un auto solo puede venderse una vez.
* Una venta puede incluir uno o varios autos.
* Una venta puede ser al contado o financiada.
* Si la venta es financiada, se generan pagos asociados.
* Los autos tienen estado (disponible/vendido).
* No se eliminan registros históricos.

---

## 8. Propuesta de modelo de datos

### 8.1 Entidades principales

* cliente
* empleado
* cargo
* auto
* categoria
* venta
* detalle_venta
* financiamiento
* pago

---

### 8.2 Relaciones principales

* Cliente (1) → (N) Venta
* Empleado (1) → (N) Venta
* Empleado (1) → (N) Empleado (jerarquía)
* Cargo (1) → (N) Empleado
* Venta (1) → (N) Detalle_Venta
* Auto (1) → (N) Detalle_Venta
* Categoría (1) → (N) Auto
* Venta (1) → (1) Financiamiento (opcional)
* Financiamiento (1) → (N) Pago

---

### 8.3 Criterio de normalización

El modelo se encuentra en tercera forma normal (3FN), garantizando:

* Eliminación de redundancia
* Separación de entidades
* Integridad referencial
* Registro histórico de precios en detalle_venta

---

## 9. Referencias

* betofleitass. django_point_of_sale. GitHub
 http://127.0.0.1:8000/admin/ventas/venta/

---

## 10. Conclusión

El sistema de concesionario de autos constituye una solución completa para la gestión de ventas de vehículos, integrando múltiples entidades y relaciones complejas.

El diseño propuesto asegura consistencia, escalabilidad y capacidad de análisis, cumpliendo con los objetivos académicos del curso.

---

## 11. Anexos

### 11.1 Diagrama ER

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/f8709d92-66d3-460d-8ad3-eae9532c7e3f" />


### 11.2 Diagrama EER

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/eb0a7970-a562-4cf5-9bef-3d491259b029" />


### 11.3 Esquema Relacional

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/77539a97-41a0-4973-9325-86f83cb8a774" />

