import streamlit as st
import pandas as pd
import numpy as np

# https://docs.streamlit.io/get-started/fundamentals/main-concepts

st.write("DataFrame Example:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
st.divider()
st.write("Numpy Random DataFrame w. Highlight Example:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('header %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0)) #column-wise max
st.dataframe(dataframe.style.highlight_max(axis=1)) #row-wise max

st.divider()
import time
st.write("Progress Bar Example:")
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
