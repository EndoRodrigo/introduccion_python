from fastapi import FastAPI, Body, Path, Query
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()
app.title = "Mi aplicacion con FastApi"
app.version = "0.0.1"

class Movie(BaseModel):
    id:Optional[int] = None
    title:str = Field(min_length=5,max_length=15)
    overview:str = Field(min_length=5,max_length=15)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5,max_length=15)

    class Config:
        schema_extra = {
            "example":{
                "id": 1,
                "title": "Mi peliculña",
                "overview": "Descripcion de la pelicula",
                "year": 2023,
                "rating": 9.8,
                "category": "Accion"
            }
        }

movies = [{
    'id': 1,
    'title': 'Avatar',
    'overview': 'En un exceburente planeta llamado pandora',
    'year': '2009',
    'rating': 7.8,
    'category': 'Otro'
},
{
    'id': 2,
    'title': 'Robocot',
    'overview': 'La nueva maquina de a policia',
    'year': '2000',
    'rating': 9.8,
    'category': 'Acccion'
}
]

@app.get('/', tags=['Home'])
def msg():
    return HTTPResponse('<h1>Hello World</h2>')

@app.get('/peliculas',tags=['Movies'])
def get_movies():
    return movies

@app.get('/peliculas/{id}',tags=['Movies'])
def get_movie(id: int = Path(ge=1,le=2000)):
    for movi in movies:
        if movi['id'] == id:
            return movi
        
    return []

@app.get('/movies/',tags=['Movies'])
def get_movies_category(category: str = Query(min_length=3,max_length=15)):
    return [item for item in movies if item['category'] == category]

@app.post('/movies/', tags=['Movies'])
def create_movie(pelicula: Movie):
    movies.append(pelicula)
    return movies[-1]

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id:int, pelicula: Movie):
    for movi in movies:
        if movi['id'] == id:
            movi['title'] = pelicula.title
            movi['overview'] = pelicula.overview
            movi['year']= pelicula.year
            movi['rating']= pelicula.rating
            movi['category']= pelicula.category
            return movies

@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    for movi in movies:
        if movi['id'] == id:
            movies.remove(movi)
            return movies
    return []
    