import streamlit as st
#funds for both gender studying in one school 
def both_gender_fund(row):
    if row['gender_studying']=='Both':
        return 6098
    else :
        return 0
    
# funds for building condition       
def calculate_bldg_fund(row):
    if row['bldg_status_code'] == 1.0:
        return 8500
    elif row['bldg_status_code'] == 1.5:
        return 15000     
    elif row['bldg_status_code'] == 2.0:
        return 25000
    elif row['bldg_status_code'] == 2.5:
        return 50237.9
    elif row['bldg_status_code'] == 4.0:
        return 75420
    elif row['bldg_status_code'] == 5.0:
        return 150000
    
# function to allocate resource fund 
def resources_fund(row):
    if row['lack_resource']==0:
        return 0
    elif row['lack_resource']==1:
        return 11957
    elif row['lack_resource']==2:
        return 2*11957
    elif row['lack_resource']==3:
        return 3*11957    
    elif row['lack_resource']==4:
        return 4*11957    
 
# funds to improve classes   
def classes_fund(row):
    if (row['fnl_class_ratio']<=10.2) & (row['fnl_class_ratio']>=0.75):
        return 3069.9
    elif (row['fnl_class_ratio']<0.75) & (row['fnl_class_ratio']>=0.50):
        return 2*3069.9
    elif (row['fnl_class_ratio']<0.50) & (row['fnl_class_ratio']>=0.25):
        return 3*3069.9
    elif (row['fnl_class_ratio']<0.25) & (row['fnl_class_ratio']>=0.0):
        return 4*3069.9    

# funds for old buildings 
def old_bldg_fund(row):
    if row['building_age']>=50:
        return 4274
    elif row['building_age']<50:
        return 0
    
#************************************* MAIN FUNCTIONS **********************************************************
@st.cache_data
def funds_allocation(df):
    formula =  (df.apply(old_bldg_fund, axis=1)) +20750 + (df['enrollment']*16.7) + (df['Teachers']*204.1)+(df['NonTeachers']*196)+(df.apply(calculate_bldg_fund, axis=1))+(df.apply(both_gender_fund, axis=1))+(df.apply(resources_fund, axis=1))+(df.apply(classes_fund, axis=1))
    df['fund($)']=formula    
    return df

@st.cache_data
def funds_details(new):
    base_fund=20750
    enrollment_alloc=int(new['enrollment'].iloc[0])*16.7
    teacher_alloc=int(new['Teachers'].iloc[0])*204.1
    non_teacher_alloc=int(new['NonTeachers'].iloc[0])*196
    bldg_age_alloc=float(new.apply(old_bldg_fund, axis=1).iloc[0])
    bldg_alloc=float(new.apply(calculate_bldg_fund, axis=1).iloc[0])
    classes_alloc=float(new.apply(classes_fund, axis=1).iloc[0])
    resources_alloc=float(new.apply(resources_fund, axis=1).iloc[0])
    dual_gender=float(new.apply(both_gender_fund, axis=1).iloc[0])
    class_fnl_alloc =float(new.apply(classes_fund, axis=1).iloc[0])

    st.write("Here are the details of fund alloted :")
        
    col1, col2, col3 = st.columns(3)  # Create three columns
    
    col1.write(f"Base Fund :{base_fund}")
    col2.write(f"Enrollment Fund :{enrollment_alloc}")
    col3.write(f"Teacher Fund Portion :{teacher_alloc}")
    
    col1, col2, col3 = st.columns(3)  
    col1.write(f"Non Teachers Fund Portion :{non_teacher_alloc}")
    col2.write(f"Resources Lackness Fund : {resources_alloc}")
    col3.write(f"Dual Gender School Fund :{dual_gender}")
    col1, col2,col3 = st.columns(3)  
    col2.write(f"Building Old Age Fund(>50) :{bldg_age_alloc}")
    col1.write(f"Building Renovation Fund :{bldg_alloc}") 
    col3.write(f"Class Resources Fund :{class_fnl_alloc}")

    total= base_fund + enrollment_alloc + teacher_alloc + non_teacher_alloc + bldg_age_alloc + bldg_alloc + classes_alloc + resources_alloc + dual_gender
    # return total
    st.write("Total Fund :",total)