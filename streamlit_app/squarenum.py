import streamlit as st

def sqr(num):
    return num ** 2

st.title("Square a Number")

num = st.number_input("Enter a number to square")

if st.button("Calculate Square"):
    result = sqr(num)
    st.success(f"The square of {num} is: {result}")