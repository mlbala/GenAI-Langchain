import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name : ")

if name:
    st.write(f"Hello, {name}")

## create a slider
age = st.slider("Select your age: ", 0, 100, 25)

st.write(f"Your age is {age}.")

options = ["Python", "Java", "C++","Java Scripts"]
choice = st.selectbox("Choose your favorite language : ", options)
st.write(f"you selected {choice}")


data = {
    "Name" : ["John","Rice","Son","Haaland"],
    "Age" : [22, 28, 29, 25],
    "City" : ["London", "New York", "California","Manchester"]
}
df = pd.DataFrame(data)
st.write(df)

## File upload

uploaded_file = st.file_uploader("choose a CSV file", type="csv")

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)
    st.write(df1)
