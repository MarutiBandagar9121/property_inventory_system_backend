from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import api_router

app = FastAPI(title="EstateHub API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
def home():
    return {"message": "EstateHub API is running"}