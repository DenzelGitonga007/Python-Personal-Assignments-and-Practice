# Take a number, and print the sum of all numbers from 1 to that number
print("...Get the sum of all numbers from 1 to your desired number...")
# Initialize the variable
num = int(input("Enter any number: "))
result = 0
for numbers in range(1, num+1, 1):
    result += numbers
print("The sum of the numbers from 1 to {} is {}".format(num, result))
