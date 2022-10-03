# To output employee's, departments, and HOD's details
employee = ["Denzel Gitonga", 2002, "Kenya"]
Dep = ["ICT Support"]
HOD = ["Mr. Ayub Shirandula"]
# printing the employee details
print("Name: {} | Year of Birth: {} | Country: {}".format(employee[0], employee[1], employee[2])) #using the format method
print("In the deparment: %s"%(Dep[0])) # Using the %s

# Replacing an entry on the list
cars = ["Vitz", "Mazda", "Mercedes", "Pegeout", "Dodge"] # Original list
print("This is the original list: {}".format(cars))
cars[2] = "Demio" #Replace
print("The list after adding an entity: %s"%(cars[:]))
# Deleting an element in the list
del cars[3] #Using the del keyword
print("After deleting an element: {}".format(cars[:]))
cars.remove("Vitz") # Using the remove method
print("Deleting using the remove method: %s"%(cars[:]))
popping = cars.pop(-1)
print("Popping the last element from the list: '{}', new list is:{}".format(popping,cars))
# Replicating a list
numbers = [1, 2, 3, 4, 5]
print(numbers*2)
# Concatinating lists
letters = ["a", "b", "c", "d", "e"]
print(numbers + letters)