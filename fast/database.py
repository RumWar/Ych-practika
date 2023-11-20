from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, relationship, declarative_base
from pydantic import BaseModel
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = psycopg2.connect(user="postgres", password="123")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
SQLALCHEMY_URL = "postgresql://postgres:123@localhost/Sweets"
engine = create_engine(SQLALCHEMY_URL)
session = Session(engine)
Session = sessionmaker(engine)
Base = declarative_base()


