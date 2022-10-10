import streamlit as st

st.set_page_config(
    page_title="Huff Model",
    page_icon= "📍",
)

st.title("Huff Model")

st.sidebar.title("Huff Model")
st.sidebar.write("The Huff Model is a form of spatial interaction model that calculates the probability any given customer will choose to shop at a store based on a combination of the store's attractiveness (commonly square footage or product offerings), the distance to that store, and the combined attractiveness of other competing stores.")

att = st.sidebar.slider("Attractiveness Exponent:", 0.0,3.0,0.1)
dist = st.sidebar.slider("Distance Decay Exponent:", 0.0,3.0,0.1)