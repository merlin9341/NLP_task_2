#Task 38 - Semantic Similarity (NLP) - Task 2

#A list is created to hold the movies
movies = []

#the file is read as a list of descritons and titles
with open("movies.txt", "r") as movies_file:
    for line in movies_file:
        movies.append(line.strip("\n").split(" :"))

print(movies)