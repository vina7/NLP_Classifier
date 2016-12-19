#Vinayak Nesarikar
import pandas
import csv
import numpy as np
from sklearn.model_selection import KFold
#imports the learning model you would like to use
from sklearn.naive_bayes import BernoulliNB
from sklearn.externals import joblib
url = "Out/Overall.csv"
names = ['Username', 'Tweet', 'noise', 'removetoyotaUsernames', 'keeponlyclosesentiment', 'keeponlyToyotahashtags', 'keeponlytoyotasubject', 'removeUnrelatewordsfortest', 'Time','Non-long tweets','allavesubjectstogether']
dataframe = pandas.read_csv(url, names=names)
array=dataframe.values
#used for cross validation
kf = KFold(n_splits=10)
cfr = BernoulliNB()
#used for cross validation
target = np.array( [x[2] for x in array] )
train = np.array([x[3:] for x in array])
results =[]
notnoisearray = [0] * len(array)
for train2, test2 in kf.split(train):
  probas = cfr.fit(train[train2], target[train2])
  prediction = probas.predict(train[test2])
  print(len(prediction)) 
  results.append(prediction)
  counter =0
  for x in prediction:
    num = test2[counter]
    counter = counter +1
    print(x)
    #needs to be changed if you want to use logistic regression
    if(x== "no"):
      notnoisearray[num]=1
cleantweets=[]
counter =0 
print(notnoisearray)
for x in notnoisearray:
  if x == 1:
    cleantweets.append(array[counter])
  counter = counter+1
print(cleantweets)  
#writes out the tweet info that the model things is clean
with open ("Out/Filtered.csv", 'wb') as outfile:
  writer = csv.writer(outfile)
  writer.writerows(cleantweets)
    
    
    
