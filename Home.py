import streamlit as st

st.set_page_config(
    page_title="Employee Attrition Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI-Powered Employee Attrition Prediction System")

st.markdown("""
Welcome to the Employee Attrition Analytics Platform.

This application helps HR teams:

✅ Analyze employee attrition trends

✅ Predict employee resignation risk

✅ Understand business insights

✅ Improve employee retention
""")

st.markdown("---")

st.subheader("Available Pages")

st.write("📈 Dashboard")
st.write("🔮 Predict Attrition")
st.write("📊 Business Insights")

st.markdown("---")

st.info(
    "Built using Python, Scikit-Learn, SHAP, Plotly and Streamlit."
)