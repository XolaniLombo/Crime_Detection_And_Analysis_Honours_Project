import pickle

from nltk.tokenize import RegexpTokenizer
# from keras.preprocessing.sequence import pad_sequences
from TextProcessor import TextProcessor
from sklearn.feature_extraction.text import TfidfVectorizer

class Detector:
    def __init__(self):
        self.a = 4
    def norm(self,list):
        sent = ""
        for word in list:
            sent += " "+word
        return sent.strip()

    def feature(message,max_length):

        #text preprocessing
        tokenizer = RegexpTokenizer(r'\w+')
        message = TextProcessor.replace_emojis(message)
        message = TextProcessor.remove_mention_and_url(message)
        message = TextProcessor.remove_punctuation(message)
        message = TextProcessor.tokenizer.tokenize(message.lower())
        message = TextProcessor.remove_stopwords(message)
        message = TextProcessor.word_stemmer(message)
        message = TextProcessor.word_lemmatizer(message)

        cv = TfidfVectorizer()

        features = cv.fit_transform(message).toarray()
        features = pad_sequences(features, padding='post',maxlen=max_length, dtype='float64')
        return features

    def detect_crime(self,message):
        f = self.feature(message,19490)
        filename = './Models/SVM_model.sav'
        # load the model from disk
        loaded_model = pickle.load(open(filename, 'rb'))
        y_pred = loaded_model.predict(f)
        if y_pred[0] == 0:
            return "Normal"
        else:
            return "Crime Related"

    def analyse_crime(self,message):
        f = self.feature(message,20141)
        filename = './Models/Random_forest_model.sav'
        # load the model from disk
        loaded_model = pickle.load(open(filename, 'rb'))
        y_pred = loaded_model.predict(f)

        if y_pred[0] == 0:
            return "Normal"
        elif y_pred[0] == 1:
            return "Hate Speech"
        elif y_pred[0] == 2:
            return "Offensive"
        elif y_pred[0] == 3:
            return "Attack Related Crime"
        else:
            return "Drug Related"



