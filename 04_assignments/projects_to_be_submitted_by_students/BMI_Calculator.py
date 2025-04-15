import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your height (in cm):", 100, 250, 170)
weight = st.slider("Enter your weight (in kg):", 30, 200, 70)

bmi = weight / ((height / 100) ** 2)

st.write(f"Your BMI is **{bmi:.2f}**")

if bmi < 18.5:
    st.write("🟡 You are **underweight**")
elif 18.5 <= bmi <= 24.9:
    st.write("🟢 Your weight is **normal**")
elif 25 <= bmi <= 29.9:
    st.write("🟠 You are **overweight**")
else:
    st.write("🔴 You are **obese**")
