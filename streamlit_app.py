import streamlit as st
st.title('All kinds of Randomness')
st.text('Lets see how many random distributions exist')

with st.form(key='my_form'):
  username = st.text_input('Username')
  password = st.text_input('Password')
  st.form_submit_button('Login')

