import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("Credit_Card_Model")

# Page config
st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

# Reduce top spacing using CSS
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
        h1 {
            margin-bottom: 0.2rem;
        }
        p {
            margin-top: 0;
            margin-bottom: 1.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# Heading
st.markdown("<h1 style='text-align: center;'>Credit Card Fraud Detection</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter the transaction details below to check if it is normal or fraudulent.</p>", unsafe_allow_html=True)

# Input form
show_result = False
inputs = []

with st.form("fraud_form"):
    cols = st.columns(4)
    for i in range(28):
        with cols[i % 4]:
            value = st.number_input(f"Feature {i+1}", value=0.0, key=f"feature_{i+1}")
            inputs.append(value)

    # Amount field
    with cols[0]:
        amount = st.number_input("Amount", value=0.0, key="amount")
        inputs.append(amount)

    submit = st.form_submit_button("Predict")

# Prediction functionality
if submit:
    prediction = model.predict([inputs])
    if prediction[0] == 0:
        st.success("This is a normal transaction.")
    else:
        st.error("This is a fraudulent transaction.")
