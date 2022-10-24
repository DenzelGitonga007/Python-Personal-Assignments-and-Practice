# Print the day of the date entered
print("...Get the day corresponding to a certain date...")
print(" ")
from datetime import datetime
# Define the variables/parameters
#Capture only the integers
while True:
    # For the year
    try:
        a = int(input("Which year was it? "))
        b = int(input("The month (in numbers)? "))
        c = int(input("The day of the month? "))
        break
    except:
        print("Please enter valid dates:")
# The variable holding the date
set_date = datetime(a, b, c)
print("The date {} was on {}".format(set_date.strftime("%Y-%m-%d"), set_date.strftime("%A")))
