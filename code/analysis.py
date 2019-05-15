import time
import csv
start = time.time()
import json
import nltk
from nltk.corpus import stopwords
from nltk.corpus import words
from collections import Counter

JSON_FILE_NAME = 'yelp_academic_dataset_review_small.json'
DATA_DIRECTORY = '../data/'
RESULT_DIRECTORY = '../result/'

# Load the JSON data from the file and start extracting data
with open(DATA_DIRECTORY + JSON_FILE_NAME, 'r') as outfile:
    loaded_json = json.load(outfile)   
    print("The length of loaded JSON file: " + str(len(loaded_json)) + '\n')
    print("Working on calculation...\n")
    
# Extract all review texts and star rating to a list of dictionaries {'t': "text", 'r': "rate" }
review = 0
review_star = []
while (review < len(loaded_json)):
#while (review < 5000):
    review_star.append({'t':loaded_json[review]['text'], 'r':loaded_json[review]['stars']}) 
    review += 1

#Pos Tagging 
pos_translate = {"J" : "a", "V" : "v", "N" : "n", "R" : "r"}
def pos2pos(tag):
    if tag in pos_translate: return pos_translate[tag] 
    else: return "n"

# Lemmatize word: Create a list of dictionaries 
# [{lemmatized word:rate}{lemmatized word:rate}..so on] 
lem = nltk.WordNetLemmatizer()
lemma_star = ({lem.lemmatize(word, pos2pos(pos[0])):eachReview['r']
            for word, pos in nltk.pos_tag(nltk.word_tokenize(eachReview['t'].lower()))}
            for eachReview in review_star)


# Removing stop words and words that are not in words corpus 
stop_words_set = set(stopwords.words('english'))
words_words_set = set(words.words())

processed_lemma_star = [{lemma : star for lemma, star in  lemma_star_pair.items()
                        if lemma not in stop_words_set and lemma in words_words_set}
                        for lemma_star_pair in lemma_star]


          
# Calculating the average sentiment level of a word and append its value to averageDict
# {lemma: sentiment level}
averageDict = dict() 
for lemma_star_pair in processed_lemma_star:
    for lemma, star in lemma_star_pair.items():
        if lemma not in averageDict:
            averageDict[lemma] = star
        elif lemma in averageDict:
            averageDict[lemma] = (averageDict[lemma] + star) / 2

# RESULT: only take lemmas that appear in more than or equal to 10 reviews
counter = Counter([lemma for lemmaStar in processed_lemma_star for lemma in lemmaStar.keys()])
finalLemmaList = [[lemma, averageDict.get(lemma)] for lemma, count in counter.items() if count >= 10]

# Sort the final list based on the sentiment level
finalLemmaList.sort(key=lambda elem: elem[1])
bestReview = finalLemmaList[-500:]
worseReview = finalLemmaList[:500]
mergeReviews = bestReview + worseReview

#write a csv file with 500 most negative and 500 most positive pairs
with open(RESULT_DIRECTORY + 'sentiment_analysis.csv', 'w', newline='') as outfile:
    thewriter = csv.writer(outfile)
    thewriter.writerow(['word', 'average'])
    thewriter.writerows(mergeReviews)
    

end = time.time()
print("The time it took to get the results for " + str(review) + " reviews is: " + str(end - start) + ' seconds')
    
