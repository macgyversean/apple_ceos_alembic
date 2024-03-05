from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from db import engine 

Base = declarative_base()

class CEOSchema(BaseModel):
    id: int
    Name: str
    Slug: str
    Year_Served: int

class Config:
    populate_by_name = True

export = CEOSchema