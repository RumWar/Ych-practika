from typing import List

from fastapi import FastAPI, HTTPException, Depends
import query, post, models
from database import Session, engine
import uvicorn
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()


app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"], )
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/home/", response_model=List[post.Sweet])
async def output(db: Session = Depends(get_db)):
    Sweet = query.get_all(db);
    return Sweet

@app.get("/category/", response_model=List[post.Category1])
def read_user(db: Session = Depends(get_db)):
    category = query.get_category(db)
    return category

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/")
async def root():
    return {"Message": "Root"}







# git remote add origin https: // github.com /RumWar/Ych-practika.git http_proxy=http://10.0.21.52:3128

uvicorn.run(app)