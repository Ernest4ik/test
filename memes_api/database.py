from sqlalchemy import create_engine
from sqlalchemy.orm import Session


SQLALCHEMY_DATABASE_URL = "postgresql://user:root@posthost:5432/database"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

