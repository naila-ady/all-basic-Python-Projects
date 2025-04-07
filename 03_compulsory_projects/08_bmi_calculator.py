import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(page_title="BMI Calculator", layout="centered")

# Title with custom styling
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌟 BMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("---")

# User Input Section
col1, col2 = st.columns(2)
with col1:
    height_unit = st.selectbox("Select height unit", ["cm", "ft/inches"])  # Dropdown for height unit
    if height_unit == "cm":
        height = st.text_input("Height (in cm)", "170")  # Text input for height in cm
    else:
        feet = st.text_input("Height (in feet)", "5")  # Text input for height in feet
        inches = st.text_input("Height (in inches)", "8")  # Text input for height in inches

with col2:
    weight_unit =st.selectbox("Select weight unit",["gm" ,"kg"])
    if weight_unit == "gm":
        weight = st.text_input("Weight (in kg)", "70000")  # Text input for weight
    else:
        weight = st.text_input("Weight in" ,"70")

# Check if inputs are valid
try:
    # Convert height based on the selected unit
    if height_unit == "cm":
        height = float(height)
    else:
        feet = float(feet)
        inches = float(inches)
        height = (feet * 30.48) + (inches * 2.54)  # Convert feet and inches to cm
    
    if weight_unit == "gm":
        weight = float(weight)/1000
    
    else:
        weight =float(weight)
       
    
    # Calculate BMI
    bmi = weight / ((height / 100) ** 2)
    
    # Determine the BMI category
    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        color = "green"
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "orange"
    else:
        category = "Obese"
        color = "red"
    
    # Display BMI and category with color
    st.markdown(f"""
    <div style='text-align:center;'>
        <h2>Your BMI: <span style='color:{color}'>{bmi:.2f}</span></h2>
        <h3 style='color:{color}'>Category: {category}</h3>
    </div>
    """, unsafe_allow_html=True)
    
except ValueError:
    st.error("Please enter valid numbers for height and weight.")


category_data = pd.DataFrame({
    'BMI Category': ['Underweight', 'Normal weight', 'Overweight', 'Obese'],
    'BMI Range': ['< 18.5', '18.5 – 24.9', '25 – 29.9', '30+'],
    'Description': [
        'BMI less than 18.5',
        'BMI between 18.5 and 24.9',
        'BMI between 25 and 29.9',
        'BMI 30 or greater'
    ]
})

# Display the table in Streamlit
st.markdown("### 💡 BMI Category Information")
st.table(category_data)
