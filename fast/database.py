from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


connection = psycopg2.connect(user="postgres", password="123")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
SQLALCHEMY_URL = "postgresql://postgres:123@localhost/Sweets"
engine = create_engine(SQLALCHEMY_URL)
session = Session(engine)
def session_scope():
    """Provide a transactional scope around a series of operations."""
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
def clear_tables():
    with session_scope() as conn:
        for table in Base.metadata.sorted_tables:
            conn.execute(
                f"TRUNCATE {table.name} RESTART IDENTITY CASCADE;"
            )
        conn.commit()
Base = declarative_base()

class Sweets(Base):
    __tablename__ = "Suger"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

# Base.metadata.create_all(bind=engine)
cookies = Sweets(
    name = "Печенье",
    description = "Вкусное",
)
session.add(cookies)
session.commit()
print(session.new)

Session = sessionmaker(bind=engine)
db = Session()