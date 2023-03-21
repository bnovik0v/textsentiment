# TextSentiment

TextSentiment is a Python library for text preprocessing and sentiment analysis. It provides a user-friendly API for chaining preprocessing tasks, supports multiple languages and text formats, and integrates with major NLP libraries.

## Features

* Easy-to-use API for text preprocessing
* Support for multiple languages and text formats
* Simple interface for sentiment analysis using pre-trained models
* Integration with popular NLP libraries like spaCy, NLTK, and gensim

## Installation

To install TextSentiment, simply run:

```sh
pip install textsentiment
```

## Quick Start

```python
from textsentiment import PreprocessingPipeline, SentimentAnalyzer

# Create a preprocessing pipeline
pipeline = PreprocessingPipeline()
pipeline.add_tokenizer()
pipeline.add_stemmer()
pipeline.add_lemmatizer()
pipeline.add_stopword_removal()

# Process input text
processed_text = pipeline.process(input_text)

# Perform sentiment analysis
analyzer = SentimentAnalyzer(model="en_core_web_sm")
sentiment_score = analyzer.analyze(processed_text)

print(f"Sentiment score: {sentiment_score}")
```

For more detailed documentation and examples, please visit [our project website](https://textsentiment.example.com).

## Contributing

We welcome contributions to TextSentiment! If you're interested in contributing, please check out [our contributing guidelines](https://textsentiment.example.com/contributing).

## License

TextSentiment is released under [the MIT License](https://opensource.org/licenses/MIT).
