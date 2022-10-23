# Display double right angled triangle
def double_triangle(size): # n is the size of the triangle
    # The y-axis
    for y_axis in range(1, size+1):
        double_y = y_axis + 1 if (y_axis % 2 != 0) else y_axis
        # The x-axis
        for x_axis in range(double_y, size):
            #set the limit
            if x_axis >= double_y:
                print(end="  ")
        #The start of second twin triangle
        for twin_x in range(0, double_y):
            if twin_x == double_y - 1:
                print(" * ")
            else:
                print(" * ", end= " ")
# Getting the input
size = int(input("How long do you want the triangle to be in cm? "))
#call the function if size value is greater than 10
if size < 10:
    print("The instructions are, size must be greater than 10")
else:
    double_triangle(size)