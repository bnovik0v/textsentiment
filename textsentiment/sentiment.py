import spacy


class SentimentAnalyzer:
    def __init__(self, model="en_core_web_sm"):
        self.model = self.load_model(model)

    def load_model(self, model_name):
        return spacy.load(model_name)

    def analyze(self, input_text):
        doc = self.model(input_text)
        return doc.sentiment
