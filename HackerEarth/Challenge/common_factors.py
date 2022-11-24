# Get the input numbers
first_num = int(input())
second_num = int(input())
# The lists for factors
first_factors = []
second_factors = []
# combined list for common factors
combined_factors = []
# Check for factors of first_num
for values in range(1, first_num):
    if first_num % values == 0:
        # print(values)
        # Append them onto a list
        first_factors.append(values)
# print(first_factors)
for values_2 in range(1, second_num):
    if second_num % values_2 == 0:
        # Append them onto a list
        second_factors.append(values_2)
# Combine the factors
combined_factors = first_factors + second_factors
print(combined_factors)
# Appending the common factors
common_factors = []
uncommon_factor = []
for factors in combined_factors:
    if factors not in uncommon_factor:
        uncommon_factor.append(factors)
    else:
        common_factors.append(factors)
print(len(common_factors))