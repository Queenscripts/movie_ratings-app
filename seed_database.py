import os
from random import choice, randint
from datetime import datetime


import crud
import model 
import server
import json

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open("data/movies.json") as f:
    movie_data = json.loads(f.read())

movies_in_db=[]

for movie in movie_data: 
    title, overview, poster_path=(
        movie["title"],
        movie["overview"],
        movie["poster_path"])
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")
    
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)


for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'
    user = crud.create_user(email, password)

    for i in range(10):
        crud.create_rating (user, choice(movies_in_db), randint(1, 10))