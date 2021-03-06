#Vinayak Nesarikar
import pandas
import csv
import numpy as np
from sklearn.model_selection import KFold
#imports the learning model you would like to use
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
url = "Out/Overall.csv"
names = ['Username', 'Tweet', 'noise', 'removetoyotaUsernames', 'keeponlyclosesentiment', 'keeponlytoyotasubject', 'removeUnrelatewordsfortest']
dataframe = pandas.read_csv(url, names=names)
array=dataframe.values
#used for cross validation
kf = KFold(n_splits=10)
cfr = LogisticRegression()
#used for cross validation
target = np.array( [x[2] for x in array] )
train = np.array([x[3:] for x in array])
results =[]
notnoisearray = [0] * len(array)
for train2, test2 in kf.split(train):
  probas = cfr.fit(train[train2], target[train2])
  prediction = probas.decision_function(train[test2])
  #check = probas.predict_log_proba(train[test2])
  print(probas.coef_) 
  results.append(prediction)
  counter =0
  for x in prediction:
    num = test2[counter]
    counter = counter +1
    #print(x)
    #needs to be changed if you want to use logistic regression
    if((x<=.226)):
      notnoisearray[num]=1
      
cleantweets=[]
counter =0 
#print(notnoisearray)
for x in notnoisearray:
  if x == 1:
    cleantweets.append(array[counter])
  counter = counter+1
#print(cleantweets)  
#writes out the tweet info that the model things is clean
with open ("Out/Filtered.csv", 'wb') as outfile:
  writer = csv.writer(outfile)
  writer.writerows(cleantweets)
    
    
    
