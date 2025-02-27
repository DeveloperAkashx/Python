import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

# Download necessary NLTK modules
nltk.download('punkt')

# Step 3: Sample text input
text = "Natural Language Processing is an interesting field of study. It is widely used in various applications such as sentiment analysis, machine translation, and text summarization."

# Step 4: Tokenize the text into words
tokens = word_tokenize(text)

# Step 5: Apply n-grams generation
# You can change the 'n' value for different n-grams. Here, n = 2 for bigrams and n = 3 for trigrams
bigram = ngrams(tokens, 2)  # Change 2 to 3 for trigrams, etc.
trigram = ngrams(tokens, 3)

# Step 6: Display results
# Display bigrams
print("Bigrams:")
for bg in bigram:
    print(bg)

# Display trigrams
print("\nTrigrams:")
for tg in trigram:
    print(tg)
