import csv
import sys
import nltk
import re
from RegExpression import RegExpression 

class preprocessingMethods:

    HateDocuments=[]
    LoveDocuments=[]
    Documents=[]
    preprocessedTweets = []
    Sentiment=""
    RegExp = None
    
    def __init__(self):
        self.RegExp = RegExpression()
        

    def setParameters(self, sentiment, documents):
        self.Documents=[]
        self.Documents = documents
        self.Sentiment = sentiment
        

    def applyPreprocessing(self, sentiment, documents):
        self.setParameters(sentiment, documents)
        self.preprocessedTweets=documents
        rowcounter=0
        colcounter=0
        tweetcounter=0
        
        for row in self.Documents:
            colcounter=0            
            for col in row:
                tweetcounter=0
                for tweet in col:
                    self.preprocessedTweets[rowcounter][colcounter][tweetcounter] = self.preprocessingMethods(tweet)
                    tweetcounter = tweetcounter +1
                colcounter = colcounter + 1
            rowcounter = rowcounter +1
        self.setResult()

    def preprocessingMethods(self, tweet):
        tweet = self.removingMentions(tweet)
        tweet = self.removingURLs(tweet)
        return tweet

    def setResult(self):
        if self.Sentiment == "Hate":
            self.HateDocuments = self.preprocessedTweets
        else:
            self.LoveDocuments = self.preprocessedTweets

                
    def removingURLs(self, doc):
        regularExpression = self.RegExp.buildURLs()
        return re.sub(regularExpression , "", doc) 


    def removingMentions(self, doc):
        regExpStream = self.RegExp.buildMentions()
        return re.sub(regExpStream, "", doc)

    def removingHashtags(self, doc):
        regExpStream = self.RegExp.buildHashtags()
        return re.sub(regExpStream, "", doc)

    def findHashtags(self, doc):
        regExpStream = self.RegExp.buildHashtags()
        pattern = re.compile(regExpStream)
        return pattern.findall(doc)

    def findEmoticons(self, doc):
        regExpStream = self.RegExp.buildEmoticons()
        pattern = re.compile(regExpStream)
        return pattern.findall(doc)


    def removingEmoticons(self, doc):
        regularExpression = self.RegExp.buildEmoticons()
        return re.sub(regularExpression , "", doc) 
        
        


