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

    one = relationship("Category", back_populates="two")


Base.metadata.create_all(bind=engine)

# cookies = Category(
#     category="cookies",
# )
#
# cookies3 = Sweets(
#     name="vanilla waffles",
#     description="crumbly",
    # category_id=3
# )
# session.add(cookies)
# session.add(cookies3)
# session.commit()