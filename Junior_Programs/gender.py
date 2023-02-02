#Print the gender
gender = str((input("Enter your gender: ").lower()))
if gender != "male" and gender != "female":
    print("{} is not recognised".format(gender))
else:
    print("You're a {}".format(gender))
