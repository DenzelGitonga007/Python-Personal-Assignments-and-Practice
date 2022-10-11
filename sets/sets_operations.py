# Set operations like Union, Intersection, and set differences
# set Union
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# confirming that a and b are actual sets
print("a and b are both {}".format(type(a)))
print("Set a = {} and set b = {}".format(a, b))
print("Set union: " + str(a | b))

# Still union
print(a.union(b))
print(b.union(a))

# Intersection
num_1 = {1, 2, 3, 4, 5,}
num_2 = {4, 5, 6, 7, 8}
print("The set num_1 = {}, and set num_2 = {}".format(num_1, num_2) )
# Only the common elements
print("The set intersection/common elements: " + str(num_1 & num_2))
# print(num_1.intersection(num_2))

# Set differences
value_1 = {10, 20, 30, 40, 50}
value_2 = {30, 40, 60, 80, 90}
print("The set value_1 = {}, and set value_2 is {}".format(value_1, value_2))
print("Set difference value_1 - value_2 = " + str(value_1 - value_2))
print("And value_2 - value_1" + str(value_2 - value_1))
print("Using the difference() method, also works: " + str(value_1.difference(value_2)))