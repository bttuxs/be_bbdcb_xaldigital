import importlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

USER = config("BBDD_USER")
PASS = config("BBDD_PASS")
HOST = config("BBDD_HOST")
BBDD = config("BBDD_BBDD")
PORT = config("BBDD_PORT")
DATABASE_URL = "postgresql://"+USER+":"+PASS+"@"+HOST+":"+PORT+"/"+BBDD

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
