
class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name
        self.appointments = []


class Doctor:
    def __init__(self, doctor_id, name, available_slots):
        self.doctor_id = doctor_id
        self.name = name
        self.available_slots = available_slots


class Appointment:
    def __init__(self, appointment_id, patient, doctor, slot):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.slot = slot
        self.status = "Pending"


class TimeSlot:
    def __init__(self, time):
        self.time = time
        self.is_available = True


class AppointmentSystem:
    MAX_APPOINTMENTS = 3

    def __init__(self):
        self.appointments = []

    def view_availability(self, doctor):
        print(f"\nAvailable slots for Dr. {doctor.name}:")
        for slot in doctor.available_slots:
            if slot.is_available:
                print(slot.time)

    def book_appointment(self, patient, doctor, slot):
        upcoming = sum(
            1 for appointment in patient.appointments
            if appointment.status in ["Pending", "Accepted"]
        )

        if upcoming >= self.MAX_APPOINTMENTS:
            print("Booking rejected: Maximum 3 upcoming appointments.")
            return None

        if not slot.is_available or slot not in doctor.available_slots:
            print("Booking rejected: Time slot is unavailable.")
            return None

        appointment = Appointment(
            len(self.appointments) + 1, patient, doctor, slot
        )

        self.appointments.append(appointment)
        patient.appointments.append(appointment)
        slot.is_available = False

        print("Booking request submitted successfully. Status: Pending")
        return appointment

    def respond_to_request(self, doctor, appointment, decision):
        if appointment.doctor != doctor:
            print("This appointment does not belong to this doctor.")
            return

        if appointment.status != "Pending":
            print("This request has already been processed.")
            return

        if decision == "accept":
            appointment.status = "Accepted"
            print("Appointment accepted.")

        elif decision == "decline":
            appointment.status = "Declined"
            appointment.slot.is_available = True
            print("Appointment declined.")

        else:
            print("Invalid decision.")


if __name__ == "__main__":
    system = AppointmentSystem()

    patient = Patient(1, "Ahmed")
    doctor = Doctor(1, "Mohamed", [
        TimeSlot("10:00 AM"),
        TimeSlot("11:00 AM"),
        TimeSlot("12:00 PM"),
        TimeSlot("01:00 PM")
    ])

    system.view_availability(doctor)

    appointment1 = system.book_appointment(
        patient, doctor, doctor.available_slots[0]
    )

    if appointment1:
        system.respond_to_request(doctor, appointment1, "accept")

    system.book_appointment(patient, doctor, doctor.available_slots[1])
    system.book_appointment(patient, doctor, doctor.available_slots[2])
    system.book_appointment(patient, doctor, doctor.available_slots[3])
