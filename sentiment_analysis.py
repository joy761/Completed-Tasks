#importing spacy and pandas
import spacy
import pandas as pd
#add the textblob component to the pipeline
from spacytextblob.spacytextblob import spacyTextBlob

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob')

#making dataframe from csv file
df = pd.read_csv('Amazon_product_reviews.csv')
clean_data = df.dropna(subset=['reviews.text']) # Remove all missing values
reviews_data = clean_data['reviews.text'] # Selects the column of reviews we want to analyse.

print("Hello, we are analysing an Amazon Product reviews Data base with 5000 products.")

first_review = -1
second_review = -1

while not (0 <= first_review <= 4999 and 0 <= second_review <= 4999):

    try:
        first_review = int(input("What will be the first review to analyse? "))
        second_review = int(input("What will be the second review to analyse? "))

    except ValueError:
        print("Please enter integers.")


def tokenize_review(review):
    #Function to tokenize our reviews

    doc = nlp(review)
    return doc


def remove_stop_words(review):
    #Function to remove stop words from reviews 

    # Creates a list with all the words not included in the stop words from Spacy.
    filtered_review = [token for token in review if not token.is_stop]
    # Gets our list of filtered tokens back as a spaCy doc.
    filtered_doc = spacy.tokens.Doc(review.vocab, words=[token.text for token in filtered_review])
    return filtered_doc


def get_polarity(review):
    #Function to get the sentiment from a review 

    analysis = TextBlob(review.text)
    polarity = analysis.polarity
    return polarity


def compare_reviews(review1 , review2):
    #Function to compare two reviews and retrieve its similarity coeficient

    coefficient = review1.similarity(review2)
    return coefficient


def get_sentiment(polarity):
  #Function to recieve the polarity and retrieve its sentiment  

    if 0.2 > polarity > -0.2:
        return "neutral"

    if 1 >= polarity > 0.2:
        return "positive"

    return "negative"

# Indexing our review in the DF.
first_choice_review = reviews_data[first_review]
second_choice_review = reviews_data[second_review]

# Tokenizing and removing stopwords.
clean_first_choice_review = remove_stop_words(tokenize_review(first_choice_review))
clean_second_choice_review = remove_stop_words(tokenize_review(second_choice_review))

print(f"Review nr: {first_review} : {first_choice_review}")
print(f"Review nr: {second_review} : {second_choice_review}")

first_polarity = get_polarity(clean_first_choice_review)
second_polarity = get_polarity(clean_second_choice_review)

similarity = compare_reviews(clean_first_choice_review , clean_second_choice_review)

first_review_sentiment = get_sentiment(first_polarity)
second_review_sentiment = get_sentiment(second_polarity)

print(f"Polarity for review nr {first_review}: {first_polarity},", end = " " )
print(f"{first_review_sentiment} feeling.")
print(f"Polarity for review nr {second_review}: {second_polarity},", end = " ")
print(f"{second_review_sentiment} feeling.")
print(f"Similarity between both: {similarity}")