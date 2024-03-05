from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db import session
from models import CEO, CEOSchema

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3000/ceos",
    "http://localhost:5173",
    "http://localhost:5174"
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message: root route."}

@app.get("/ceos")
def get_ceos():
    ceos = session.query(CEO)
    return ceos.all()

@app.post("/ceos")
def create_ceo(id: int, Name: str, Slug: str, Year_Served: int):
    new_ceo = CEO(
        id=id,
        Name=Name,
        Slug=Slug,
        Year_Served=Year_Served
    )
    session.add(new_ceo)
    session.commit()
    return new_ceo