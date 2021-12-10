import time
import pandas as pd
import streamlit as st
import numpy as np

st.write(pd.DataFrame({
  "Name":["Name1", "Age1", "GPA1", "Dept1"],
  "Age": [10,12,24,32],
  "GPA": [3.2,3.1,3.3,2.7],
  "Dept": ["CSE", "EEE", "CE", "ICE"]})
)

df = np.random.randn(10, 2)
df = pd.DataFrame(df,columns=('Col%d' % i for i in range(2)))
st.line_chart(df)


map_data = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [24.11, 89.15],
    columns=['lat', 'lon'])

st.map(map_data)


st.button('Click me')
st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a photo')