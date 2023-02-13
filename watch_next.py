#Task 38 - Semantic Similarity (NLP) - Task 2

#nlp is set up using spacy
import spacy
nlp = spacy.load("en_core_web_md")

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
    similarity_list = [[movie[0], nlp(movie[1]).similarity(description_token)] for movie in movies]