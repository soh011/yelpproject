#Predicting Star Ratings from Yelp Reviews

##Research Question
'Can the use of positive and negative adjectives in a written Yelp review accurately predict the accompanying star rating for Las Vegas restaurants in 2016?'

##Hypothesis
'Yelp reviews significantly impact businesses by influencing customer perceptions and aiding in reputation management. I hypothesize that the language in written reviews strongly correlates with the star rating, with positive and negative language mirroring customer feelings.'

##Data Overview
### For this project the datasets are from the following Kaggle links
# *   https://www.kaggle.com/code/ambarish/a-very-extensive-data-analysis-of-yelp/input?select=yelp_business.csv
# *   https://www.kaggle.com/code/ambarish/a-very-extensive-data-analysis-of-yelp/input?select=yelp_review.csv
# *   https://www.kaggle.com/datasets/prajwalkanade/sentiment-analysis-word-lists-dataset/data?select=negative-words.txt
# *   https://www.kaggle.com/datasets/prajwalkanade/sentiment-analysis-word-lists-dataset/data?select=positive-words.txt
# *   https://www.kaggle.com/datasets/konradb/profanities-in-english-collection

### I plan to combine the first two datasets to filter restaurants in Las Vegas. Using the business IDs, I’ll perform a merge to link reviews with businesses, leaving only reviews for Las Vegas restaurants 