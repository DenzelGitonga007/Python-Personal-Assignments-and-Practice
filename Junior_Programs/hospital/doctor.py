# Doctor details
class Doctor:

   def _init_(self, doctor):
      self.name = doctor['name']
      self.gender = doctor['gender']
      self.specialiality = doctor['specialiality']

   def get_doctor_details(self):
    #   return f"Name: {self.name}\nGender: {self.gender}\nSpeciality: {self.specialiality}"
      return "Name: {}\nGender: {}\nSpeciality: {}".format(self.name, self.gender, self.specialiality)