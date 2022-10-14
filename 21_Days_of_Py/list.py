# Create a list of favorite movies and 
# display the first and last movies

# Initialize the movies list
movies = []
# To set a limit for the movies(otherwise, the list will be endless
# and never display anything afterall)
list = int(input("How many movies do you have in mind? "))
# Iterating over the movies
for element in range(0, list):
    element = str(input())

    # Now append the elements to the movies
    movies.append(element)
print("I totally enjoy watching {} and {}.".format(movies[0], movies[-1]))
