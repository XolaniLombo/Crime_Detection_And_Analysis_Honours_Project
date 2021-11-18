import string
from num2words import num2words
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import emoji
import json
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
import validators as validators
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
class TextProcessor:
    def __init__(self):
        self.a = 9
    def replace_emojis(text):
        dec = emoji.demojize(text)
        list = dec.split()
        new_text = ''
        for word in list:
            if word[0] == ':' and word[len(word) - 1] == ":" and word.find('_') > 0:
                word = word[1:-1]  # remove 1st and last :
                word = word.replace('_', ' ')
                new_text += " " + word
            else:
                new_text += " " + word
        return new_text.lstrip()
    def remove_mention_and_url(text):
        #replace url, remove mention, remove #
        list = text.split()
        post = ""
        for word in list:
            if len(word) > 0 and word[0] == '@':
                post += " user" # replace mention with 'user' name
            elif validators.url(word):
                post += " URL" # replace url with word url
            elif word.isnumeric(): # convert number to words
                post += " "+ num2words(word)
            else:
                post += " " + word
        return post.lstrip()

    def remove_punctuation(text):
        no_punct = " ".join([word.strip(string.punctuation) for word in text.split(" ")])
        return no_punct

    def remove_stopwords(text):
        words = [w for w in text if w not in stopwords.words('english')]
        return words

    def word_lemmatizer(text):
        lemmatizer = WordNetLemmatizer()
        lem = [lemmatizer.lemmatize(i) for i in text]
        return lem

    def word_stemmer(text):
        stemmer = PorterStemmer()
        # stem = " ".join([stemmer.stem(i) for i in text])
        stem = [stemmer.stem(i) for i in text]
        return stem