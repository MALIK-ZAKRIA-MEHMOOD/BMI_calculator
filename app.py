import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert height from cm to meters
    bmi = weight / (height_m ** 2)
    return bmi

# Function to classify BMI based on the result
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Streamlit App
st.title("BMI Calculator")

# Input fields for weight and height
weight = st.number_input("Enter your weight in kilograms:", min_value=0.0, step=0.1)
height_cm = st.number_input("Enter your height in centimeters:", min_value=0.0, step=0.1)

# Button to calculate BMI
if st.button("Calculate BMI"):
    if weight > 0 and height_cm > 0:
        # Calculate BMI
        bmi = calculate_bmi(weight, height_cm)
        classification = classify_bmi(bmi)
        
        # Display BMI and classification
        st.success(f"Your BMI is: {bmi:.2f}")
        st.info(f"Based on your BMI, you are classified as: {classification}")
    else:
        st.error("Please enter valid numbers for both weight and height.")

# Footer
st.markdown("---")
st.markdown("Designed by [MALIK ZAKRIA MEHMOOD](https://github.com/MALIK-ZAKRIA-MEHMOOD/)")
