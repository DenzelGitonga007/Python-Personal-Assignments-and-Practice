# Using the zipped file to compact elements in a tuple
first_name = ("Denzel", "Catherine", "Ndanu")
last_name = ("Gitonga", "Marigu", "Wa Naivasha")
name = zip(first_name, last_name)
print(name) #initiates the zipped tuple
people = tuple(name)
print(people)
