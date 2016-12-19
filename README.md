# NLP_Classifier
Made By: Vinayak Nesarikar

This repository holds the code for the noise classifier and LDA pipeline. It also has the test results for each model used.

To run the filter.py:</br>
python filter.py</br>
output: Overall.csv</br>
The feature headers follows this order (left to right)</br>
 removeToyotaUsernames </br>
  keeponlyclosesentiment </br>
  keeponlyToyotahashtags </br>
  keeponlytoyotasubject</br>
  removeUnrelatewordsfortest</br>
  remove1to4amtime</br>
  removelongtweets</br>
  keeponlyavesubjects

To run the supervised_pipe_line.py:</br>
python supervised_pipe_line.py</br>
output: Filtered.csv</br>
The feature headers follows this order (left to right)</br>
 removeToyotaUsernames </br>
  keeponlyclosesentiment </br>
  keeponlyToyotahashtags </br>
  keeponlytoyotasubject</br>
  removeUnrelatewordsfortest</br>
  remove1to4amtime</br>
  removelongtweets</br>
  keeponlyavesubjects

To run the LDA pipeline: 
read the Instruction for running the pipeline the pipeline.docx

 The directory structure follows the structure for the original code base provided. 
 The Directory Structure is a follows:
 
 -BernoulliNB_test_results</br>
 --BernoulliNB_test_results.csv
 
 -Current_Nonfiltered_data</br>
 --AllOfFilesCombinedWithFeatureResults.csv</br>
 --Toyota-January-2016-hate.csv</br>
 --Toyota-January-2016-love.csv</br>
 --Toyota-March-2016-hate.csv</br>
 --Toyota-March-2016-love.csv</br>
 --Toyota-November-2015-hate.csv</br>
 --Toyota-November-2015-love.csv</br>
 --Toyota-October-2015-hate.csv</br>
 --Toyota-October-2015-love.csv</br>
 --Toyota-September-2015-hate.csv</br>
 --Toyota-September-2015-love.csv
 
 -logistic_regression_results</br>
 --Logistic_Regression_Results.csv
 
 -ManualData</br>
 --Toyota</br>
 ---Hate</br>
 (same as the .csv files found in the Current_Nonfiltered_data. Put the .csv files you would like to use with the python scripts in this directory. The file will need to have their headers removed from the file to work with the python scripts)</br>
 ----Toyota-January-2016-hate.csv</br>
 ----Toyota-January-2016-love.csv</br>
 ----Toyota-March-2016-hate.csv</br>
 ----Toyota-March-2016-love.csv</br>
 ----Toyota-November-2015-hate.csv</br>
 ----Toyota-November-2015-love.csv</br>
 ----Toyota-October-2015-hate.csv</br>
 ----Toyota-October-2015-love.csv</br>
 ----Toyota-September-2015-hate.csv</br>
 ----Toyota-September-2015-love.csv</br>
 
 -MultinomialNB_test_results</br>
 --Multinomial_test_results.csv
 
 -MyOwnCodeCMD</br>
 --Out </br>
 (output of filter.py and supervised_pipe_line.py is found here) </br>
 --Output</br>
 (LDA script output found here)</br>
 --checkingPipeline.py</br>
 --ExtractSpecialTweets.py</br>
 --filters.py</br>
 --Instruction for running the pipeline the pipeline.docx </br>
 --LDAForYelp.py</br>
 --negative&positive_words.txt</br>
 --np_extractor.py</br>
 --np_extractor.pyc</br>
 --PrepareDataForLDA.py</br>
 --preparingListOfTweets.py</br>
 --Preprocessing.py</br>
 --ReadCSV.py</br>
 --RegExpression.py</br>
 --remove_toyota_usernames.py</br>
 --supervised_pipe_line.py</br>
 --topic_unrelated_words.txt</br>
 --toyota_brand_words.txt</br>
 --toyota_brand_words_subject.txt
 
 -Original_Classification_data</br>
 --Feature_results.ods</br>
 --OriginalFilteredResults.csv</br>
 --AllOfFilesCombinedWithFeatureResults.csv</br>
 --Toyota-January-2016-hate.csv</br>
 --Toyota-January-2016-love.csv</br>
 --Toyota-March-2016-hate.csv</br>
 --Toyota-March-2016-love.csv</br>
 --Toyota-November-2015-hate.csv</br>
 --Toyota-November-2015-love.csv</br>
 --Toyota-October-2015-hate.csv</br>
 --Toyota-October-2015-love.csv</br>
 --Toyota-September-2015-hate.csv</br>
 --Toyota-September-2015-love.csv
 
 -StopWordCollection</br>
 (used for LDA)</br>
 --ListExtractedFromTweets.txt</br>
 --MyList.txt</br>
 --OriginalSlangList.txt</br>
 --SearchEngines.txt</br>
 --SlangList.txt
 
 -Topics</br>
 (Results for the LDA test with multiple lable combinations)</br>
 --ad,car,carcomparison,company,companycomparison,dealership.txt</br>
 --ad,car,carcomparison,company,companycomparison,dealershipFiltered.csv</br>
 --ad,car,carcomparison,company,companycomparison,dealership,isis,prop,racing.txt</br>
 -ad,car,carcomparison,company, companycomparison,dealership,isis,prop, racing, companyowned.txt</br>
 --ad,car,carcomparison,company,companycomparison, dealership,isis,prop,racing,companyownedFiltered.csv</br>
 --ad,car,carcomparison,company,companycomparison,dealership,isis,prop,racingFiltered.csv</br>
 --ad,car,carcomparison,company,dealership.txt</br>
 --ad,car,carcomparison,company,dealershipFiltered.csv</br>
 --ad,car,company,companycomparison,dealership.txt</br>
 --ad,car,company,companycomparison,dealershipFiltered.csv</br>
 --all.txt</br>
 --yesremoved.txt</br>
 --yesremovedFiltered.csv
 
