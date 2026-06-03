from textblob import TextBlob
import pandas as pd

reviews = [
    "This product is amazing and very useful.",
    "I love this service.",
    "The quality is very poor.",
    "Not bad, but could be better.",
    "Excellent experience and fast delivery.",
    "Worst purchase ever."
]

results = []

for review in reviews:
    polarity = TextBlob(review).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    results.append([review, sentiment, polarity])

df = pd.DataFrame(results, columns=["Review", "Sentiment", "Polarity"])

print("\nSentiment Analysis Results\n")
print(df)

print("\nSentiment Count\n")
print(df["Sentiment"].value_counts())