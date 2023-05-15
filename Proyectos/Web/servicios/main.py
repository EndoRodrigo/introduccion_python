from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
from config.database import Session, engine, Base
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder


app = FastAPI()
app.title = "Mi aplicacion con FastApi"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)

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
                "title": "Mi peliculia",
                "overview": "Descripcion",
                "year": 2013,
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
    db = Session()
    result = db.query(MovieModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@app.get('/peliculas/{id}',tags=['Movies'])
def get_movie(id: int = Path(ge=1,le=2000)):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"Mensaje":"No se encontaron resultados"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.get('/movies/',tags=['Movies'])
def get_movies_category(category: str = Query(min_length=3,max_length=15)):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category == category).first()
    if not result:
        return JSONResponse(status_code=404, content={"Mensaje":"No se encontaron resultados"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.post('/movies/', tags=['Movies'])
def create_movie(pelicula: Movie):
    db = Session()
    new_movie = MovieModel(**pelicula.dict())
    db.add(new_movie)
    db.commit()
    movies.append(pelicula)
    return JSONResponse(status_code=201, content={"Mensaje: ": "Se ha registrado los datos con exito"})

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id:int, pelicula: Movie):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"Mensaje":"No se encontaron resultados"})
    result.title = pelicula.title
    result.overview = pelicula.overview
    result.year = pelicula.year
    result.rating = pelicula.rating
    result.category = pelicula.category
    db.commit()
    return JSONResponse(status_code=200, content={"Mensaje":"Informacion actualizada"})


@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"Mensaje":"No se encontaron resultados"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"Mensaje":"Informacion eliminada"})
    