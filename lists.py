# To output employee's, departments, and HOD's details
employee = ["Denzel Gitonga", 2002, "Kenya"]
Dep = ["ICT Support"]
HOD = ["Mr. Ayub Shirandula"]
# printing the employee details
print("Name: {} | Year of Birth: {} | Country: {}".format(employee[0], employee[1], employee[2])) #using the format method
print("In the deparment: %s"%(Dep[0])) # Using the %s

# Replacing an entry on the list
cars = ["Vitz", "Mazda", "Mercedes"] # Original list
print("This is the original list: {}".format(cars))
cars[2] = "Demio" #Replace
print("The list after adding an entity: %s"%(cars[:]))
