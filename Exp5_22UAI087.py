import nltk
from nltk.util import ngrams
from collections import Counter
import random
nltk.download('punkt')

corpus = "The cat eats fish. The dog barks loudly. The cat sleeps peacefully."

tokens = nltk.word_tokenize(corpus.lower())

def generate_ngrams(tokens, n):
    return list(ngrams(tokens, n))

def train_ngram_model(tokens, n):
    n_grams = generate_ngrams(tokens, n)
    model = Counter(n_grams)
    return model

def predict_next_word(model, prev_words, n):
    prev_words = tuple(prev_words[-(n-1):])
    possible_ngrams = {k: v for k, v in model.items() if k[:-1] == prev_words}
    if not possible_ngrams:
        return None
    next_word = random.choices(
        population=[k[-1] for k in possible_ngrams.keys()],
        weights=possible_ngrams.values(),
        k=1
    )[0]
    return next_word

n = 3
ngram_model = train_ngram_model(tokens, n)

prev_words = ["the", "cat"]
predicted_word = predict_next_word(ngram_model, prev_words, n)

print(f"Given words: {prev_words}")
print(f"Predicted next word: {predicted_word}")
