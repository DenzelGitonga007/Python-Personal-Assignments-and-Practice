# Import the doctor and nurse classes from the files
from doctor import Doctor
from nurse import Nurse

# creating dictionary for doctor and nurse
doctor_dict = {'name' : 'George', 'gender': 'Male', 'specialiality': 'gynocologist'}
nurse_dict = {'name': 'Polline', 'department': 'Labor'}

# creating instances of the doctor and nurse
doctor = Doctor(doctor_dict)
nurse = Nurse(nurse_dict)

# getting and printing the doctor and nurse details
print(doctor.get_doctor_details())
print()
print(nurse.get_nurse_details())