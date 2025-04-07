import streamlit as st

# Set the page configuration
st.set_page_config(page_title="BMI Calculator", layout="centered")

# Title with custom styling
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌟 BMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("---")

# User Input Section
col1, col2 = st.columns(2)

# Height Input
with col1:
    height_unit = st.selectbox("Select height unit", ["cm", "ft/inches"])  # Dropdown for height unit
    if height_unit == "cm":
        height = st.text_input("Height (in cm)")  # Text input for height in cm
    else:
        feet = st.text_input("Height (in feet)")  # Text input for height in feet
        inches = st.text_input("Height (in inches)")  # Text input for height in inches

# Weight Input
with col2:
    weight_unit = st.selectbox("Select weight unit", ["gm","kg and gm",])   # Dropdown for kg and gm option
    
    if weight_unit == "gm":
        weight = st.text_input("Weight (in gm)")  # Text input for weight in kilograms
    else:
        kg = st.text_input("Weight (in kg)")  # Text input for weight in kilograms
        gm = st.text_input("Weight (in gm)")  # Text input for weight in grams

# Check if inputs are valid and calculate BMI
try:
    # Convert height based on the selected unit
    if height_unit == "cm":
        height = float(height)
    else:
        feet = float(feet)
        inches = float(inches)
        height = (feet * 30.48) + (inches * 2.54)  # Convert feet and inches to cm
    
    # Convert weight based on the selected unit
    if weight_unit == " gm":
        weight = float(weight)
    else:
        kg = float(kg)
        gm = float(gm)
        weight = kg + (gm / 1000)  # Convert gm to kg and sum it with kg

    # Calculate BMI
    bmi = weight / ((height / 100) ** 2)  # BMI formula
    
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
