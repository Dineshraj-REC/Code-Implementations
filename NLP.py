import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

text = """
Natural Language Processing is a field of Artificial Intelligence.
It helps computers understand human language.
NLP is used in chatbots, translation, and sentiment analysis.
"""

sentences = sent_tokenize(text)
words = word_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

word_freq = Counter(stemmed_words)

pos_tags = nltk.pos_tag(words)

print("Sentences:")
print(sentences)

print("\nWords:")
print(words)

print("\nFiltered Words:")
print(filtered_words)

print("\nStemmed Words:")
print(stemmed_words)

print("\nWord Frequency:")
print(word_freq)

print("\nPOS Tags:")
print(pos_tags)
