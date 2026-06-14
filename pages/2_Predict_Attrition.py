import streamlit as st
import joblib
import pandas as pd
import numpy as np

model = joblib.load("logistic_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.title("🔮 Employee Attrition Prediction")

st.subheader("Personal Information")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=60,
    value=30
)

distance_from_home = st.number_input(
    "Distance From Home",
    min_value=1,
    max_value=50,
    value=5
)

marital_status = st.selectbox(
    "Marital Status",
    ["Single", "Married", "Divorced"]
)

overtime = st.selectbox(
    "OverTime",
    ["No", "Yes"]
)

st.subheader("Career Information")

total_working_years = st.number_input(
    "Total Working Years",
    min_value=0,
    max_value=40,
    value=10
)

years_at_company = st.number_input(
    "Years At Company",
    min_value=0,
    max_value=40,
    value=5
)

years_in_current_role = st.number_input(
    "Years In Current Role",
    min_value=0,
    max_value=20,
    value=3
)

years_since_last_promotion = st.number_input(
    "Years Since Last Promotion",
    min_value=0,
    max_value=20,
    value=1
)

years_with_curr_manager = st.number_input(
    "Years With Current Manager",
    min_value=0,
    max_value=20,
    value=3
)

num_companies_worked = st.number_input(
    "Number of Companies Worked",
    min_value=0,
    max_value=20,
    value=2
)

st.subheader("Compensation")

monthly_income = st.number_input(
    "Monthly Income",
    min_value=1000,
    max_value=50000,
    value=5000
)

stock_option_level = st.selectbox(
    "Stock Option Level",
    [0, 1, 2, 3]
)

st.subheader("Employee Satisfaction")

job_satisfaction = st.slider(
    "Job Satisfaction",
    1,
    4,
    3
)

environment_satisfaction = st.slider(
    "Environment Satisfaction",
    1,
    4,
    3
)

work_life_balance = st.slider(
    "Work Life Balance",
    1,
    4,
    3
)

if st.button("Predict Attrition Risk"):

    # Create empty employee record
    employee = pd.DataFrame(
        np.zeros((1, len(feature_columns))),
        columns=feature_columns
    )

    # Numerical features
    employee["Age"] = age
    employee["DistanceFromHome"] = distance_from_home
    employee["MonthlyIncome"] = monthly_income

    employee["TotalWorkingYears"] = total_working_years
    employee["YearsAtCompany"] = years_at_company
    employee["YearsInCurrentRole"] = years_in_current_role
    employee["YearsSinceLastPromotion"] = years_since_last_promotion
    employee["YearsWithCurrManager"] = years_with_curr_manager

    employee["NumCompaniesWorked"] = num_companies_worked

    employee["JobSatisfaction"] = job_satisfaction
    employee["EnvironmentSatisfaction"] = environment_satisfaction
    employee["WorkLifeBalance"] = work_life_balance

    employee["StockOptionLevel"] = stock_option_level

    # Categorical features
    if overtime == "Yes":
        employee["OverTime_Yes"] = 1

    if marital_status == "Married":
        employee["MaritalStatus_Married"] = 1

    elif marital_status == "Single":
        employee["MaritalStatus_Single"] = 1

    # Prediction
    probability = model.predict_proba(employee)[0][1]

    risk_percentage = round(
        probability * 100,
        2
    )

    # Risk category
    if probability < 0.30:
        risk_level = "🟢 LOW RISK"

    elif probability < 0.60:
        risk_level = "🟡 MEDIUM RISK"

    else:
        risk_level = "🔴 HIGH RISK"

    # Results
    st.markdown("---")

    st.metric(
        "Attrition Risk",
        f"{risk_percentage}%"
    )

    st.subheader(risk_level)

    # Progress bar
    st.subheader("Attrition Risk Score")

    st.progress(float(probability))

    st.metric(
        "Risk Percentage",
        f"{risk_percentage}%"
    )

    # Risk factors
    reasons = []

    if overtime == "Yes":
        reasons.append("Overtime")

    if job_satisfaction <= 2:
        reasons.append("Low Job Satisfaction")

    if environment_satisfaction <= 2:
        reasons.append("Low Environment Satisfaction")

    if years_since_last_promotion >= 5:
        reasons.append("No Recent Promotion")

    if stock_option_level == 0:
        reasons.append("No Stock Options")

    st.subheader("Top Risk Factors")

    if reasons:
        for reason in reasons:
            st.write(f"• {reason}")
    else:
        st.write("No major risk factors detected.")

    # HR Recommendations
    st.subheader("Recommended HR Actions")

    if probability >= 0.60:

        st.error("""
1. Schedule retention meeting

2. Review compensation package

3. Evaluate promotion opportunities

4. Improve work-life balance

5. Discuss career growth plan
""")

    elif probability >= 0.30:

        st.warning("""
Employee should be monitored.

Consider career development discussions.
""")

    else:

        st.success("""
Employee appears stable.

Continue normal engagement practices.
""")