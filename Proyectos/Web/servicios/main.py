from fastapi import FastAPI

app = FastAPI()
app.title = "Mi aplicacion con FastApi"
app.version = "0.0.1"

@app.get('/', tags=['Home'])
def msg():
    return "Hello world"