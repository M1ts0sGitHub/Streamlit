import streamlit as st
from numpy import random
st.title('All kinds of Randomness')
st.text('Lets see how many random distributions exist')



st.text('Generate Random Number')
st.code('from numpy import random\n \nx = random.randint(100)\n\nprint(x)')
x = random.randint(100)
st.text(f'Random number: {x}')
