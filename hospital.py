class Patient(object):
    def __init__(self, id, name, allergies, bed_number=None):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number

class Hospital(object):
    def __init__(self, name, patients, capacity):
        self.name = name
        self.patients = []
        self.capacity = capacity

    def add(self, patient):
        patient_dictionary = {
        'ID': patient.id,
        'Name': patient.name,
        'Allergies': patient.allergies,
        'Bed Number': patient.bed_numbers
        }

        self.patients.append(patient_dictionary)
