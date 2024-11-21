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
#how many times has any number been rolled?
st.text(f'Number of times each number has been rolled: {np.unique(rl, return_counts=True)}')
#make a bar chart
st.bar_chart(np.unique(rl, return_counts=True)[1])
