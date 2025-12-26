import streamlit as st
import pandas as pd
st.title("streamlit text input")
name = st.text_input("enter your name")
age = st.slider("select your age", 0, 100, 25)
options = ['python', 'java', 'c++', 'javascript']
choice = st.selectbox("select your favorite programming language", options)
st.write(f"your favorite programming language is {choice}")
st.write(f"your age is {age}")
data = {
    'name': ['alice', 'bob', 'charlie', 'david'],
    'age': [25, 30, 35, 40],
    'city': ['new york', 'los angeles', 'chicago', 'houston']
}
df = pd.DataFrame(data)
df.to_csv('sample_data.csv', index=False)
st.write(df)
uploaded_file = st.file_uploader("upload a csv file", type=['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
if name:
    st.write(f"hello {name}!")