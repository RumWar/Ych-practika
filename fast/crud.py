from sqlalchemy.orm import Session
from . import schemas, models


def get_all(db: Session):
    return db.query(models.Sweets).all()


def get_name(db: Session, name: str):
    return db.query(models.Sweets).filter(models.Sweets.name == name).first()

def get_description(db: Session, description: str):
    return db.query(models.Sweets).filter(models.Sweets.description == description).first()


