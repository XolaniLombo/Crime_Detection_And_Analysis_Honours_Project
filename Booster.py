
import re
class DetectorBooster:
    def __init__(self,filename):
        self.file = open(filename,"r")
        self.key_words = []

    def detect(self):
        crime_sentences = ""
        self.extractor()
        tot = 0
        # sentences =  self.file.read().split(".")
        sentences = re.split('\.|\?|!', self.file.read())

        # print(sentences)

        for s in sentences:
            s = s.strip()

            if len(s) > 4: # meaningful sentence
                ar_s = s.split(" ")
                for word in  ar_s:
                    if word.lower() in self.key_words:

                        crime_sentences += s + "."
                        break
                tot+=1
        my_list = crime_sentences.split(".")[:-1]
        crime_rate = len(my_list) /  tot
        return my_list, crime_rate

    def extractor(self):

        att = open("Files/Attack_Related_Words.txt", "r")
        for line in att:
            self.key_words.append(line.lower().strip())

        dg = open("Files/Drug_Related_Words.txt", "r")
        for line in dg:
            self.key_words.append(line.lower().strip())


class AnalyzorBooster:
    def __init__(self,filename):
        self.attack_key_words = []
        self.drug_key_words = []
        self.file = open(filename,"r")
        self.key_words = []

    def analyse(self):
        drug_sentences = ""
        attack_sentences = ""
        self.extractor()
        tot = 0
        # sentences =  self.file.read().split(".")
        sentences = re.split('\.|\?|!|\n', self.file.read())



        for s in sentences:
            s = s.strip()
            if len(s) > 4: # meaningful sentence
                ar_s = s.split(" ")
                for word in  ar_s:
                    if word.lower() in self.drug_key_words:
                        drug_sentences += s + "."
                        break
                    elif word.lower() in self.attack_key_words:
                        attack_sentences += s + "."
                        break

                tot+=1
        my_list = attack_sentences.split(".")[:-1]
        my_list_2 = drug_sentences.split(".")[:-1]
        attack_rate = len(my_list) /  tot
        drug_rate = len(my_list_2) /  tot
        return my_list,my_list_2, attack_rate, drug_rate

    def extractor(self):

        att = open("Files/Attack_Related_Words.txt", "r")
        for line in att:
            self.attack_key_words.append(line.lower().strip())

        dg = open("Files/Drug_Related_Words.txt", "r")
        for line in dg:
            self.drug_key_words.append(line.lower().strip())
