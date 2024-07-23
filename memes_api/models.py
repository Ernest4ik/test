from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Mem(Base):
    __tablename__ = 'memes'
    id = Column(Integer, primary_key=True)
    description = Column(String)
