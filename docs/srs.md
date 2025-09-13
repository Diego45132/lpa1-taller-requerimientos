
## 1. Introducción

### 1.1 Propósito

El presente documento especifica los requerimientos funcionales y no funcionales del Sistema de Gestión de Reservas Hoteleras. Su propósito es definir de manera clara, completa y verificable las funcionalidades necesarias para que el sistema permita a los hoteles registrar su información, gestionar habitaciones, precios, temporadas, políticas de pago y cancelación, así como permitir a los clientes realizar búsquedas, reservas y evaluaciones.

### 1.2 Alcance

El sistema permitirá a los hoteles:

* Registrar información de sus instalaciones, habitaciones y servicios.
* Administrar precios, temporadas, políticas de pago y cancelación.
* Gestionar la disponibilidad de habitaciones y estados de operación.

El sistema permitirá a los clientes:

* Registrarse en la plataforma.
* Buscar y reservar habitaciones de acuerdo con criterios múltiples.
* Realizar pagos en línea y gestionar cancelaciones.
* Calificar y dejar comentarios sobre su estancia.

El sistema estará disponible como aplicación web responsiva, accesible desde dispositivos móviles y de escritorio.

### 1.3 Definiciones, Acrónimos y Abreviaturas

* **PMS:** Property Management System.
* **Reserva Activa:** Reserva confirmada con pago válido.
* **Hotel Activo/Inactivo:** Estado que determina si el hotel está disponible para reservas.
* **Habitación Activa/Inactiva:** Estado que determina si una habitación puede ser reservada.

### 1.4 Referencias

* Entrevista con Luciana y Felipe (Administradores turísticos del hotel).
* IEEE 830 – Recommended Practice for Software Requirements Specifications.

---

## 2. Descripción General

### 2.1 Perspectiva del Producto

El sistema reemplaza y mejora los procesos manuales o parciales de gestión de reservas, centralizando información de hoteles, habitaciones, clientes y transacciones. Se integrará con un módulo de pasarela de pagos para gestionar cobros y reembolsos.

### 2.2 Funcionalidades del Producto

* Registro de hoteles y habitaciones.
* Administración de precios, temporadas y promociones.
* Definición de políticas de pago y cancelación.
* Gestión de disponibilidad mediante calendarios.
* Registro y autenticación de clientes.
* Motor de búsqueda avanzado de habitaciones.
* Proceso de reserva y pago en línea.
* Registro de calificaciones y comentarios.

### 2.3 Usuarios y Características

* **Administrador del hotel:** Encargado de registrar información, actualizar disponibilidad, definir políticas y gestionar promociones.
* **Cliente:** Usuario final que busca, reserva, paga y califica.
* **Administrador del sistema (interno):** Mantiene y supervisa el correcto funcionamiento de la plataforma.

### 2.4 Restricciones

* El sistema debe estar disponible en español como idioma principal.
* Compatible con navegadores modernos (Chrome, Firefox, Edge, Safari).
* Integración con al menos una pasarela de pago estándar (ej. Stripe, PayPal).

### 2.5 Suposiciones y Dependencias

* Se asume que cada hotel cuenta con personal capacitado para ingresar información correcta y actualizada.
* La disponibilidad del sistema depende de servicios externos como pasarela de pagos y servicio de correo electrónico.

---

## 3. Requerimientos Específicos

### 3.1 Requerimientos Funcionales

(ya elaborados en detalle y numerados)

* **REQ-001 a REQ-019** (incluyen registro de hoteles, habitaciones, precios, temporadas, estados, pagos, cancelaciones, clientes, búsquedas, reservas y calificaciones).

### 3.2 Requerimientos No Funcionales

* **RNF-001 (Seguridad):** El sistema debe cifrar datos sensibles (contraseñas, información de pago) usando estándares de la industria (ej. AES-256, TLS 1.3).
* **RNF-002 (Disponibilidad):** El sistema debe estar disponible al menos el 99,5% del tiempo mensual.
* **RNF-003 (Escalabilidad):** El sistema debe soportar hasta 5.000 usuarios concurrentes sin degradación significativa del rendimiento.
* **RNF-004 (Usabilidad):** La interfaz debe ser responsiva y accesible, cumpliendo con los estándares WCAG 2.1 AA.
* **RNF-005 (Mantenibilidad):** El código debe estar modularizado y documentado para facilitar futuras actualizaciones.
* **RNF-006 (Rendimiento):** Las búsquedas deben retornar resultados en menos de 2 segundos en condiciones de carga normal.
* **RNF-007 (Compatibilidad):** Debe funcionar en dispositivos móviles (Android/iOS) y navegadores de escritorio.

### 3.3 Criterios de Aceptación Generales

* Cada requerimiento funcional debe ser verificable mediante pruebas unitarias y de aceptación.
* El sistema debe permitir trazabilidad desde la necesidad de negocio hasta la prueba ejecutada.

---

## 4. Anexos

* Diagramas de flujo de procesos (a elaborar en siguiente fase).
* Mockups de pantallas de registro, búsqueda y reserva (fase de diseño).

