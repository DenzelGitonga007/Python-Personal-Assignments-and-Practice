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