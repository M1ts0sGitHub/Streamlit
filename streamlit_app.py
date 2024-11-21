import streamlit as st
from numpy import random

st.title('Random Number')
st.text("Let's create a random number with numpy")
st.code("from numpy import random\nx = random.randint(100)\nprint(f'Random number: {x}')")
x = random.randint(100)
st.text(f'Random number: {x}')

st.text("Let's create a random normal dictionary with numpy")

rl = random.normal(20, 0.5, size=100)
rl = round(rl, 2)
st.text(f'Random number: {rl}')  