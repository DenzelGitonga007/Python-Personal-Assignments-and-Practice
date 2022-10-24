# Print the day of the date entered
print("...Get the day corresponding to a certain date...")
print(" ")
from datetime import datetime
# Define the variables/parameters
a = int(input("Which year was it? "))
b = int(input("The month (in numbers)? "))
c = int(input("The day of the month? "))
set_date = datetime(a, b, c)
print("The date {} was on {}".format(set_date.strftime("%Y-%m-%d"), set_date.strftime("%A")))
# print(set_date.strftime("%A"))