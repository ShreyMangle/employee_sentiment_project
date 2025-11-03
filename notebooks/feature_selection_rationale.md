# Feature Selection Rationale

1. Keep features that have a plausible causal link to the target.
2. Remove identifiers and leakage features (e.g. employee ID, future labels).
3. Use correlation heatmaps and model-based importance (tree-based) to prune.
4. Examples of excluded features: 'email font size', 'random uuid', 'file path'.

Recommended steps:
- Compute correlation with the target.
- Train a light tree model and inspect feature importances.
- Manually validate top features against domain logic.