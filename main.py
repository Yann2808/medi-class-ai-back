from fastapi import FastAPI
from pydantic import BaseModel
import spacy

# Charger un modèle spaCy pré-entraîné (petit modèle pour rapidité)
app = FastAPI()

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

class TextRequest(BaseModel):
    text: str

@app.post("/classify")
async def classify_text(request: TextRequest):
    doc = nlp(request.text)
    
    # Logique simple de détection basée sur les mots clés
    medical_fields = {
        "cardiology": ["heart", "cardiac", "blood pressure"],
        "neurology": ["brain", "nerve", "neurological"],
        "orthopedics": ["bone", "fracture", "joint"]
    }
    
    detected_fields = []
    for field, keywords in medical_fields.items():
        if any(keyword in request.text.lower() for keyword in keywords):
            detected_fields.append(field)
    
    return {
        "text": request.text,
        "detected_fields": detected_fields if detected_fields else ["general"],
        "entities": [(ent.text, ent.label_) for ent in doc.ents]
    }
