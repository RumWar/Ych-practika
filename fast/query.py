from sqlalchemy.orm import Session
import models


def get_all(db: Session):
    return db.query(models.Sweets).all()

def get_category(db: Session, category: int):
    return db.query(models.Sweets).filter(models.Sweets.category_id == category).first()

def get_description(db: Session, description: str):
    return db.query(models.Sweets).filter(models.Sweets.description == description).first()