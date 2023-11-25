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
#     category="Мармелад",
# )
# session.add(cookies)
cookies3 = Sweets(
    name="Рахат-лукум с орехами",
    description="Восточная сладость в сахорной пудре с кусочками арахиса",
    category_id=5,
    img="https://o-tendencii.com/uploads/posts/2022-02/1645682122_40-o-tendencii-com-p-turetskie-sladosti-rakhat-lukum-foto-43.jpg"
)

session.add(cookies3)
session.commit()
