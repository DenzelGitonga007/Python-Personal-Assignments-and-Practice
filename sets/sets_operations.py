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