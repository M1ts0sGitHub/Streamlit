import streamlit as st
import numpy as np


st.title('Random Distributions')
st.text("Let's create a list with random numbers from a binomial distribution with numpy")

st.code("import numpy as np\nrl = np.random.binomial(20, 0.5, size=1015)")
rl = np.random.binomial(20, 0.5, size=1015)
with st.expander("Binomial distribution values"):
    st.text(' '.join(f'{i:02}' for i in rl))

st.text("Let's create a histogram with the random list")
st.code("table = {i: np.count_nonzero(rl == i) for i in range(21)}\nst.bar_chart([table[i] for i in range(21)], use_container_width=True)")

table = {i: np.count_nonzero(rl == i) for i in range(21)}
st.bar_chart([table[i] for i in range(21)], use_container_width=True)