# Pour formatter des réponses
def format_medical_result(doc):
    """Formate les résultats de spaCy pour l'API."""
    entities = [
        (ent.text, ent.label_) for ent in doc.ents
    ]

    # Détection de spécialité basique
    medical_fields = {
        "cardiology": ["heart", "cardiac", "cardiovascular"],
        "neurology": ["brain", "nerve", "neurological", "neurology"],
        "pediatrics": ["child", "children", "pediatric"],
        "dermatology": ["skin", "dermatological", "dermatology"],
        "orthopedics": ["bone", "fracture", "joint", "cast"]
    }

    detected_fields = []
    text_lower = doc.text.lower()
    for field, keywords in medical_fields.items():
        if any(keyword in text_lower for keyword in keywords):
            detected_fields.append(field)

    return {
        "text": doc.text,
        "detected_fields": detected_fields if detected_fields else ["general"],
        "entities": entities,
    }
