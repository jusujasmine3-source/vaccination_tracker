# Vaccination Tracker

**Course:** PROG211 Object-Oriented Programming 1
**Assignment:** Real-World Solutions under DPG Standards
**Domain:** Health (Vaccination Tracker)

## About the Project

This is a simple Python program that tracks vaccinations at a community clinic. It records which vaccines a patient has received, counts the doses, and shows whether a patient has finished a full vaccine course. It is written with Object-Oriented Programming (OOP) and follows Digital Public Goods (DPG) principles.

## Problem It Solves

Paper vaccination records are easy to lose and hard to check. Clinics can forget which patients still need a second or third dose. This program keeps a clear record of every dose given and shows who has completed each vaccine.

## Files

| File | Purpose |
|------|---------|
| `vaccination_tracker_simple.py` | The full Python source code |
| `README.md` | Documentation (this file) |
| `LICENSE` | MIT open-source licence |

## How to Run

1. Install Python 3 (no other libraries are needed).
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```
python vaccination_tracker_simple.py
```

## How the Code Is Organised

### Classes
- **`vaccine`**: stores the vaccine name, the number of doses required, and the days between doses.
- **`patient`**: stores an anonymous patient ID, birth year, and the doses the patient has taken.

### Data Structure
- A single **dictionary** (`patients`) stores many `patient` objects, using the patient ID as the key.
- `add_patient()` adds a record and refuses duplicate IDs.
- `display_patients()` loops through the dictionary and prints every record.

### Tuples
- Each dose is stored as a tuple: `(vaccine_name, dose_number, dose_date)`.
- A patient's `doses_taken` is a tuple of these dose tuples.
- Tuple unpacking is used when displaying records.

### Methods
| Type | Methods |
|------|---------|
| Instance methods | `add_dose()`, `count_doses()`, `is_fully_vaccinated()`, `get_age()`, `get_patient_info()`, `get_vaccine_info()` |
| Class methods (`@classmethod`) | `vaccine.from_text()`, `patient.from_text()`, `patient.get_total_patients()` |
| Static method (`@staticmethod`) | `patient.is_valid_id()` |

## How the Project Meets DPG Standards

**1. Open-source**
The code is uploaded to GitHub under the MIT licence, so anyone can read, use, change and share it for free. It uses only standard Python with no paid tools.

**2. Inclusive and accessible design**
The program uses plain text output and simple, clear words. It needs no internet connection, no special hardware and no account, so it works on low-cost computers in places with poor connectivity.

**3. Privacy-respecting (no sensitive personal data)**
The program stores only an anonymous patient ID (such as `P001`) and a birth year. It never stores names, phone numbers, addresses or email addresses. The static method `is_valid_id()` rejects IDs that look like an email address or a phone number, so personal data cannot be entered by mistake.

**4. Modular and reusable**
The `vaccine` and `patient` classes are separate and independent, so they can be imported and used in other health projects. The demonstration code is inside a `main()` function, so importing the file does not run it automatically.

## Example Usage

Sample input (created in `main()`):

```python
measles = vaccine("Measles", 2, 180)
polio = vaccine.from_text("Polio, 3, 30")

patient1 = patient("P001", 2024)
patient2 = patient("P002", 1985)
patient3 = patient.from_text("P003, 1950")

add_patient(patient1)
patient1.add_dose(measles, "2026-01-10")
patient2.add_dose(measles, "2025-12-01")
patient2.add_dose(measles, "2026-06-01")
```

Sample output:

```
Measles: 2 dose(s), 180 days apart
Polio: 3 dose(s), 30 days apart
P001 added
P002 added
P003 added
P001 already exists
Dose 1 of Measles given to P001
Dose 1 of Polio given to P001
Dose 1 of Measles given to P002
Dose 2 of Measles given to P002
P002 already finished Measles
Dose 1 of Polio given to P003
----- All Patients -----

        Patient ID: P001
        Age: 2
        Doses taken: 2

   Measles dose 1 on 2026-01-10
   Polio dose 1 on 2026-08-01

        Patient ID: P002
        Age: 41
        Doses taken: 2

   Measles dose 1 on 2025-12-01
   Measles dose 2 on 2026-06-01

        Patient ID: P003
        Age: 76
        Doses taken: 1

   Polio dose 1 on 2026-09-01
Patient 2 fully vaccinated for measles: True
Patient 1 fully vaccinated for measles: False
Total patients: 3
```

## Author

Jasmine Sia Deborah Jusu

## Licence

This project is released under the MIT Licence. See the `LICENSE` file.
