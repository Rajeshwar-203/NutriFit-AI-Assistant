# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.ai_controller import router as ai_router

app = FastAPI(title="Fitness AI Backend")

# Allow your frontend (adjust origin if needed)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(ai_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Fitness AI backend is running"}
