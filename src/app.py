import streamlit as st
import pandas as pd
from data_cleaning import clean_data
from rsc_allocation import funds_allocation,funds_details
from eda import schools_in_district,school_gender_dist,features_correlation,bldg_cond_distr,gender_studying_in_schools,resource_lackness_distr,students_in_district

#**************************  Basic Info about Project *****************************

st.title("**Optimizing Education Impact: Funds Distribution Project**")

st.subheader("**OBJECTIVE :**")
st.write("""
This project aims to empower an ed-tech company to achieve **maximum impact** in improving the current education landscape.

We achieve this by:

* **Analyzing key constraints:** Identifying factors hindering educational progress.
* **Data-driven fund allocation:** Distributing resources strategically to address these constraints.

By focusing on these elements, we ensure that funds reach schools with the greatest need, fostering equitable access to quality education.
""")

Total_Fund = '3 Billion USD'
Distributed = '2.75 Billion USD'
Remaining = '250 Million USD'

# Consider using a progress bar or pie chart for visual representation

st.subheader("**FUND OVERVIEW:**")
data = {'Fund Category': ['Total Fund', 'Distributed', 'Remaining'],
        'Amount': [Total_Fund, Distributed, Remaining]}
st.dataframe(data)


note_text = "**Important Note:**"
st.subheader(note_text)

st.write("""
We've allocated **250 million USD** specifically to address potential data quality issues. 

These issues stem from:

* **Missing values (nulls)** in the dataset that required imputation techniques.
* The possibility of **imputed data** not accurately reflecting reality.

This reserved amount allows us to identify and support schools potentially affected by inaccurate data. Once addressed, the remaining funds will be distributed **equally among all 50,000 schools**.

By prioritizing data integrity and equitable distribution, we ensure that resources have the most significant impact on educational needs.
""")


#******************************************DATA CLEANING PART *******************************

with st.expander("**1. DATA CLEANING**"):
    st.write('''If you want to know how the cleaning process is done , take a look on my code by clicking above on github icon and visiting github ....
    ''')
    # loading the provided schools data
    init_df = pd.read_csv(r"C:\Users\PMLS\Desktop\Python\School_Funds_Distribution\data\Input_Schools_Data.csv")
    df=clean_data(init_df)


#******************************************EDA PART *************************************************
with st.expander("**2. EXPLORATORY DATA ANALYSIS** "):
    st.write("Here are some visuals to give you know-how about the schools data . \n")
    
    st.text("**Figure 1 :**\n")
    schools_in_district(df)

    st.write("-------------------------------------------------------------------------------")
    st.text("**Figure 2 :**\n")
    features_correlation(df)
    
    st.write("-------------------------------------------------------------------------------")
    st.text("**Figure 3 :**\n")
    students_in_district(df)

    st.write("-------------------------------------------------------------------------------")
    st.text("**Figure 4 :**\n")
    school_gender_dist(df)
 
    st.write("-------------------------------------------------------------------------------")
    st.text("**Figure 5 :**\n")
    resource_lackness_distr(df)
  
    st.write("-------------------------------------------------------------------------------")
    st.text("**Figure 6 :**\n")
    gender_studying_in_schools(df)
    
    st.write("-------------------------------------------------------------------------------")
    st.text("**Figure 7 :**\n")
    bldg_cond_distr(df)
    
    st.write("-------------------------------------------------------------------------------")



#******************************************FUNDS ALLOCATION PART ***************************************
with st.expander("**3. ALLOCATED FUNDS DATASET**",expanded=True):
    st.write("Dataset showing **< SCHOOLS_DATA >** & **< FUND_ALLOTED >** to Schools")
    df=funds_allocation(df)
    st.dataframe(df)


#******************************************FUNDS DETAIL PART *******************************************
with st.expander("**4. DETAILS OF ALLOCATED FUNDS** ",expanded=True):
    

    default_id = 12345  # Optional default value
    school_id_input = st.text_input("Enter the school id :", value=default_id)

    if school_id_input:
          # Check if user entered anything
        try:
            id = int(school_id_input)
            new=(df[df['school_id'] == id])
            st.write(new)
            funds_details(new)
        except ValueError:
            st.error("Please enter a valid numeric school ID.")
            id = None 

    else:
        st.text(f"No school with id {id} found....")    

