
# P5 - Class Diagram

## Project: Doctor Appointment Booking System

This class diagram is based on the five selected classes from P4.

```mermaid
classDiagram
    direction TB

    class Patient {
        +int patientId
        +string name
        +list appointments
        +getUpcomingAppointments()
    }

    class Doctor {
        +int doctorId
        +string name
        +list availableSlots
        +respondToRequest(appointmentId, decision)
    }

    class Appointment {
        +int appointmentId
        +int patientId
        +int doctorId
        +string slotId
        +string status
        +updateStatus(status)
    }

    class TimeSlot {
        +string slotId
        +string date
        +string time
        +bool isAvailable
    }

    class AppointmentSystem {
        +int MAX_APPOINTMENTS
        +list appointments
        +viewAvailability(doctorId)
        +bookAppointment(patientId, doctorId, slotId)
        +checkAppointmentLimit(patientId)
        +respondToRequest(appointmentId, decision)
    }

    Patient "1" --> "0..*" Appointment : requests
    Doctor "1" --> "0..*" Appointment : receives
    Doctor "1" --> "0..*" TimeSlot : offers
    Appointment "1" --> "1" TimeSlot : reserves

    AppointmentSystem ..> Patient : manages
    AppointmentSystem ..> Doctor : manages
    AppointmentSystem ..> Appointment : manages
    AppointmentSystem ..> TimeSlot : checks
```

## Class Responsibilities

| Class | Responsibility |
|---|---|
| Patient | Stores patient information and upcoming appointments. |
| Doctor | Manages available slots and responds to appointment requests. |
| Appointment | Stores booking information and its current status. |
| TimeSlot | Represents a date and time available for booking. |
| AppointmentSystem | Coordinates bookings, checks availability, and enforces N = 3. |

## Business Rules

- A patient can have at most 3 upcoming appointments (N = 3).
- A patient can request an appointment only for an available time slot.
- A doctor can accept or decline an appointment request.
- Appointment status can be Pending, Accepted, or Declined.
- Patient medical data must be accessible only to authorized staff (R5).
- Available appointment times should be displayed within 2 seconds (R6).
- The application should support mobile phone screens (R7).
