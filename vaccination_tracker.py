class vaccine:
    def __init__(self, vaccine_name, doses_required, days_between):
        self.vaccine_name = vaccine_name
        self.doses_required = doses_required
        self.days_between = days_between

    def get_vaccine_info(self):
        return f"{self.vaccine_name}: {self.doses_required} dose(s), {self.days_between} days apart"

    @classmethod
    def from_text(cls, text):
        vaccine_name, doses_required, days_between = text.split(",")
        return cls(vaccine_name.strip(), int(doses_required), int(days_between))


class patient:
    total_patients = 0

    def __init__(self, patient_id, birth_year):
        if not patient.is_valid_id(patient_id):
            raise ValueError("Use an anonymous ID like P001, not personal data")
        self.patient_id = patient_id
        self.birth_year = birth_year
        self.doses_taken = ()
        patient.total_patients += 1

    def get_age(self):
        current_year = 2026
        return current_year - self.birth_year

    def count_doses(self, vaccine_name):
        count = 0
        for dose in self.doses_taken:
            if dose[0] == vaccine_name:
                count += 1
        return count

    def add_dose(self, vaccine_object, dose_date):
        doses_so_far = self.count_doses(vaccine_object.vaccine_name)
        if doses_so_far >= vaccine_object.doses_required:
            print(f"{self.patient_id} already finished {vaccine_object.vaccine_name}")
            return
        dose = (vaccine_object.vaccine_name, doses_so_far + 1, dose_date)
        self.doses_taken = self.doses_taken + (dose,)
        print(f"Dose {dose[1]} of {dose[0]} given to {self.patient_id}")

    def is_fully_vaccinated(self, vaccine_object):
        return self.count_doses(vaccine_object.vaccine_name) >= vaccine_object.doses_required

    def get_patient_info(self):
        return f"""
        Patient ID: {self.patient_id}
        Age: {self.get_age()}
        Doses taken: {len(self.doses_taken)}
"""

    @classmethod
    def from_text(cls, text):
        patient_id, birth_year = text.split(",")
        return cls(patient_id.strip(), int(birth_year))

    @classmethod
    def get_total_patients(cls):
        return cls.total_patients

    @staticmethod
    def is_valid_id(patient_id):
        if "@" in patient_id or patient_id.isdigit():
            return False
        return True


patients = {}


def add_patient(patient_object):
    if patient_object.patient_id in patients:
        print(f"{patient_object.patient_id} already exists")
    else:
        patients[patient_object.patient_id] = patient_object
        print(f"{patient_object.patient_id} added")


def display_patients():
    print("----- All Patients -----")
    for patient_id in patients:
        p = patients[patient_id]
        print(p.get_patient_info())
        for dose in p.doses_taken:
            vaccine_name, dose_number, dose_date = dose
            print(f"   {vaccine_name} dose {dose_number} on {dose_date}")


def main():
    measles = vaccine("Measles", 2, 180)
    polio = vaccine.from_text("Polio, 3, 30")
    print(measles.get_vaccine_info())
    print(polio.get_vaccine_info())

    patient1 = patient("P001", 2024)
    patient2 = patient("P002", 1985)
    patient3 = patient.from_text("P003, 1950")

    add_patient(patient1)
    add_patient(patient2)
    add_patient(patient3)
    add_patient(patient1)

    patient1.add_dose(measles, "2026-01-10")
    patient1.add_dose(polio, "2026-08-01")
    patient2.add_dose(measles, "2025-12-01")
    patient2.add_dose(measles, "2026-06-01")
    patient2.add_dose(measles, "2026-07-01")
    patient3.add_dose(polio, "2026-09-01")

    display_patients()

    print("Patient 2 fully vaccinated for measles:", patient2.is_fully_vaccinated(measles))
    print("Patient 1 fully vaccinated for measles:", patient1.is_fully_vaccinated(measles))
    print("Total patients:", patient.get_total_patients())


if __name__ == "__main__":
    main()
