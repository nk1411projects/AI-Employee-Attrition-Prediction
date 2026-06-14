import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="Employee Attrition Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# KPI Calculations
attrition_rate = round(
    (df["Attrition"] == "Yes").mean() * 100,
    2
)

high_risk = df[df["Attrition"] == "Yes"].shape[0]

avg_income = int(df["MonthlyIncome"].mean())

avg_years = round(
    df["YearsAtCompany"].mean(),
    2
)

# Title
st.title("📊 AI-Powered Employee Attrition Prediction System")

st.markdown("---")

# KPI Section
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Total Employees",
        len(df)
    )

with col2:
    st.metric(
        "Attrition Rate",
        f"{attrition_rate}%"
    )

with col3:
    st.metric(
        "Average Income",
        f"${avg_income}"
    )

with col4:
    st.metric(
        "Employees Left",
        high_risk
    )

with col5:
    st.metric(
        "Avg Years At Company",
        avg_years
    )

st.markdown("---")

# Attrition by Department
dept_attrition = (
    df.groupby("Department")["Attrition"]
    .apply(lambda x: (x == "Yes").sum())
    .reset_index(name="AttritionCount")
)

fig1 = px.bar(
    dept_attrition,
    x="Department",
    y="AttritionCount",
    title="Attrition by Department"
)



# Attrition by Overtime
overtime_attrition = (
    df.groupby("OverTime")["Attrition"]
    .apply(lambda x: (x == "Yes").sum())
    .reset_index(name="AttritionCount")
)

fig2 = px.pie(
    overtime_attrition,
    values="AttritionCount",
    names="OverTime",
    title="Attrition by Overtime"
)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)
# Footer
st.markdown("---")

st.caption(
    "AI-Powered Employee Attrition Prediction System | Built with Python, Scikit-Learn, SHAP & Streamlit"
)