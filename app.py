import streamlit as st

st.set_page_config(
    page_title="Machine Learning Learning Hub",
    layout="wide"
)

st.title("Machine Learning Learning Hub")

st.write("""
Learn Machine Learning from basics to advanced concepts.
""")

st.header("Topics Covered")

topics = [
    "History of Machine Learning",
    "Learning Roadmap",
    "Data Preprocessing",
    "Train/Test Split",
    "Feature Scaling",
    "Linear Regression",
    "Decision Trees",
    "Random Forest",
    "Voting Classifier",
    "TPOT AutoML"
]

for topic in topics:
    st.markdown(f"✅ {topic}")

st.header("Machine Learning Lifecycle")

steps = [
    "Problem Definition",
    "Data Collection",
    "Data Cleaning",
    "Feature Engineering",
    "Model Training",
    "Evaluation",
    "Deployment"
]

for i, step in enumerate(steps, start=1):
    st.write(f"{i}. {step}")

st.success("Machine Learning Learning Hub is running successfully!")
