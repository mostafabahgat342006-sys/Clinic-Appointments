
# P4 - Candidate Classes

## Project: Doctor Appointment Booking System

## Candidate Classes Identification

The following candidate classes were identified from requirements R1-R7 and use cases UC1-UC3.

| Candidate Class | Evidence | Classification | Decision |
|---|---|---|---|
| Patient | R1, R2, R4: A patient views availability, books appointments, and has a booking limit. | Explicit | Accepted |
| Doctor | R1, R3: A doctor has available time slots and accepts or declines appointment requests. | Explicit | Accepted |
| Appointment | R2, R3, R4: Appointments are booked, reviewed, and counted. | Explicit | Accepted |
| TimeSlot | R1, R2: The system displays and books available time slots. | Inferred | Accepted |
| AppointmentSystem | UC1, UC2, UC3: The system coordinates availability, booking, and appointment responses. | Inferred | Accepted |
| MedicalRecord | R5: Patient medical data must be accessible only to authorized staff. | Inferred | Rejected - Not needed as a separate class in the simple booking implementation. |
| Notification | UC2, UC3: The system displays booking confirmation and updated status. | Inferred | Rejected - Messages can be displayed directly by the system. |
| MobileInterface | R7: The application must be usable on mobile phone screens. | Inferred | Rejected - This is a usability constraint, not a core domain class. |

## Selected Classes

### 1. Patient
Represents a patient who can view doctor availability and request appointments.

Responsibilities:
- Store patient information.
- Keep track of upcoming appointments.

### 2. Doctor
Represents a doctor who provides available appointment times and responds to requests.

Responsibilities:
- Maintain available time slots.
- Accept or decline appointment requests.

### 3. Appointment
Represents an appointment request between a patient and a doctor.

Responsibilities:
- Store appointment details.
- Track appointment status: Pending, Accepted, or Declined.

### 4. TimeSlot
Represents a specific available date and time for an appointment.

Responsibilities:
- Store date and time.
- Track whether the slot is available.

### 5. AppointmentSystem
Coordinates the main booking operations.

Responsibilities:
- Display doctor availability.
- Check the maximum appointment limit (N = 3).
- Create appointment requests.
- Update appointment status.

## Rejected Candidates

- MedicalRecord: Not required as a separate class for the minimal appointment booking workflow. Requirement R5 remains a security constraint.
- Notification: Confirmation and status messages can be handled by AppointmentSystem.
- MobileInterface: Mobile usability is a non-functional requirement rather than a separate domain class.

## Conclusion

Five classes are selected for the initial class diagram:

1. Patient
2. Doctor
3. Appointment
4. TimeSlot
5. AppointmentSystem

These classes will be used consistently in P5 (Class Diagram), P6 (Sequence Diagram), and P7 (Implementation).
