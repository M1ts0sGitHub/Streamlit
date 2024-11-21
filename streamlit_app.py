import streamlit as st
st.caption('Balloons. Hundreds of them...')
st.title('All kinds of Randomness')
st.text('Lets see how many random distributions exist')

st.text('Lets see how many random distributions exist')
# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
st.camera_input("一二三,茄子!")
