from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/profile"):
async def root():
    return {"message": "This is my profile"}

