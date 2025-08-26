from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="MediClassAI API", version="1.0.0")

# Inclusion des routes
app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "MediClassAI API - Utilisez /api/v1/classify"}