import streamlit as st

status=st.radio("Select your status", ("Student", "Professional"))

if status == "Student":
    st.write("You are a student.")
    st.write("Please enter your student ID:")
    student_id = st.text_input("Student ID")
    if student_id:
        st.success(f"Your student ID is: {student_id}")
elif status == "Professional":
    st.write("You are a professional.")
    st.write("Please enter your professional ID:")
    professional_id = st.text_input("Professional ID")
    if professional_id:
        st.success(f"Your professional ID is: {professional_id}")

if st.button("button click"): 
    st.write("You clicked the button!")    