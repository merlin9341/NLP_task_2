#Task 38 - Semantic Similarity (NLP) - Task 2

#nlp is set up using spacy
import spacy
nlp = spacy.load("en_core_web_md")

class Movie:
    def __init__(self, name, similarity):
        self.name = name
        self.similarity = similarity

    def get_name(self):
        return self.name

    def __lt__(self, other):
        return self.similarity < other.similarity

#A list is created to hold the movies
movies = []

def file_read():
    #the file is read as a list of descritons and titles
    with open("movies.txt", "r") as movies_file:
        for line in movies_file:
            movies.append(line.strip("\n").split(" :"))

def movie_finder(description):
    "returns the movies from the movies list that are most semantically similar to the description provided"
    #creats a token from the descrition provided
    description_token = nlp(description)

    #Uses list comprehension to create list of the movies in the movies list and their similarity to the descrition given
    similarity_list = [Movie(movie[0], nlp(movie[1]).similarity(description_token)) for movie in movies]

    #the list is now sorted
    similarity_list.sort(reverse= True)

    #the top (last) three from the list are now returned
    top3 = similarity_list[:3]
    return list(map(Movie.get_name, top3))

file_read()

print(movie_finder("dragon"))