import streamlit as st
import pandas as pd

st.title('StreamLit text input')
name=st.text_input("Enter your name: ")
age = st.slider("Select your age", 0, 100, 25)

if name:
      st.write(f"Hello, {name}")
if age:
      st.write(f"Your age, {age}")

options= ['Python', 'Java', 'C++', 'JavaScript']
choice = st.selectbox('Choose your favourite language : ', options)
st.write(f"You selected {choice}")

data = {
      "Name": ["John", "Rajat", "Shiv", "Professor"],
      "Age": [28, 73, 27, 49],
      "City": ['New York', 'Kanpur', 'Lucknow', 'London']
}

df = pd.DataFrame(data)
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
      df=pd.read_csv(uploaded_file)
      st.write(df)