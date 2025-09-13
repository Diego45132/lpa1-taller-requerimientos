
## 📌 Entidades identificadas

1. **Hotel**

   * nombre
   * dirección
   * teléfono
   * correo electrónico
   * ubicación geográfica
   * descripción servicios
   * estado (activo/inactivo)
   * fotos
   * promociones

2. **Habitación**

   * tipo
   * descripción
   * precio base
   * capacidad
   * estado (activa/inactiva)
   * servicios incluidos
   * fotos
   * calendario disponibilidad

3. **Promoción / Oferta**

   * nombre
   * descripción
   * descuento (%)
   * fecha inicio – fecha fin
   * condiciones

4. **Temporada**

   * nombre (alta, baja, etc.)
   * fecha inicio – fecha fin
   * región asociada

5. **Cliente**

   * nombre completo
   * correo electrónico
   * teléfono
   * dirección

6. **Reserva**

   * fecha inicio – fecha fin
   * estado (pendiente, confirmada, cancelada)
   * monto total
   * fecha creación

7. **Política de Pago**

   * tipo (anticipado, check-in, etc.)
   * condiciones

8. **Política de Cancelación**

   * tipo (reembolsable, parcial, no reembolsable)
   * penalidad (%)
   * condiciones

9. **Pago**

   * fecha
   * monto
   * método (tarjeta, PayPal, etc.)
   * estado

10. **Calificación / Comentario**

    * puntaje (1–5)
    * comentario
    * fecha

---

## 📐 Diagrama de Clases (Mermaid UML)

```mermaid
classDiagram
    class Hotel {
        +String nombre
        +String direccion
        +String telefono
        +String email
        +String ubicacion
        +String descripcionServicios
        +Boolean activo
        +List~Foto~ fotos
    }

    class Habitacion {
        +String tipo
        +String descripcion
        +Double precioBase
        +Integer capacidad
        +Boolean activa
        +List~String~ serviciosIncluidos
        +List~Foto~ fotos
    }

    class Promocion {
        +String nombre
        +String descripcion
        +Double descuento
        +Date fechaInicio
        +Date fechaFin
    }

    class Temporada {
        +String nombre
        +Date fechaInicio
        +Date fechaFin
        +String region
    }

    class Cliente {
        +String nombre
        +String email
        +String telefono
        +String direccion
    }

    class Reserva {
        +Date fechaInicio
        +Date fechaFin
        +String estado
        +Double montoTotal
        +Date fechaCreacion
    }

    class PoliticaPago {
        +String tipo
        +String condiciones
    }

    class PoliticaCancelacion {
        +String tipo
        +Double penalidad
        +String condiciones
    }

    class Pago {
        +Date fecha
        +Double monto
        +String metodo
        +String estado
    }

    class Calificacion {
        +Integer puntaje
        +String comentario
        +Date fecha
    }

    %% Relaciones
    Hotel "1" --> "many" Habitacion
    Hotel "1" --> "many" Promocion
    Hotel "1" --> "many" Temporada
    Hotel "1" --> "1" PoliticaPago
    Hotel "1" --> "1" PoliticaCancelacion
    Habitacion "1" --> "many" Reserva
    Cliente "1" --> "many" Reserva
    Reserva "1" --> "1" Pago
    Reserva "1" --> "many" Calificacion
```

