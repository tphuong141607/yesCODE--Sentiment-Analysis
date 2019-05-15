# yesCODE--Sentiment-Analysis
The project is created on May 10, 2019

### What is it?
The program calculates the word sentiment level, based on the user reviews from the Yelp academic dataset.

The provided data file has 156,602 reviews written by Yelp members (the original dataset has 1,569,265 reviews). Each review has a text fragment and a star rating on the scale from1 (worst) to 5 (best). We assume that the words predominantly used in "bad" reviews are "bad" and the words predominantly used in "good" reviews are "good." The measure of the sentiment level of a word, therefore, is the average star rating of all reviews where the word is used. 

### Processing steps:
1. Load the JSON data from the file using a JSON reader.
2. Extract all review texts and star ratings.
3. Break each review into individual words using NLTK. 
4. Lemmatize the words.
5. Filter out stop words and words that are not in the words corpus.
6. For each lemma, calculate its average star rating. If a lemma is used in fewer than 10 reviews, discard it.
7. Save the 500 most negative lemmas and 500 most positive lemmas and their respective sentiment levels in a one two-column CSV file (the lemmas in the first column, the levels in the second column), sorted in the descending order of sentiment levels.

## How to run this program on your computer locally?
#### Notes: The program takes approximately 20 minutes to run and process the whole data set. 
1. Download Anaconda Navigator [here](https://www.anaconda.com/distribution/#download-section)
2. Install Spider within Anaconda Navigator
3. Launch Spider and import the source code (File --> Open --> select the analysis.py)
4. Run the program
#### The result file: [sentiment_analysis.csv](https://github.com/tphuong141607/yesCODE--Sentiment-Analysis/blob/master/result/sentiment_analysis.csv)
