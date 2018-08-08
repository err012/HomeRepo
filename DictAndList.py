import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Parse in movieListing and check imdb scores (In DICTIONARY way)
def movieScoringDict(movie):
        #imdbScore = ""
        for i in movies:
            if i["name"] == movie and i["imdb"] > 5.5:
                imdbScore = True
            elif i["name"] == movie and i["imdb"] < 5.5:
                imdbScore = "Failed"
        #print imdbScore
        return imdbScore

#Parse in movieListing and check imdb scores (In LIST way)
def movieScoringList(movie_name):
    return ['True' for movie in movies if movie["name"] == movie_name and movie["imdb"] > 5.5]

#Parse movieListing and store in empty list where imdb < 5.5 (In DICTIONARY way)
def moviesListInDict(movies):
    movies_above = []
    for m in movies:
        if m["imdb"] < 5.5:
            movies_above.append(m["name"])
    return movies_above

#Parse movieListing and store in empty list where imdb < 5.5 (In LIST way)
def moviesListInList(movies):
    movies_greater = [movie["name"] for movie in movies if movie["imdb"] < 5.5]
    return movies_greater

#Parse and load movies list in PANDAS
def loadAndReadWithPandas(fileIn):
    #ConvertedFile = pd.DataFrame(fileIn)
    Aver = fileIn.boxplot(column = "name", by = "imdb")
    return Aver


myDictScore = movieScoringDict("We Two")
print myDictScore

myListScore = movieScoringList("Detective")
print myListScore

myDictMovieList = moviesListInDict(movies)
print myDictMovieList

myListMovieList = moviesListInList(movies)
print myListMovieList

myLoadedPandasFile = loadAndReadWithPandas(movies)
print myLoadedPandasFile
