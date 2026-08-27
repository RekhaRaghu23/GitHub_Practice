import streamlit as st

st.title("Add Two Numbers")

st.write("Simple Streamlit app to add two numbers.")

a = st.number_input("Enter first number", value=0.0, format="%.3f")
b = st.number_input("Enter second number", value=0.0, format="%.3f")

if st.button("Add"):
    result = a + b
    st.success(f"Result: {result}")

st.write("Current sum:", a + b)
