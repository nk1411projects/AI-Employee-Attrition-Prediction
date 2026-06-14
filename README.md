# AI-Powered Employee Attrition Prediction & HR Analytics Platform

Live Demo:

https://ai-attrition-prediction.streamlit.app

Screenshots:

<img width="850" height="796" alt="Screenshot 2026-06-14 142539" src="https://github.com/user-attachments/assets/9c5d56c2-d377-4c12-b61f-3b3973434242" />

<img width="850" height="847" alt="Screenshot 2026-06-14 142511" src="https://github.com/user-attachments/assets/67faff17-a151-43b4-90ca-743f7af45f14" />

<img width="850" height="883" alt="Screenshot 2026-06-14 143041" src="https://github.com/user-attachments/assets/127fe0ca-a0a4-48fa-8be9-6d16848bfbc5" />

<img width="850" height="984" alt="Screenshot 2026-06-14 142946" src="https://github.com/user-attachments/assets/191202cb-7274-443a-85e0-d1084e843ce3" />

<img width="850" height="1018" alt="Screenshot 2026-06-14 142934" src="https://github.com/user-attachments/assets/33336560-17bb-48f9-bc25-e66f14aeb8ba" />


## Overview

Employee attrition is a major challenge for organizations as it leads to increased recruitment costs, loss of productivity, and disruption of business operations.

This project uses Machine Learning and Explainable AI to predict employee attrition risk and provide actionable HR insights. The platform helps HR professionals identify employees who may leave the organization and supports data-driven retention strategies.

---

## Problem Statement

Employee turnover can negatively impact organizational performance. HR teams often struggle to identify employees at risk of leaving before attrition occurs.

The objective of this project is to:

* Predict employee attrition using Machine Learning
* Identify key factors influencing employee turnover
* Provide business insights for HR decision-making
* Improve employee retention strategies

---

## Dataset

Dataset: IBM HR Analytics Employee Attrition Dataset

Features include:

* Age
* Monthly Income
* Job Satisfaction
* Environment Satisfaction
* Work Life Balance
* Overtime
* Years at Company
* Years Since Last Promotion
* Total Working Years
* Marital Status
* Stock Option Level
* And other employee-related attributes

Target Variable:

* Attrition (Yes / No)

---

## Tech Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn
* Logistic Regression

### Explainable AI

* SHAP

### Deployment

* Streamlit

---

## Machine Learning Pipeline

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. One-Hot Encoding
5. Train-Test Split
6. Logistic Regression Model Training
7. Model Evaluation
8. Threshold Optimization
9. SHAP Explainability
10. Streamlit Deployment

---

## Model Performance

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 84.69% |
| Precision | 52.78% |
| Recall    | 40.43% |
| F1 Score  | 45.78% |
| ROC-AUC   | 79.27% |

The model was optimized to improve employee attrition detection rather than relying solely on accuracy.

---

## Key Findings

* Employees working overtime have a higher attrition risk.
* Low job satisfaction significantly increases turnover probability.
* Lack of promotions contributes to employee attrition.
* Employees with fewer stock options are more likely to leave.
* Career stagnation is a major attrition driver.

---

## Explainable AI (SHAP)

SHAP was used to explain model predictions and identify the most influential features.

Top factors affecting attrition:

* OverTime
* Marital Status
* Years Since Last Promotion
* Job Satisfaction
* Environment Satisfaction
* Stock Option Level
* Num Companies Worked
* Monthly Income

---

## Application Features

### Home Page

* Project Overview
* Navigation Guide

### Dashboard

* KPI Metrics
* Attrition Analysis
* Department Insights
* Overtime Insights

### Attrition Prediction

* Employee Risk Prediction
* Risk Score
* Risk Classification
* HR Recommendations

### Business Insights

* HR Analytics
* Attrition Trends
* Business Findings
* SHAP Insights

---

## Future Enhancements

* Random Forest and XGBoost models
* Real-time database integration
* Employee retention recommendation engine
* Cloud deployment
* Advanced HR analytics dashboard

---

## Author

Nithish Kumar

Aspiring AI/ML Engineer | MERN stack Developer

---

## License

This project is intended for educational and portfolio purposes.
