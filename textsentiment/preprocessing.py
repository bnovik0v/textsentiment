import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

class PreprocessingPipeline:
    def __init__(self):
        self.tasks = []

    def add_tokenizer(self, tokenizer=None):
        if tokenizer is None:
            tokenizer = word_tokenize
        self.tasks.append(('tokenize', tokenizer))

    def add_stemmer(self, stemmer=None):
        if stemmer is None:
            stemmer = PorterStemmer().stem
        self.tasks.append(('stem', stemmer))

    def add_lemmatizer(self, lemmatizer=None):
        if lemmatizer is None:
            lemmatizer = WordNetLemmatizer().lemmatize
        self.tasks.append(('lemmatize', lemmatizer))

    def add_stopword_removal(self, stopword_removal=None):
        if stopword_removal is None:
            stopword_removal = self.remove_stopwords
        self.tasks.append(('remove_stopwords', stopword_removal))

    def process(self, input_text):
        for task_name, task_func in self.tasks:
            input_text = task_func(input_text)
        return input_text

    @staticmethod
    def remove_stopwords(tokens, language='english'):
        stop_words = set(stopwords.words(language))
        return [word for word in tokens if word.lower() not in stop_words]
