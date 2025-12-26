import streamlit as st
import pandas as pd
import numpy as np 
## title of the application
st.title("hello streamlit")
## DISPLAYING A SIMPLE TEXT
st.write("this is a simple text")
##create a dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
## displaying dataframe
st.write("this is a simple dataframe")
st.write(df)
## displaying a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)