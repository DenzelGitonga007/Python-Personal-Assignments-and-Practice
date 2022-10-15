# Creating a list of favorite movies, 
# and assigning them to different genres
# and display the output as key-value pair
movies = []
# set the limit of users' movies list
limit = int(input("How many movies do you have in mind? "))
# Iterating over the movies list provided, based on the limit
for elements in range(0, limit):
    elements = str(input()) #The movies entered
    # Append the elements onto the movies
    movies.append(elements)

