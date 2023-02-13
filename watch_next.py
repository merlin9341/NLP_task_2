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

watched_title =  "Planet Hulk"

watched_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, "\
    "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. "\
    "Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

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
top3 = movie_finder(watched_description)

print(f"The 3 movies that are most similar to {watched_title} are:")
print("\n".join(top3))
