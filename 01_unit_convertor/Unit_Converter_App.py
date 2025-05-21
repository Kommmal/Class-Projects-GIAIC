import streamlit as st

st.title("Unit Converter App")
st.markdown("### Converts Length, Weight, And Time Instantly")
st.write("Welcome to unit convertor app! Select a category and enter value to convert.")

conversion_type = st.selectbox("Choose a type to convert", ["Length", "Weight", "Temperature"])

# Length Conversion
if conversion_type == "Length":
    st.subheader("📏 Length Converter")
    value = st.number_input("Enter length value")
    
    from_unit = st.selectbox("From", ["Meters", "Kilometers"])
    

    if from_unit == "Meters":
        to_unit = st.selectbox("To", ["Kilometers"])
        result = value / 1000
    elif from_unit == "Kilometers":
        to_unit = st.selectbox("To", ["Meters"])
        result = value * 1000
    else:
        result = value

    st.write("Result:", result)

# Weight Conversion
elif conversion_type == "Weight":
    st.subheader("⚖️ Weight Converter")
    value = st.number_input("Enter weight value")

    from_unit = st.selectbox("From", ["Kilograms", "Grams"])
    
    if from_unit == "Kilograms":
        to_unit = st.selectbox("To", ["Grams"])
        result = value * 1000
    elif from_unit == "Grams":
        to_unit = st.selectbox("To", ["Kilograms"])
        result = value / 1000
    else:
        result = value

    st.write("Result:", result)

# Temperature Conversion
elif conversion_type == "Temperature":
    st.subheader("🌡️ Temperature Converter")
    value = st.number_input("Enter temperature")

    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    
    if from_unit == "Celsius":
        to_unit = st.selectbox("To", ["Fahrenheit"])
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit":
        to_unit = st.selectbox("To", ["Celsius"])
        result = (value - 32) * 5/9
    else:
        result = value

    st.write("Result:", result)
