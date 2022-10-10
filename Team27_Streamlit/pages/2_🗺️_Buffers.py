import streamlit as st

st.set_page_config(
    page_title="Buffers",
    page_icon= "🗺️",
)

st.title("Buffers")

st.sidebar.title("Buffers")
st.sidebar.write("Buffers create trade areas by calculating a specified distance from a store to the area that surrounds it. They assume that all customers falling within the buffer's boundary will shop at the store.")

Dist_m= st.sidebar.slider("Distance multiplier:", 0,10)