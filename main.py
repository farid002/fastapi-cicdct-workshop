from fastapi import FastAPI
from api.conversion import router as conversion_router
from api.oghuz import router as oghuz_router
from api.farhad import router as farhad_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the conversion API!"}

app.include_router(conversion_router)
app.include_router(oghuz_router)
app.include_router(farhad_router)
