# Auto-generated script for employee sentiment project
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('data/data_used.csv')
print('Loaded', df.shape)

mapping = {"date": "date", "feedback": "Subject", "employee_id": "Subject", "employee_name": "Subject", "department": null}

feedback_col = mapping.get('feedback')
if feedback_col is None:
    raise ValueError('No feedback column detected')

POS_WORDS = set(['love','great','good','happy','supportive','opportunities','growth','enjoy','excellent','satisfied','pleased','awesome'])
NEG_WORDS = set(['unhappy','poor','overworked','underpaid','toxic','stressful','leave','leaving','angry','bad','frustrated','problem'])

def rule_based_sentiment(text):
    txt = str(text).lower()
    pos = sum(1 for w in POS_WORDS if w in txt)
    neg = sum(1 for w in NEG_WORDS if w in txt)
    score = 0.0
    if pos+neg > 0:
        score = (pos - neg) / (pos + neg)
    label = 'Neutral'
    if score > 0.2:
        label = 'Positive'
    elif score < -0.2:
        label = 'Negative'
    return label, score

f = df[mapping.get('feedback')].astype(str)
df[['sentiment_label','sentiment_score']] = f.apply(lambda t: rule_based_sentiment(t)).apply(pd.Series)
df.to_csv('feedback_with_sentiment.csv', index=False)
print('Saved feedback_with_sentiment.csv')