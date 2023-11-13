from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# git remote add origin https: // github.com / RumWar / Ych - practika.git

uvicorn.run(app)