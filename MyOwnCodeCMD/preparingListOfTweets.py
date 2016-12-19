import csv
import sys
from os import listdir
from os.path import isfile, join, isdir

class preparingListOfTweets:

    DirectoryPath = ""
    ListOfBrands = ""
    HateListOfFilesOfBrands = []
    LoveListOfFilesOfBrands = []

    def resetparameters(self):
        DirectoryPath = ""
        ListOfBrands = ""
        LoveListOfFilesOfBrands = [] 
    
    
    def __init__(self, path):
        self.DirectoryPath=path

    def finfFoldersOfDirectory(self):
        self.ListOfBrands = [name for name in listdir(self.DirectoryPath) if isdir(join(self.DirectoryPath, name))]
        if '.DS_Store' in self.ListOfBrands:
            self.ListOfBrands.remove('.DS_Store')
        

    def fillListOfPathsForBrands(self, sentiment):
        for brandName in self.ListOfBrands:
            DirectoryExtension = self.DirectoryPath +  brandName + '/'+ sentiment + '/' 	
            FileNames = self.findFilesOfDirectory(DirectoryExtension)
            TempList=[]
            for fileName in FileNames:
                TempList.append(DirectoryExtension + fileName)
            if  sentiment=='Hate':
                self.HateListOfFilesOfBrands.append(TempList)
            else:
                self.LoveListOfFilesOfBrands.append(TempList)
                

    def findFilesOfDirectory(self, directoryExtension):
        onlyfilesList = [f for f in listdir(directoryExtension) if isfile(join(directoryExtension, f))]
        if '.DS_Store' in onlyfilesList:
            onlyfilesList.remove('.DS_Store')
        return (onlyfilesList)
    

