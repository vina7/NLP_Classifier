#!/usr/bin/env python
#The LDA does not distribute the data as well as I thought it would.
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import unicodedata
import gensim
from os import listdir
from os.path import isfile, join
import pyLDAvis.gensim
from Preprocessing import preprocessingMethods

class A:
    
    preprocessingMethodsObj = preprocessingMethods()
    
    def readfile(self, adr):
        address = '../StopWordCollection/' + adr
        Words = []
        with open(address) as f:
            for line in f:
                Words.append(line.rstrip())
        return Words

    def hasHashTagInTheBeginning(self, word):

        word = word.strip()
        print ('word')
        print (word)
        if word.startswith( '#' ):
            return True
        return False

        
    def func(self, sentiment, Document, TopicNumber, TopicWordNumber, NumberOfPasses):
        #--------------------------Parameter Initialization--------------------------
        
        tokenizer = RegexpTokenizer(r'\w+')
        texts = []# list for tokenized documents in loop

        #--------------------------create English stop words list--------------------------
        
        en_stop = get_stop_words('en') # StopWords from NLTK
        
        Searchengines = self.readfile('SearchEngines.txt') # From http://www.webconfs.com/stop-words.php
        en_stop = en_stop + Searchengines 
        
        MyStopWordList = self.readfile('MyList.txt') # Selected by me from tweet data
        en_stop = en_stop + MyStopWordList

        Slanglist = self.readfile('SlangList.txt') # Slang list from http://www.webopedia.com/quick_ref/textmessageabbreviations.asp
        en_stop = en_stop + Slanglist

        ListExtractedFromTweets = self.readfile('ListExtractedFromTweets.txt') # Slang list from http://www.webopedia.com/quick_ref/textmessageabbreviations.asp
        en_stop = en_stop + ListExtractedFromTweets

        #-------------------------- Create p_stemmer of class PorterStemmer--------------------------
        p_stemmer = PorterStemmer()
        # --------------------------Read Reviews with rank 3--------------------------
        doc_set = Document  
        #-----------------------Delete the header from the document----------------
        del doc_set[0] 
        #-----------------------------loop through document list-------------------------------------
        for i in doc_set:
            
            # read Tweets and lowecase the whole sentence.
            raw = i.lower()

            # Collect Hashtags
            Hashtags = self.preprocessingMethodsObj.findHashtags(raw)
            Hashtags = [unicode(i) for i in Hashtags]
            
            # Exclude hashtags and Emoticons from the Tweet
            raw = self.preprocessingMethodsObj.removingHashtags(raw)
            
            # Clean and tokenize document string
            tokens = tokenizer.tokenize(raw)
	    
    
            # remove stop words from tokens
            stopped_tokens = [] 
            for i in tokens:
                i=i.decode('utf-8','ignore').encode('utf-7')
	        if not ((i in en_stop) or i in Hashtags):
                    stopped_tokens.append(i)
            
            # stem tokens 
            stemmed_tokens = []
	    for i in stopped_tokens:
		val = p_stemmer.stem(i)
                stemmed_tokens.append(unicodedata.normalize('NFKD', val).encode('ascii','ignore')) 
            
            # Delete Emoticons
            stemmed_tokens2 = []
            for i in stemmed_tokens:
                if not ( "_" in i or "?" in i):
                    stemmed_tokens2.append(i)
            stemmed_tokens = filter(None, stemmed_tokens2)
            # Add Hashtags
            stemmed_tokens = stemmed_tokens + Hashtags
    
            # add tokens to list
            texts.append(stemmed_tokens)
            
        #----------------------turn our tokenized documents into a id <-> term dictionary-----------------
        dictionary = corpora.Dictionary(texts)
        
        #print('Dictionary:')
        #for keys,values in dictionary.items():
            #print(keys)
            #print(values)

        #-------------convert tokenized documents into a document-term matrix-------------
        corpus = [dictionary.doc2bow(text) for text in texts]
        # --------------------------generate LDA model--------------------------
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, TopicNumber, id2word = dictionary, passes=NumberOfPasses)
        Output=ldamodel.print_topics(TopicNumber, TopicWordNumber)
        print(Output)
##        
##
        target = open("../Topics/" + sentiment + "Topic" + str(TopicNumber) + "Word" + str( TopicWordNumber) + "Passes" + str(NumberOfPasses) + ".txt", 'w')
        for rows in Output:
            Words=[];
            for cols in rows:
                if "+" in str(cols):
                    B=str(cols).split('+')
                    for elems in B:
                        C=str(elems).split('*')
                        Words.append( C[1] );
            print(Words)

            for words in Words:
                target.write(str(words))
            target.write('\n')
        target.close()
        
       # --------------------------Visualization part--------------------------
##        followers_data =  pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary)
##        pyLDAvis.save_html(followers_data,"../VisualizationResult/" + sentiment + "Topic" + str(TopicNumber) + "Word" + str( TopicWordNumber) + "Passes" + str(NumberOfPasses) + ".html")
##        pyLDAvis.show(followers_data)
##        print ('------------------------')

