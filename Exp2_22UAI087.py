import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def remove_stop_words(sentence):

    words = sentence.split()

    filtered_words = [word for word in words if word not in stop_words]

    return ' '.join(filtered_words)

sentence = "This is an example of AkashPatilSir."
filtered_sentence = remove_stop_words(sentence)
print(filtered_sentence)
