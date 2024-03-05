from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from db import engine 

Base = declarative_base()

class CEO(Base):
    __tablename__ = 'CEOS'
    id = Column(Integer, primary_key=True,)
    Name = Column(String)
    Slug = Column(String)
    Year_Served = Column(Integer)

Base.metadata.create_all(engine)

export = CEO