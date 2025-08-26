from fastapi import APIRouter
from pydantic import BaseModel
from app.models.nlp_model import nlp_model
from app.utils.formatters import format_medical_result

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.get("/classify")
@router.post("/classify")
async def classify_text(request: TextRequest):
    """Endpoint principal de classification"""
    doc = nlp_model.analyze(request.text)
    return format_medical_result(doc)

@router.get("/healthcheck")
async def health_check():
    """Health check pour Render"""
    return {"status": "healthy", "model_loaded": True}