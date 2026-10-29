# AI Usage Journal

## Project: Doctor Appointment Booking System

**Team Members:**
- Mostafa Bahgat Salah — 20240591
- Tarek Osama Farouk — 20240284

**Maximum Appointments:** N = 3

## 1. AI Usage and Our Checks

| Phase | AI Help | What We Checked |
|---|---|---|
| P1 | Classified requirements R1–R7. | Checked that R1–R4 are functional and R5–R7 are non-functional. |
| P2 | Created three use cases. | Checked the actors, main flows, and alternative flows. |
| P3 | Created the Use Case Diagram. | Checked the Patient and Doctor interactions. |
| P4 | Suggested candidate classes. | Checked the classes against the requirements and selected five. |
| P5 | Created the Class Diagram. | Checked the attributes, methods, and relationships. |
| P6 | Created the Sequence Diagram. | Checked the booking process and the N = 3 limit. |
| P7 | Helped write the Python code. | Ran the program and checked booking, acceptance, and appointment limits. |

## 2. AI Mistakes and Corrections

### Issue 1: Diagram Preview

**What happened:** The Mermaid diagram did not load in the GitHub editor preview.

**How we noticed:** The preview kept loading without displaying the diagram.

**What we checked:** We opened the saved Markdown file and confirmed that the diagram was displayed correctly.

**Result:** The diagram was successfully rendered in the saved file.

### Issue 2: Candidate Classes

**What AI suggested:** AI suggested additional candidate classes, including MedicalRecord, Notification, and MobileInterface.

**Why we did not use them:** They were not needed as separate classes for the required implementation.

**How we checked:** We compared the candidates with the requirements and use cases.

**Correction:** We selected five main classes for the system.

## 3. Final Testing

We ran the Python program in PyCharm.

We checked that appointments could be booked and accepted, and that a patient could not exceed three upcoming appointments.

## 4. Output of main.py

```text
Available slots for Dr. Mohamed:
10:00 AM
11:00 AM
12:00 PM
01:00 PM
Booking request submitted successfully. Status: Pending
Appointment accepted.
Booking request submitted successfully. Status: Pending
Booking request submitted successfully. Status: Pending
Booking rejected: Maximum 3 upcoming appointments.

Process finished with exit code 0
```
