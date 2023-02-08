# Nurse details
class Nurse:

   def _init_(self, nurse):
      self.name = nurse['name']
      self.department = nurse['department']

   def get_nurse_details(self):
    #   return f"Name: {self.name}\nDepartment: {self.department}"
    return "Name: {}\nDepartment: {}".format(self.name, self.department)