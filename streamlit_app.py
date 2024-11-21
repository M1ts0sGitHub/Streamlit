import streamlit as st
from numpy import random

st.title('Random Number')
st.text("Let's create a random number with numpy")
st.code("from numpy import random\nx = random.randint(100)\nprint(f'Random number: {x}')")
x = random.randint(100)
st.text(f'Random number: {x}')

st.text("Let's create a random dictionary with numpy")
st.code("from numpy import random\nx = random.randint(100)\nprint(f'Random number: {x}')")
x = random.randint(100)
st.text(f'Random number: {x}')