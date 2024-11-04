import streamlit as st
import numpy as np
import pandas as pd


## Title of the applicaiton
st.title("Hello Streamlit ")

## Display simple text

st.write("This si a simple text")

## Simple datafram

df = pd.DataFrame({
    'First Column' : [1, 2, 3, 4],
    'Second Column' : [10, 20, 30, 40]
    })

## Display the datafram
st.write("here is the Dataframe")
st.write(df)

## Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)