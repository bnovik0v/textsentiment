class PreprocessingPipeline:
    def __init__(self):
        self.tasks = []

    def add_tokenizer(self, tokenizer=None):
        if tokenizer is None:
            from .utils import default_tokenizer
            tokenizer = default_tokenizer
        self.tasks.append(('tokenize', tokenizer))

    def add_stemmer(self, stemmer=None):
        if stemmer is None:
            from .utils import default_stemmer
            stemmer = default_stemmer
        self.tasks.append(('stem', stemmer))

    def add_lemmatizer(self, lemmatizer=None):
        if lemmatizer is None:
            from .utils import default_lemmatizer
            lemmatizer = default_lemmatizer
        self.tasks.append(('lemmatize', lemmatizer))

    def add_stopword_removal(self, stopword_removal=None):
        if stopword_removal is None:
            from .utils import default_stopword_removal
            stopword_removal = default_stopword_removal
        self.tasks.append(('remove_stopwords', stopword_removal))

    def process(self, input_text):
        for task_name, task_func in self.tasks:
            input_text = task_func(input_text)
        return input_text
