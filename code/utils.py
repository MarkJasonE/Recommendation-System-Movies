import numpy as np
import requests
from tmdbv3api import TMDb, Movie

#API settings
tmdb = TMDb()
tmdb.api_key = "b01e862aa12fef25be50f4cb0582263f"
tmdb.language = "en"
tmdb.debug = True
tmdb_movie = Movie()

#Get movie genre from TMDb API
def get_genre(x):
    genres = []
    result = tmdb_movie.search(x)
    if not result:
        return np.NaN
    else:
        movie_id = result[0].id
        response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key={}&language={}".format(movie_id, tmdb.api_key, tmdb.language))
        data_json = response.json()
        if data_json["genres"]:
            ws = " "
            for i in range(0, len(data_json["genres"])):
                genres.append(data_json["genres"][i]["name"])
            return ws.join(genres)           
        else:
            return np.NaN


#Get the director name when encountering various inputs of "director"
def get_director(x):
    if " (director)" in x:
        return x.split(" (director)")[0]
    elif " (directors)" in x:
        return x.split(" (directors)")[0]
    elif " (director," in x:
        return x.split(" (director,")[0]
    elif " (director/" in x:
        return x.split(" (director/")[0]
    elif " (directors/" in x:
        return x.split(" (directors/")[0]
    else: 
        return "None"
        


#Getting the first name after we encounter either "writer", various inputs of "screenplay" and lastly "director"
def get_actor1(x):
    if "writer); " in x:
        return ((x.split("writer); ")[-1]).split(", ")[0])
    elif "Screenplay), " in x:
        return ((x.split("Screenplay), ")[-1]).split(", ")[0])
    elif "screenplay), " in x:
        return ((x.split("screenplay), ")[-1]).split(", ")[0])
    elif "screenplay); " in x:
        return ((x.split("screenplay); ")[-1]).split(", ")[0])
    elif "(screenplay); " in x:
        return ((x.split("(screenplay); ")[-1]).split(", ")[0])
    elif "director); " in x:
        return ((x.split("director); ")[-1]).split(", ")[0])
    else:
        return "None"


#Getting the second name after we encounter either "writer", various inputs of "screenplay" and lastly "director"
def get_actor2(x):
    if "writer); " in x:
        if len(x.split("writer); ")[-1].split(", ")) < 2:
            #If only one name
            return "None"
        else:
            return (x.split("writer); ")[-1].split(", ")[1])
    elif "Screenplay), " in x:
        if len(x.split("Screenplay), ")[-1].split(", ")) < 2:
            return "None"
        else:
            return (x.split("Screenplay), ")[-1].split(", ")[1])
    elif "screenplay) " in x:
        if len(x.split("screenplay) ")[-1].split(", ")) < 2:
            return "None"
        else:
            return (x.split("screenplay) ")[-1].split(", ")[1])
    elif "screenplay); " in x:
        if len(x.split("screenplay); ")[-1].split(", ")) < 2:
            return "None"
        else:
            return (x.split("screenplay); ")[-1].split(", ")[1])
    elif "director); " in x:
        if len(x.split("director); ")[-1].split(", ")) < 2:
            return "None"
        else:
            return (x.split("director); ")[-1].split(", ")[1])
    else:
        return "None"


#Getting the second name after we encounter either "writer", various inputs of "screenplay" and lastly "director"
def get_actor3(x):
    if "writer); " in x:
        if len(x.split("writer); ")[-1].split(", ")) < 3:
            #If only one name
            return "None"
        else:
            return (x.split("writer); ")[-1].split(", ")[2])
    elif "Screenplay), " in x:
        if len(x.split("Screenplay), ")[-1].split(", ")) < 3:
            return "None"
        else:
            return (x.split("Screenplay), ")[-1].split(", ")[2])
    elif "screenplay), " in x:
        if len(x.split("screenplay), ")[-1].split(", ")) < 3:
            return "None"
        else:
            return (x.split("screenplay), ")[-1].split(", ")[2])
    elif "screenplay); " in x:
        if len(x.split("screenplay); ")[-1].split(", ")) < 3:
            return "None"
        else:
            return (x.split("screenplay); ")[-1].split(", ")[2])
    elif "director); " in x:
        if len(x.split("director); ")[-1].split(", ")) < 3:
            return "None"
        else:
            return (x.split("director); ")[-1].split(", ")[2])
    else:
        return "None"