import streamlit as st


st.set_page_config(
    page_title="Trade Area Analysis App",
    page_icon= "🏬",
)

st.sidebar.header("Trade Area Analysis")
st.sidebar.write("Trade area analysis is an important practice that can forecast whether a business will succeed or fail in a given geographical area. It gives you insight into who your potential customers are, what they likely want, and where they typically come from (and when). Plus, it helps you identify who your possible competitors are and how (or if) they will impact your store’s performance.")

st.header("Cape Town Trade Area Analysis")
st.subheader("1. Project Overview")
st.write("Malapo Store wants to explore the viability of setting up a retail outlet in Cape Town")
st.write("Trade Area Analysis tool offers insight to Molapo store on the viability of opening a retail outlet in different locations within Cape Town")

from PIL import Image
image = Image.open('capetown_pop.png')

st.image(image, caption='Distribution of Wards in Cape Town', width=None)

st.subheader("2. Business Value")
st.write("1. The trade area analysis will provide the retailer a picture about demographic and socio-cultural aspects of consumers. For a new store, the analysis is necessary in understanding the prevailing opportunities and threats (if any).")
st.write("2. The analysis will help in locating better site location by understanding the existing trade areas around the potential locations.")
st.write("3. Trade area analysis will assess, in advance the effects of trade area overlapping.")

image2 = Image.open('cape.png')

st.image(image2, caption='Distribution of Potential Competitors in Cape Town', width=None)

st.subheader("3. The Process")