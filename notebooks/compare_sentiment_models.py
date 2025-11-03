"""
compare_sentiment_models.py

Compare basic sentiment scorers (TextBlob, VADER) on a small sample.
This is an example; customize to your dataset.
"""
import sys
import pandas as pd
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.metrics import classification_report

def tb_score(text):
    return TextBlob(text).sentiment.polarity

def vader_score(sia, text):
    return sia.polarity_scores(text)['compound']

def to_label(score, neg=-0.33, pos=0.33):
    if score <= neg:
        return "negative"
    elif score >= pos:
        return "positive"
    else:
        return "neutral"

def main(path):
    df = pd.read_csv(path)
    sia = SentimentIntensityAnalyzer()
    df['tb'] = df['text'].apply(tb_score)
    df['vader'] = df['text'].apply(lambda t: vader_score(sia, t))
    df['tb_label'] = df['tb'].apply(to_label)
    df['vader_label'] = df['vader'].apply(to_label)
    print("TextBlob performance:")
    print(classification_report(df['label'], df['tb_label'], zero_division=0))
    print("VADER performance:")
    print(classification_report(df['label'], df['vader_label'], zero_division=0))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compare_sentiment_models.py path/to/labeled.csv")
    else:
        main(sys.argv[1])