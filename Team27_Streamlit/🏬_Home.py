import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Trade Area Analysis App",
    page_icon= "🏬",
)

st.sidebar.header("Trade Area Analysis")
st.sidebar.write("Trade area analysis is an important practice that can forecast whether a business will succeed or fail in a given\
     geographical area. It gives you insight into who your potential customers are, what they likely want, and where they typically come\
         from (and when). Plus, it helps you identify who your possible competitors are and how (or if) they will impact your store’s \
            performance.")

st.sidebar.header("Cape Town Overview")
st.sidebar.write("Cape Town has the second largest municipal economy in South Africa and is the second most important contributor to\
     national employment, contributing 9,5% (EGS – Baseline Statistics 2019). It’s not surprising, as the Mother City really does offer all of the top qualities required for sustainable economic growth. From a world-class Central Business District (CBD) to established infrastructure across several sectors throughout the Western Cape, it truly is a bustling node of commerce and industry.")

st.header("Cape Town Trade Area Analysis")

tab1,tab2,tab3 = st.tabs(['Project Overview', 'Business Value', 'The Process'])

with tab1:
    st.subheader("Project Overview")
    st.write("Trade Area Analysis explores the viability of setting up a retail outlet in a location of interest. For this project,\
         the location of interest is Cape Town.")
    st.write("The project offers insight on the viability of opening a retail outlet in different locations within Cape Town.")

    image = Image.open('/home/explore-student/t27-s3bucket/Data/capetown_.png')
    st.image(image, caption='An Aerial View of Cape Town Business District', width=None)

with tab2:
    st.subheader("Business Value")
    st.write("1. The trade area analysis will provide the retailer a picture about demographic and socio-cultural aspects of consumers.\
         For a new store, the analysis is necessary in understanding the prevailing opportunities and threats (if any).")
    st.write("2. The analysis will help in locating better site location by understanding the existing trade areas around the\
        potential locations.")
    st.write("3. Trade area analysis will assess in advance the effects of trade area overlapping.")

    image2 = Image.open('/home/explore-student/t27-s3bucket/Data/cape.png')
    st.image(image2, caption='Distribution of Potential Competitors in Cape Town', width=None)

with tab3:
    st.subheader("The Roadmap")

    image3 = Image.open('/home/explore-student/t27-s3bucket/Data/27_roadmap.png')
    st.image(image3, caption='The project roadmap', width=None)
