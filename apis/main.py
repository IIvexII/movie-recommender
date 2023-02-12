from fastapi import FastAPI
import pickle

app = FastAPI()

# loading the data
movies = pickle.load(open("data/movies.pkl", "rb"))
similarity = pickle.load(open("data/similarities.pkl", "rb"))


@app.get("/{movie_name}")
async def recommend_movies(movie_name):
    movie = movies[movies["title"] == movie_name]
    if (len(movie) > 0):
        movie_index = movie.index[0]
        distance = similarity[movie_index]

        movie_list = sorted(list(enumerate(distance)),
                            reverse=True, key=lambda tupple: tupple[1])[1:6]

        return {"movies": [movies.iloc[movie[0]].title for movie in movie_list]}
    else:
        return {"err_code": 404, "movies": []}
