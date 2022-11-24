# #Python coding challenge **12
# # A "Perfect Number" is a number in which the sum of its factors (excluding itself) are equal to itself.
# Write a function that can verify if the given integer n is a perfect number, 
# and return True if it is, or return False if not.
# Example
# n = 28 has the following factors: 1, 2, 4, 7, 14
# 1 + 2 + 4 + 7 + 14 = 28 therefore n = 28 is a perfect number, so you should return True.
# n = 25 has the following factors: 1, 5, 25
# 1 + 5 = 6 therefore n = 25 is not a perfect number, so you should return False.

print("...Finding a perfect number...")
# Get the number from the user
test_num = int(input("Enter any number: "))
print("The factors of {} are: ".format(test_num))
for values in range(1, test_num):
    # Obtain only factors-- numbers that can divide 28 without a remainder 
    factors = 0
    if test_num % values == 0:
        factors = values
        print(factors)
# Adding the factors to check that if they form a perfect number
sum_of_factors = sum(
    accurate_factors for accurate_factors in range(1, test_num) 
    if test_num % accurate_factors == 0
    )
# print(sum_of_factors)
# printing whether the test_num is a perfect number or not
if sum_of_factors == test_num:
    print("The sum of the factors is '{}', hence, '{}' is a perfect number".format(sum_of_factors, test_num))
else:
    print("The sum of the factors is '{}', hence, '{}' is not a perfect number".format(sum_of_factors, test_num))