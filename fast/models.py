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
#     category="Взбитые",
# )
# session.add(cookies)
# cookies3 = Sweets(
#     name="Безе",
#     description="Хрустящее удовольствие, белой нежности, со сладкой начинкой, вытекающей из оболочки, смешивающийся в приятное послевкусие.Тает во рту",
#     category_id=7,
#     img="https://avatars.dzeninfra.ru/get-zen_doc/108343/pub_62b45547390b0f3680acf7d4_62b48dd8db821f6462882865/scale_1200"
# )
# session.add(cookies3)
# session.commit()
