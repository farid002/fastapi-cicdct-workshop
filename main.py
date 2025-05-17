from fastapi import FastAPI
from api.conversion import router as conversion_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the conversion API!"}
app.include_router(conversion_router)
