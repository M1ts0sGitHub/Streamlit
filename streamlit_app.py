import streamlit as st
import numpy as np

st.title('Random Number')
st.text("Let's create a random number with numpy")
st.code("from numpy import random\nx = random.randint(999)\nprint(f'Random number: {x}')")
x = np.random.randint(999)
st.text(f'Random number: {x}')

st.text("Let's create a random normal dictionary with numpy")

rl = np.random.binomial(20, 0.5, size=999)
st.text(' '.join(f'{i:02}' for i in rl))
st.text("Let's create a table and a histogram with the random list")
table = dict()
for i in range(21):
    table[i] = np.count_nonzero(rl == i)

st.table(table)
st.bar_chart([table[i] for i in range(21)])
