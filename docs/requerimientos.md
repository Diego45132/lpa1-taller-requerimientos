
# 📋 Listado de Requerimientos

### 1. Registro de Hoteles

* **REQ-001:** El sistema debe permitir registrar un hotel con los siguientes datos obligatorios: nombre, dirección, teléfono, correo electrónico y ubicación geográfica.
  *Criterio de aceptación:* Al guardar un hotel, el sistema valida que todos los campos obligatorios estén completos y la ubicación se almacene en formato estándar (ej. coordenadas o ciudad/país).

* **REQ-002:** El sistema debe permitir registrar una descripción detallada de los servicios ofrecidos por el hotel (ej. restaurante, piscina, gimnasio, coworking).
  *Criterio de aceptación:* La descripción debe ser visible en el perfil público del hotel.

* **REQ-003:** El sistema debe permitir asociar fotos al registro de cada hotel.
  *Criterio de aceptación:* Se puede cargar al menos una foto y esta debe mostrarse en la vista pública del hotel.

* **REQ-004:** El sistema debe permitir registrar ofertas y promociones asociadas al hotel (ej. descuentos de temporada, paquetes especiales, estacionamiento gratuito).
  *Criterio de aceptación:* El sistema debe permitir definir vigencia y condiciones de la promoción.

---

### 2. Gestión de Habitaciones

* **REQ-005:** El sistema debe permitir registrar habitaciones con los siguientes datos: tipo, descripción, precio, servicios incluidos, capacidad y fotos.
  *Criterio de aceptación:* Toda habitación debe estar asociada a un hotel previamente registrado.

* **REQ-006:** El sistema debe permitir establecer el estado de una habitación como *activa* o *inactiva* (por mantenimiento, remodelación, limpieza, desinfección).
  *Criterio de aceptación:* Una habitación inactiva no debe aparecer disponible para reserva.

* **REQ-007:** Cada habitación debe tener un calendario de disponibilidad que muestre fechas ocupadas y libres.
  *Criterio de aceptación:* El calendario debe actualizarse automáticamente al confirmarse una reserva.

---

### 3. Precios y Temporadas

* **REQ-008:** El sistema debe permitir definir precios de habitaciones en función de:
  a) número de personas (respetando la capacidad máxima),
  b) temporada (alta, baja, intermedia).
  *Criterio de aceptación:* El precio mostrado en la búsqueda debe corresponder al cálculo de estas condiciones.

* **REQ-009:** El sistema debe permitir la configuración de calendarios de temporada a nivel regional y por hotel.
  *Criterio de aceptación:* El calendario del hotel debe poder ajustarse al calendario regional sin contradicciones.

---

### 4. Estados de Hoteles

* **REQ-010:** El sistema debe permitir establecer el estado del hotel como *activo* o *inactivo* (ej. reformas, cierre temporal).
  *Criterio de aceptación:* Un hotel inactivo no debe aceptar reservas.

---

### 5. Pagos y Cancelaciones

* **REQ-011:** El sistema debe permitir configurar políticas de pago por hotel (ej. pago completo anticipado, pago en el check-in).
  *Criterio de aceptación:* La política seleccionada debe mostrarse antes de confirmar la reserva.

* **REQ-012:** El sistema debe permitir configurar políticas de cancelación por hotel y por tipo de habitación (ej. reembolso completo, penalidad, no reembolsable).
  *Criterio de aceptación:* Al cancelar una reserva, el sistema debe aplicar automáticamente la política correspondiente.

* **REQ-013:** El sistema debe gestionar reembolsos de acuerdo con la política de cancelación definida.
  *Criterio de aceptación:* El reembolso debe reflejarse en el historial de transacciones del cliente.

---

### 6. Registro de Clientes

* **REQ-014:** El sistema debe permitir registrar clientes con los siguientes datos obligatorios: nombre completo, número de teléfono, correo electrónico y dirección.
  *Criterio de aceptación:* El sistema valida formato de correo electrónico y número de teléfono.

---

### 7. Búsqueda y Reserva de Habitaciones

* **REQ-015:** El sistema debe permitir a los clientes buscar habitaciones por uno o más criterios: fecha, ubicación, calificación, precio.
  *Criterio de aceptación:* El motor de búsqueda debe retornar solo habitaciones activas y disponibles en las fechas solicitadas.

* **REQ-016:** El sistema debe mostrar los detalles de la habitación seleccionada: descripción, características, servicios incluidos, fotos, calificación y comentarios de otros huéspedes.
  *Criterio de aceptación:* La información debe coincidir con la registrada en el sistema.

* **REQ-017:** El sistema debe permitir al cliente confirmar la reserva y proceder al pago en línea según la política del hotel.
  *Criterio de aceptación:* La reserva solo se confirma si el pago es exitoso.

---

### 8. Calificaciones y Comentarios

* **REQ-018:** El sistema debe permitir a los clientes calificar su estancia y dejar comentarios después de completar una reserva.
  *Criterio de aceptación:* Solo clientes con reservas finalizadas pueden calificar.

* **REQ-019:** El sistema debe calcular una calificación promedio por habitación y por hotel, basada en las evaluaciones recibidas.
  *Criterio de aceptación:* La calificación promedio debe actualizarse en tiempo real al registrarse una nueva reseña.

