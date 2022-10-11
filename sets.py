# Difference between a set and a dictionary is, a dictionary has a key and an associate value
numbers = {1, 2, 3}
alpha_numeric = {1:20, 20:2} #The key and the associate value
print(type(numbers))
print(type(alpha_numeric))

# Initializing a set
values = {1, 2}
print("The initial list is " + str(values))
# Adding elements into the set
values.add(3)
print("Adding elements into the set " + str(values))
# Update more elements therein
values.update([4,5])
print("Updated version " + str(values))
# Removing elements from the set
values.discard(4)
print("Discarded an element " + str(values))
values.remove(5)
print("Removed an element " + str(values))
