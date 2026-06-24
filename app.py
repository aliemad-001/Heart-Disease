import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Heart Disease Predictor")

st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient details below")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=40)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.number_input("Chest Pain Type", min_value=0, max_value=3)
trestbps = st.number_input("Resting Blood Pressure", value=120)
chol = st.number_input("Cholesterol", value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.number_input("Resting ECG", min_value=0, max_value=2)
thalach = st.number_input("Maximum Heart Rate", value=150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak", value=1.0)
slope = st.number_input("Slope", min_value=0, max_value=2)
ca = st.number_input("Number of Major Vessels", min_value=0, max_value=4)
thal = st.number_input("Thal", min_value=0, max_value=3)

# Convert Male/Female to numbers
sex = 1 if sex == "Male" else 0

# Predict button
if st.button("Predict"):

    input_data = np.array([
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]).reshape(1, -1)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")
    
