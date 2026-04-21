from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Demand Planning Test API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Hello World !!!!!"}