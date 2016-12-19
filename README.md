# NLP_Classifier
Made By: Vinayak Nesarikar

This repository holds the code for the noise classifier and LDA pipeline. It also has the test results for each model used.

To run the filter.py:
python filter.py
output: Overall.csv
The feature headers follows this order (left to right)
 removeToyotaUsernames 
  keeponlyclosesentiment 
  keeponlyToyotahashtags 
  keeponlytoyotasubject
  removeUnrelatewordsfortest
  remove1to4amtime
  removelongtweets
  keeponlyavesubjects

To run the supervised_pipe_line.py:
python supervised_pipe_line.py
output: Filtered.csv
The feature headers follows this order (left to right)
 removeToyotaUsernames 
  keeponlyclosesentiment 
  keeponlyToyotahashtags 
  keeponlytoyotasubject
  removeUnrelatewordsfortest
  remove1to4amtime
  removelongtweets
  keeponlyavesubjects

To run the LDA pipeline: 
read the Instruction for running the pipeline the pipeline.docx

 The directory structure follows the structure for the original code base provided. 
 The Directory Structure is a follows:
 
 -BernoulliNB_test_results
 --BernoulliNB_test_results.csv
 
 -Current_Nonfiltered_data
 --AllOfFilesCombinedWithFeatureResults.csv
 --Toyota-January-2016-hate.csv
 --Toyota-January-2016-love.csv
 --Toyota-March-2016-hate.csv
 --Toyota-March-2016-love.csv
 --Toyota-November-2015-hate.csv
 --Toyota-November-2015-love.csv
 --Toyota-October-2015-hate.csv
 --Toyota-October-2015-love.csv
 --Toyota-September-2015-hate.csv
 --Toyota-September-2015-love.csv
 
 -logistic_regression_results
 --Logistic_Regression_Results.csv
 
 -ManualData
 --Toyota
 ---Hate
 (same as the .csv files found in the Current_Nonfiltered_data. Put the .csv files you would like to use with the python scripts in this directory. The file will need to have their headers removed from the file to work with the python scripts)
 ----Toyota-January-2016-hate.csv
 ----Toyota-January-2016-love.csv
 ----Toyota-March-2016-hate.csv
 ----Toyota-March-2016-love.csv
 ----Toyota-November-2015-hate.csv
 ----Toyota-November-2015-love.csv
 ----Toyota-October-2015-hate.csv
 ----Toyota-October-2015-love.csv
 ----Toyota-September-2015-hate.csv
 ----Toyota-September-2015-love.csv
 
 -MultinomialNB_test_results
 --Multinomial_test_results.csv
 
 -MyOwnCodeCMD
 --Out 
 (output of filter.py and supervised_pipe_line.py is found here) 
 --Output
 (LDA script output found here)
 --checkingPipeline.py
 --ExtractSpecialTweets.py
 --filters.py
 --Instruction for running the pipeline the pipeline.docx
 --LDAForYelp.py
 --negative&positive_words.txt
 --np_extractor.py
 --np_extractor.pyc
 --PrepareDataForLDA.py
 --preparingListOfTweets.py
 --Preprocessing.py
 --ReadCSV.py
 --RegExpression.py
 --remove_toyota_usernames.py
 --supervised_pipe_line.py
 --topic_unrelated_words.txt
 --toyota_brand_words.txt
 --toyota_brand_words_subject.txt
 
 -Original_Classification_data
 --Feature_results.ods
 --OriginalFilteredResults.csv
 --AllOfFilesCombinedWithFeatureResults.csv
 --Toyota-January-2016-hate.csv
 --Toyota-January-2016-love.csv
 --Toyota-March-2016-hate.csv
 --Toyota-March-2016-love.csv
 --Toyota-November-2015-hate.csv
 --Toyota-November-2015-love.csv
 --Toyota-October-2015-hate.csv
 --Toyota-October-2015-love.csv
 --Toyota-September-2015-hate.csv
 --Toyota-September-2015-love.csv
 
 -StopWordCollection
 (used for LDA)
 --ListExtractedFromTweets.txt
 --MyList.txt
 --OriginalSlangList.txt
 --SearchEngines.txt
 --SlangList.txt
 
 -Topics
 (Results for the LDA test with multiple lable combinations)
 --ad,car,carcomparison,company,companycomparison,dealership.txt
 --ad,car,carcomparison,company,companycomparison,dealershipFiltered.csv
 --ad,car,carcomparison,company,companycomparison,dealership,isis,prop,racing.txt
 -ad,car,carcomparison,company, companycomparison,dealership,isis,prop, racing, companyowned.txt
 --ad,car,carcomparison,company,companycomparison, dealership,isis,prop,racing,companyownedFiltered.csv
 --ad,car,carcomparison,company,companycomparison,dealership,isis,prop,racingFiltered.csv
 --ad,car,carcomparison,company,dealership.txt
 --ad,car,carcomparison,company,dealershipFiltered.csv
 --ad,car,company,companycomparison,dealership.txt
 --ad,car,company,companycomparison,dealershipFiltered.csv
 --all.txt
 --yesremoved.txt
 --yesremovedFiltered.csv
 
