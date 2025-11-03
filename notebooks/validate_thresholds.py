"""
validate_thresholds.py

Example script to help tune sentiment thresholds using labeled data.
Produces an evaluation table for candidate thresholds.

Usage: python validate_thresholds.py path/to/labeled.csv
"""

import sys
import pandas as pd
from sklearn.metrics import f1_score

def predict_with_thresholds(scores, neg_thr=-0.33, pos_thr=0.33):
    preds = []
    for s in scores:
        if s <= neg_thr:
            preds.append("negative")
        elif s >= pos_thr:
            preds.append("positive")
        else:
            preds.append("neutral")
    return preds

def evaluate(df, score_col='sentiment_score', label_col='label'):
    # try a few candidate thresholds
    candidates = [(-0.5,-0.2), (-0.33,0.33), (-0.2,0.2), (-0.1,0.1)]
    rows=[]
    for neg,pos in candidates:
        preds = predict_with_thresholds(df[score_col], neg, pos)
        f1 = f1_score(df[label_col], preds, average='macro', zero_division=0)
        rows.append({'neg_thr':neg, 'pos_thr':pos, 'f1_macro':f1})
    return pd.DataFrame(rows)

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_thresholds.py path/to/labeled.csv")
        return
    path = sys.argv[1]
    df = pd.read_csv(path)
    print("Evaluating thresholds on labeled data...")
    print(evaluate(df))

if __name__ == "__main__":
    main()