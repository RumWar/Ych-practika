from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base, engine, session


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)

    two = relationship("Sweets", back_populates="one")


class Sweets(Base):
    __tablename__ = "Suger"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))
    img = Column(String)

    one = relationship("Category", back_populates="two")


class Response(Base):
    __tablename__ = "response"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String, index=True)


Base.metadata.create_all(bind=engine)

# cookies = Category(
#     category="cookies",
# )
#
# cookies3 = Sweets(
#     name="Шоколадное печенье",
#     description="Рассыпчатое, политое шоколадом",
#     category_id=1,
#     img="http://klublady.ru/uploads/posts/2022-02/1644704359_64-klublady-ru-p-pechenki-s-shokoladom-foto-70.jpg"
# )
# session.add(cookies)
# session.add(cookies3)
# session.commit()
