from fastapi import FastAPI
import database
# from pydantic import BaseModel
import uvicorn
app = FastAPI()

#

# SQLALCHEMY_URL = "postgresql://postgres:123@localhost/mydb"
# engine = create_engine(
#     SQLALCHEMY_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# db = SessionLocal()

# Base = declarative_base()
# class Shop(Base):
#     __tablename__ = "products"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     price = Column(Float)
#
# Base.metadata.create_all(bind=engine)
#
# Модель
# class Item(BaseModel):
#    name: str
#    description: Union[str, None] = None
#    price: float
#    tax: Union[float, None] = None

@app.post("/post/")
async def create_item(data:Item):
    return {"message": "Hello World"}
@app.get("/")
async def root():
    return {"message": "Hello World"}

# git remote add origin https: // github.com /RumWar/Ych-practika.git http_proxy=http://10.0.21.52:3128

uvicorn.run(app)