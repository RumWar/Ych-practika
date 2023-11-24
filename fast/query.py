from sqlalchemy.orm import Session
import models, post


def get_all(db: Session):
    return db.query(models.Sweets).all()


def get_category(db: Session):
    return db.query(models.Category).all()


def get_description(db: Session, description: str):
    return db.query(models.Sweets).filter(models.Sweets.description == description).first()


def create_user(db: Session, comment: post.Response1):
    db_user = models.Response(comment=comment)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
