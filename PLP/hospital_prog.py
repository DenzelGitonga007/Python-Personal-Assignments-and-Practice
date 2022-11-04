# Write a program for a hospital 

# Check in a patient named John Smith
# He is 20 years old
# He is a new Patient
# Declare variables to store this values
print("...A hospital program for checking patient records...")
print(" ")
# Fetching the name and the age of the patient
# checking that only strings and integers are taken
while True:
    try:
        name = str(input("Please enter the name of the patient: "))
    except:
        print("Please enter a text value only: ")
    break
while True:
    try:
        age = int(input("Hold old is the patient? (In numbers): "))
    except:
        print("Please enter a numerical value only: ")
    break
#Print out the name and age entered
print("The patient {}, age {}, is a new patient.".format(name, age))