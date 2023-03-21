import json
import re
from bs4 import BeautifulSoup


def load_text_from_json(json_data, key):
    data = json.loads(json_data)
    return data.get(key, '')


def load_text_from_html(html_data, tag=None, class_=None, id_=None):
    soup = BeautifulSoup(html_data, 'html.parser')

    if tag:
        elements = soup.find_all(tag, class_=class_, id_=id_)
        text = ' '.join([element.get_text() for element in elements])
    else:
        text = soup.get_text()

    return text


def remove_html_tags(text):
    clean_text = re.sub('<[^>]*>', '', text)
    return clean_text


def default_tokenizer(text):
    # Implement the default tokenizer function.
    pass


def default_stemmer(text):
    # Implement the default stemmer function.
    pass


def default_lemmatizer(text):
    # Implement the default lemmatizer function.
    pass


def default_stopword_removal(text):
    # Implement the default stopword removal function.
    pass

