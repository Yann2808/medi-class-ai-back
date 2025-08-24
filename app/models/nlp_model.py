# Modèle spaCy
import spacy
# from spacy.lang.fr.stop_words import STOP_WORDS

class NLPModel:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def analyze(self, text: str):
        doc = self.nlp(text)
        return doc

# Instance globale du modèle
nlp_model = NLPModel()