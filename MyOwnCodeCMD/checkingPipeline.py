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
from ReadCSV import ReadCsv
from LDAForYelp import A
from PrepareDataForLDA import PrepareDataForLDA
import sys

# Initialize arguments
DirectoryPathArg = int(sys.argv[1])
LDATopicNo = int(sys.argv[2])
LDATopicWordNo = int(sys.argv[3])
LDAPasses = int(sys.argv[4])
LDADocPreparationMethodArg = int(sys.argv[5])
LDAMEthodArg = int(sys.argv[6])


# Initialization
if DirectoryPathArg == 1:
    DirectoryPath = '../OriginalData/'
elif DirectoryPathArg == 2:
    DirectoryPath = '../HashtagDataOfAutoBrands/'
elif DirectoryPathArg == 3:
    DirectoryPath = '../ManualData/'
else:
    print 'Error in entering the DirectoryPathArg.'


# categorize the csv file addresses based on brands. After this phase, we have the list of brands.
preparingListOfTweetsObj = preparingListOfTweets(DirectoryPath)
preparingListOfTweetsObj.finfFoldersOfDirectory()
preparingListOfTweetsObj.fillListOfPathsForBrands("Hate")
preparingListOfTweetsObj.fillListOfPathsForBrands("Love")


# categorize the csv file based on brands
ReadCSVObj = ReadCsv()
ReadCSVObj.CollectListOfTweetsOfBrands("Hate", preparingListOfTweetsObj.HateListOfFilesOfBrands)
ReadCSVObj.CollectListOfTweetsOfBrands("Love", preparingListOfTweetsObj.LoveListOfFilesOfBrands)


# Preprocessing phase (it is better to be a class)
preprocessingMethodsObj = preprocessingMethods()
preprocessingMethodsObj.applyPreprocessing("Hate", ReadCSVObj.AllHateTweets)
preprocessingMethodsObj.applyPreprocessing("Love", ReadCSVObj.AllLoveTweets)

#prepare data for LDA. We have different methods for that. Please refer to the Report 2 and 3.
PrepareDataForLDAObj = PrepareDataForLDA(preparingListOfTweetsObj.ListOfBrands, LDATopicNo, LDATopicWordNo, LDAPasses)
if LDADocPreparationMethodArg == 1:
    PrepareDataForLDAObj.prepareDataForEachDateAllBrands(preprocessingMethodsObj.HateDocuments, "Hate")
    PrepareDataForLDAObj.prepareDataForEachDateAllBrands(preprocessingMethodsObj.LoveDocuments, "Love")
elif LDADocPreparationMethodArg == 2:    
    PrepareDataForLDAObj.prepareDataForEachDate(preprocessingMethodsObj.HateDocuments, "Hate")
    PrepareDataForLDAObj.prepareDataForEachDate(preprocessingMethodsObj.LoveDocuments, "Love")
elif LDADocPreparationMethodArg == 3: 
    PrepareDataForLDAObj.prepareDataForEachSentiment(preprocessingMethodsObj.HateDocuments, "Hate")
    PrepareDataForLDAObj.prepareDataForEachSentiment(preprocessingMethodsObj.LoveDocuments, "Love")
elif LDADocPreparationMethodArg == 4: 
    PrepareDataForLDAObj.prepareDataForEachBrand( preprocessingMethodsObj.HateDocuments, "Hate")
    PrepareDataForLDAObj.prepareDataForEachBrand( preprocessingMethodsObj.LoveDocuments, "Love")
else:
    print 'Error in entering the LDADocPreparationMethod.'
    

# Call LDA
if LDAMEthodArg == 1:
    PrepareDataForLDAObj.callLDAForAllBrands()
elif LDAMEthodArg == 2: 
    PrepareDataForLDAObj.callLDAForEachSentiment()
elif LDAMEthodArg == 3: 
    PrepareDataForLDAObj.callLDAForEachBrand()
else:
    print 'Error in entering the LDAMEthodArg.'






