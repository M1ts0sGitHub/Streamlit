import streamlit as st
import numpy as np

st.title('Random Number')
st.text("Let's create a random number with numpy")
st.code("from numpy import random\nx = random.randint(100)\nprint(f'Random number: {x}')")
x = np.random.randint(100)
st.text(f'Random number: {x}')

st.text("Let's create a random normal dictionary with numpy")

rl = np.random.binomial(20, 0.5, size=100)
st.text(f'Random number: {rl}')
#make a plot
st.line_chart(rl)
#make a histogram
st.bar_chart(rl)

