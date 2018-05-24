import random
class Patient(object):
    def __init__(self, id_number = None, name = None, allergies = None, bed_number = None):
        self.id_number = id_number
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number
    
class Hospital(object):
    def __init__(self, patients = [], name = None, capacity = 0):
        self.patients = patients
        self.name = name
        self.capacity = capacity

    def admit(self, patient):
        if len(self.patients) >= capacity:
            print ("{} is currently at full capacity. We cannot admit {} at this time.".format(self.name, patient.name))
            return self
        else:
            self.patients.append(patient)
            patient.bed_number = random.randInt(1,self.capacity)
            print ("Admission successful!")
            return self

    def discharge(self, patient):
        self.patients.remove(patient)
        patient.bed_number = None
        return self
