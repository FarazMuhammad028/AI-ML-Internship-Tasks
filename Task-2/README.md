# Customer Churn Prediction – ML Pipeline

## Objective
Build an end-to-end ML pipeline for predicting customer churn with preprocessing, hyperparameter tuning, and model export.

## Dataset
Telco Customer Churn Dataset (Kaggle)

## Methodology
- ColumnTransformer for preprocessing (numerical scaling + categorical encoding)
- Pipeline with Random Forest and Logistic Regression
- GridSearchCV for hyperparameter tuning
- Model evaluation: Accuracy, F1-score
- Export pipeline using Joblib

## Results
- Accuracy: ~82%
- F1-score: ~0.7

## Usage
```python
import joblib
model = joblib.load("churn_pipeline.joblib")
preds = model.predict(X_new)
