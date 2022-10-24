import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Data",
    page_icon= "📊",
)

st.header("Interact with the Datasets and the Visuals 📊")

st.sidebar.header("Data and EDA")
st.sidebar.write("The data used for the Trade Area Analysis is derived from South African 2011 census. The data constitutes of two dataframes. The first dataframe has the population data, while the second dataframe has the household data ")
st.sidebar.header("Data Insights")
st.sidebar.write("The census data used for determining the viable trade area for Molapo Stores include the population distribution per ward and the average household income per ward")

#Importing the dataframes
pop= pd.read_csv("/home/explore-student/s3-drive/Data/capetown_population.csv")
hhs= pd.read_csv("/home/explore-student/s3-drive/Data/capetown_households.csv")

st.subheader("1. The Datasets")

tab1, tab2 = st.tabs(["Population Data", "Households Data"])

with tab1:
    container1= st.container()
    container1.write("This is Population Data for Wards in Cape Town from 2011 Census")
    container1.dataframe(pop)

with tab2:
    container2= st.container()
    container2.write("This is Households Data for wards in Cape Town fron 2011 Census")
    container2.dataframe(hhs)

st.write("")

ward_option= pop['Ward'].unique().tolist()
ward= st.selectbox("Select a Ward to review", ward_option,0)

st.write("")

st.subheader("2. The Visuals")

tab3, tab4, tab5, tab6, tab7 = st.tabs(["Pop Distribution", "Tenure Status", "Household Size", "Average HH Income", "Employment Staus"])

    
with tab3:
    container=st.container()
    container.write("Population Distribution Per Ward")
    data = pop.Pop
    labels = pop.Ward
    fig = plt.figure(figsize=(100,30))
    plt.xticks(range(len(data)), labels)
    plt.xlabel('Ward_ID')
    plt.ylabel('Population Size')
    plt.title('Population Size Per Ward')
    plt.bar(range(len(data)), data)
    st.pyplot(fig)

with tab4:
    hhs=hhs[hhs["Ward"]== ward]
    container=st.container()
    container.write(f"Tenure Status in Ward {ward}")
    data = hhs[['Rented','Owned_but_','Occupied_r','Owned_and_','Other1']].sum()
    my_labels = "Rented","Owned but not paid off","Occupied Rent Free","Owned and fully paid","Other"
    fig4= plt.figure()
    plt.pie(data,labels=my_labels,autopct='%1.1f%%')
    #plt.title('Tenure Status')
    plt.axis('equal')
    st.pyplot(fig4)

with tab5:
    container=st.container()
    container.write(f"Households Size distribution in Ward {ward}")
    data2 = hhs[['HH_Size_1','HH_Size_2','HH_Size_3','HH_Size_4','HH_Size_5','HH_Size_6','HH_Size_7','HH_Size_8','HH_Size_9','HH_Size_10']].sum()
    my_labels2 = 'HH_Size_1','HH_Size_2','HH_Size_3','HH_Size_4','HH_Size_5','HH_Size_6','HH_Size_7','HH_Size_8','HH_Size_9','HH_Size_10'
    y_pos = np.arange(len(my_labels2))
    fig5= plt.figure(figsize=(20,10))
    plt.bar(y_pos, data2, align='center', alpha=0.5)
    plt.xticks(y_pos, my_labels2)
    plt.ylabel('Number of Households')
    plt.title('Household size')
    st.pyplot(fig5)
with tab6:
    container=st.container()
    container.write(f"Average household income in Ward {ward}")
    data3 = hhs[['AHHI_No_in','AHHI_R_1__','AHHI_R_480','AHHI_R_960','AHHI_R_19_','AHHI_R_38_','AHHI_R_76_','AHHI_R_153','AHHI_R_307','AHHI_R_614','AHHI_R_1_2','AHHI_R_2_4','AHHI_Unspe']].sum()
    my_labels3 = 'No income','R1-R4,800','R4,801-R9,600','R9,601-R19,600','R19,601-R38,200','R38,201-R76,400','R76,401-R153,800','R153,801-R307,600','R307,601-R614,400','R614,401-1,228,800','R1,228,801-R2,457,600','R2,457,601+','Unspecified'
    y_pos1 = np.arange(len(my_labels3))
    fig6= plt.figure(figsize=(30,10))
    plt.bar(y_pos1, data3, align='center', alpha=0.5)
    plt.xticks(y_pos1, my_labels3)
    plt.ylabel('Number of Households')
    plt.title('Average Household Income')
    st.pyplot(fig6)
with tab7:
    container=st.container()
    container.write(f"Employment Status in Ward {ward}")
    data4 = pop[['Employed','Unemployed','Discourage','Other_NotE']].sum()
    my_labels4 = "Employed", "Unemployed", "Discouraged Work Seeker", "Not Economically Active"
    fig7= plt.figure()
    plt.pie(data4,labels=my_labels4,autopct='%1.1f%%')
    #plt.title('Employment Status')
    plt.axis('equal')
    st.pyplot(fig7)

