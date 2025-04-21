import nltk
import random
from nltk.corpus import words

nltk.download("words")
word_list = words.words()
random_words = random.sample(word_list, 50)
print(random_words)
