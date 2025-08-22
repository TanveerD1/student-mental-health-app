from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.backend.db.connection import engine, Base  # Fixed import path

# Import your models to create tables
from app.backend.db import models  # Fixed import path

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Mental Health API", version="0.1.0")

# Add CORS middleware to allow frontend communication later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only. Restrict this later.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mental Health API"}

@app.get("/health")
def health_check():
    return {"status": "OK"}