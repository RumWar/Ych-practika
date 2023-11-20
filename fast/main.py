from typing import List

from fastapi import FastAPI, HTTPException, Depends
import query, post, models
from database import Session, engine
import uvicorn


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

@app.get("/home/{category}", response_model=List[post.Sweet])
def read_user(category: int, db: Session = Depends(get_db)):
    db_user = query.get_category(db, category=category)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/")
async def root():
    return {"message": "Hello World"}


# git remote add origin https: // github.com /RumWar/Ych-practika.git http_proxy=http://10.0.21.52:3128

uvicorn.run(app)