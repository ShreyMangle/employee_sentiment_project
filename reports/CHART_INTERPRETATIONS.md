# Chart Interpretations

- Sentiment over time (monthly): If sentiment drops for two consecutive months, check for HR events, policy changes, or product issues in that period. Correlate with support ticket volume.
- Distribution of sentiment: A spike in 'neutral' may indicate tool insensitivity. Validate with a sample of neutral texts.
- Model confusion matrix: Look at which classes get confused (e.g. neutral vs negative) and consider class-specific thresholds.