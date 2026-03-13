from fastapi import FastAPI # type: ignore
from app.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Adaptive Diagnostic Engine Running"}