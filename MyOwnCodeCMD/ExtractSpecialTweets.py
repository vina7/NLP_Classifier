#!/usr/bin/env python
from os import listdir
from os.path import isfile, join
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
from os import listdir
from os.path import isfile, join
from Preprocessing import preprocessingMethods
from preparingListOfTweets import preparingListOfTweets
import csv


class ExtractSpecialTweets:

    fileAddressOfTweets = []
    AllHateTweets=[]
    AllLoveTweets=[]
    AllHateUsernameWithNameOfBrands = []
    AllLoveUsernameWithNameOfBrands = []
    

    def CollectListOfTweetsOfBrands(self, sentimnent, FileAddressOfTweets):
        self.fileAddressOfTweets = FileAddressOfTweets
        
        for brand in self.fileAddressOfTweets:
            Temp=[]
            for tweetFile in brand:
                Temp.append(self.ReadFiles(tweetFile))
            if sentimnent == 'Hate':
                self.AllHateTweets.append(Temp)
            else:
                self.AllLoveTweets.append(Temp)
                    
        
    
    def ReadFiles(self, address):
        # Read each Tweet excel file and extract the Tweet which is row[3]
        Temp=[]
        with open(address, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                Temp.append(row[3])
        return Temp
    
