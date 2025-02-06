import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
nltk.download('stopwords')
ps = PorterStemmer()

set_stopwords=set(stopwords.words('english'))

def RemoveStopWords(text):
    words=text.split()
    print(words)
 
    filter_words=[w for w in words if w not in set_stopwords]

    return  (filter_words)

text="Hello my name is Akash and i am looking forwarded to make friend with you."
filterd_text=RemoveStopWords(text)

print("{0:20}{1:20}".format("--Word--","--Stem--"))
for word in filterd_text:
   print ("{0:20}{1:20}".format(word, ps.stem(word)))