import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Business Insights",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Business Insights")

st.markdown("""
This page provides HR-focused insights derived from employee attrition analysis.
""")

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

st.header("🔍 Key Findings")

st.info("""
1. Employees working overtime show higher attrition.

2. Lack of promotion is a major attrition driver.

3. Employees with low satisfaction are more likely to leave.

4. Stock options improve retention.

5. Career stagnation is strongly associated with attrition.
""")

st.header("🏢 Attrition Rate by Department")

dept_rate = (
    df.groupby("Department")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="AttritionRate")
)

st.bar_chart(
    dept_rate.set_index("Department")
)

st.header("⏰ Overtime Impact")

overtime_rate = (
    df.groupby("OverTime")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="AttritionRate")
)

st.dataframe(overtime_rate)

st.header("😊 Job Satisfaction Analysis")

satisfaction_rate = (
    df.groupby("JobSatisfaction")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="AttritionRate")
)

st.line_chart(
    satisfaction_rate.set_index("JobSatisfaction")
)

st.header("🚀 Promotion vs Attrition")

promotion_rate = (
    df.groupby("YearsSinceLastPromotion")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="AttritionRate")
)

st.line_chart(
    promotion_rate.set_index("YearsSinceLastPromotion")
)

st.header("🤖 Model Insights (SHAP)")

st.success("""
Top Factors Influencing Attrition:

• Years In Current Role

• Years With Current Manager

• Years Since Last Promotion

• Num Companies Worked

• Monthly Income

• Environment Satisfaction

• Stock Option Level

• Job Satisfaction
""")