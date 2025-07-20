import streamlit as st
import pandas as pd
import numpy as np


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
st.write("Numpy")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
st.divider()
st.write("Numpy DataFrame")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('header %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0)) #column-wise max

st.dataframe(dataframe.style.highlight_max(axis=1)) #row-wise max
st.table(dataframe)

