# Modèle spaCy
import spacy
# from spacy.lang.fr.stop_words import STOP_WORDS

class NLPModel:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            # Fallback sans modèle chargé
            self.nlp = spacy.blank("en")
            print("⚠️  Using blank spaCy model (no NLP features)")

    def analyze(self, text: str):
        doc = self.nlp(text)
        return doc

# Instance globale du modèle
nlp_model = NLPModel()