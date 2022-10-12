# Using the zipped file to compact elements in a tuple
first_name = ("Denzel", "Catherine", "Ndanu")
last_name = ("Gitonga", "Marigu", "Wa Naivasha")
name = zip(first_name, last_name)
print(name) #initiates the zipped tuple
people = tuple(name)
print(people)
# Returning more than one value using tuples
def mean(x, y, z):
    sum = x + y + z
    avg = sum/3
    return (sum, avg)
(s, a) = mean(27, 30, 35)
print("The sum is: " + str(s))
print("The average is: " + str(a))