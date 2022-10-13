# Comprehension + enumerate()
# Initialising a students pass list
pass_list = ["Denzel", "Jayden", "Catherine", "Junne", "Francis"]
print(pass_list)
# Using the dictionary Comprehension and enumerate()
result = {position : name + 1 for name, position in enumerate(pass_list)}
print(result)