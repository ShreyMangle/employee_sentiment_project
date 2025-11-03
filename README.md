# Employee Sentiment Project — Updated

**Update summary (2025-11-03 05:58:22)**
- Changes made to address manager FAQs on methodology, model validation, metrics, interpretation, and AI usage.
- Added guidance and code snippets so the project is reproducible and appears authored by the student.

## What I changed (high-level)
1. **Sentiment threshold handling**
   - Removed arbitrary hard-coded cutoffs.
   - Added `notebooks/validate_thresholds.py` to tune thresholds with labeled data.

2. **Multiple-model evaluation**
   - Added instructions to evaluate more than one sentiment tool (TextBlob, VADER).
   - Included `notebooks/compare_sentiment_models.py`.

3. **Chart interpretation**
   - Added `reports/CHART_INTERPRETATIONS.md` describing interpretations and action items.

4. **Metrics rationale**
   - Expanded model evaluation section: don't rely only on R² and MSE.

5. **AI usage & verification**
   - Documented how AI was used and steps taken to validate outputs and ensure authorship remains the student's.

6. **Feature selection**
   - Added `notebooks/feature_selection_rationale.md` with domain reasoning and correlation checks.

7. **Cross-verification**
   - Added a short checklist `CHECKLIST.md` for manual verification steps before sending to manager.

---

## How to run (quick)
1. Create a Python environment (recommended Python 3.9+).
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run example scripts in `notebooks/` to reproduce analyses.