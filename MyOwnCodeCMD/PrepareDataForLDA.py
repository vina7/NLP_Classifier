import sys
from LDAForYelp import A
from os import path, makedirs
from os.path import exists


class PrepareDataForLDA:

    DataForEachBrandLove = []
    DataForEachBrandHate = []
    DataForHate =[]
    DataForLove =[]
    BranNames = []
    Sentiment = ""

    

    def __init__(self, branNames, TopicNo, TopicWordNo, Passes):
        self.BranNames = branNames
        self.topicNumber = TopicNo
        self.topicWordNumber = TopicWordNo
        self.passes = Passes
    
    def prepareDataForEachBrand(self, document, sentiment ):
        Document = []
        self.Sentiment = sentiment
        for row in document:
            Temp = []
            Doc = ""
            for col in row:
                for Tweet in col:
                    Doc = Doc + " " + Tweet
                Temp.append(Doc)
            Document.append(Temp)
            
        if sentiment == "Hate":
            self.DataForEachBrandHate = Document
        else:
            self.DataForEachBrandLove = Document
        

    def prepareDataForEachDate(self, document, sentiment ):
        Document = []
        self.Sentiment = sentiment
        for row in document:
            Temp = []
            for col in row:
                for Tweet in col:
                    Temp.append(Tweet)
            
            Document.append(Temp)
            
        if sentiment == "Hate":
            self.DataForEachBrandHate = Document
        else:
            self.DataForEachBrandLove = Document

    def prepareDataForEachDateAllBrands(self, document, sentiment ):
        Document = []
        self.Sentiment = sentiment
        Temp = []
        for row in document:
            for col in row:
                for Tweet in col:
                    Temp.append(Tweet)
            
            Document.append(Temp)
            
        if sentiment == "Hate":
            self.DataForEachBrandHate = Document
        else:
            self.DataForEachBrandLove = Document
        

            
    def prepareDataForEachSentiment(self, document, sentiment):
        Document = []
        self.Sentiment = sentiment
        for row in document:
            for col in row:
                for Tweet in col:
                    Document.append(Tweet)
        if sentiment == "Hate":
            self.DataForHate = Document
        else:
            self.DataForLove = Document

    def callLDAForEachSentiment(self):
        directory = './Output/Sentiments/'
        if not exists(directory ):
             makedirs(directory)

        x=A()
        x.func("Hate",self.DataForHate, self.topicNumber , self.topicWordNumber, self.passes )
        x.func("Love",self.DataForLove, self.topicNumber , self.topicWordNumber, self.passes)

    def callLDAForEachBrand(self):
        directory = './Output/Brands/'
        counter=0
        for  names in self.BranNames:
            if not exists(directory + names + '/Hate/'):
                makedirs(directory + names + '/Hate/')
            if not exists(directory + names + '/Love/'):
                makedirs(directory + names + '/Love/')
            x = A()
            x.func("Hate", self.DataForEachBrandHate[counter], self.topicNumber , self.topicWordNumber, self.passes)
            counter = counter + 1

    def callLDAForAllBrands(self):
        directory = './Output/Brands/'
        counter=0
        if not exists(directory + '/AllBrands/Hate/'):
            makedirs(directory +  '/AllBrands/Hate/')
        if not exists(directory + '/AllBrands/Love/'):
            makedirs(directory + '/AllBrands/Love/')
            
        x = A()
        x.func("Hate", self.DataForEachBrandHate[counter], self.topicNumber , self.topicWordNumber, self.passes)
        counter = counter + 1
        
        

            
                
                    
            
