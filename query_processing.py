from datetime import datetime
from Stemmer import Stemmer
from stop_words import get_stop_words
import nltk
import re
import sys

startTime = datetime.now()
stop_words = get_stop_words('en')
p_stemmer = Stemmer('english')

while(1):
    query_text = raw_input("\nHi! Please enter your query:\n")
    text = re.sub('[^A-Za-z]', ' ', query_text)
    chunk = nltk.word_tokenize(title.lower())
    stopped_tokens = [i for i in chunk if not i in stop_words]
    field_tokens = p_stemmer.stemWords(stopped_tokens)
    print field_tokens
