import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

# Plot 0
def features_correlation(df):
    # Select only the numerical columns
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    # Calculate the correlation matrix for the numerical columns
    corr = df[num_cols].corr()
    
    # Create the heatmap
    plt.figure(figsize=(12, 10))
    ax = sns.heatmap(corr, cmap='coolwarm')
    
    # Adjust the font size of annotations
    ax.tick_params(axis='both', which='major', labelsize=8)
    
    plt.title('Correlation Matrix of Numerical Features')
    
    st.pyplot(plt)
    st.write("This heatmap visualizes the correlation between numerical features in the DataFrame. Higher values indicate stronger relationships between features.")

# Plot 1
def schools_in_district(df):
    district_counts = df.groupby('district')['school_id'].count()
    plt.figure(figsize=(15,7))
    # Extract district names and counts for plotting
    districts = district_counts.index.to_numpy()  # Get district names as NumPy array
    counts = district_counts.to_numpy()  # Get counts as NumPy array
    
    # Create the bar chart
    plt.bar(districts, counts)
    for i, v in enumerate(counts):
        y_val = v + 0.1  # Add a small offset for better visibility
        plt.text(districts[i], v+0.1, int(v), ha='center', va='bottom', fontsize=9) 
    
    # Add labels and title
    plt.xlabel('District')
    plt.ylabel('Number of Schools')
    plt.xticks(rotation=75)
    plt.title('Number of Schools by District')
    
    # Display the plot
    st.pyplot(plt)
    st.write("This bar chart shows the distribution of schools across different districts.")
    

# Plot 2
def school_gender_dist(df):
    fig, ax = plt.subplots()  # Create a single figure with an Axes object
    plt.pie(df.groupby("school_gender")["enrollment"].sum(), autopct='%1.1f%%', colors=["blue", "orange"])  # Plot data on the Axes
    
    # Add title and legend within the Axes object
    ax.set_title('Schools Distribution Based on Genders')
    ax.legend(labels=['Female', 'Male'])
    
    # Display the plot 
    st.pyplot(fig)
    st.write("This pie chart depicts the distribution of schools categorized by the genders they cater to (female, male).")
    

# Plot 3
def students_in_district(df):
    district_counts = df.groupby('district')['enrollment'].sum()
    plt.figure(figsize=(17,7))
    # Extract district names and counts for plotting
    districts = district_counts.index.to_numpy()  # Get district names as NumPy array
    counts = district_counts.to_numpy()  # Get counts as NumPy array
    
    # Create the bar chart
    plt.bar(districts, counts)
    for i, v in enumerate(counts):
        y_val = v + 0.1  # Add a small offset for better visibility
        plt.text(districts[i], v+0.1, int(v), ha='center', va='bottom', fontsize=6.5) 
    
    # Add labels and title
    plt.xlabel('District')
    plt.ylabel('Number of Enrollments')
    plt.xticks(rotation=75)
    plt.title('Number of Enrollments by District')
    
    st.pyplot(plt)
    st.write("This bar chart shows the total student enrollment in each district.")
  

# Plot 4
def bldg_cond_distr(df):
    bldg_cond = df["bldg_condition"].value_counts()
    condition=bldg_cond.index.to_numpy()
    plt.figure(figsize=(15,7))
    
    counts = bldg_cond.to_numpy()  # Get counts as NumPy array
    
    # # Create the bar chart
    plt.barh(condition, counts)
    for i, count in enumerate(counts):
        plt.annotate(str(count), xy=(count, condition[i]), ha='left', va='center')

    # Add labels and title
    plt.xlabel('No of Buidings')
    plt.ylabel('Buildings Condition')
    plt.title('Distribution of Buildings  Conditions')
    plt.grid()
     
    st.pyplot(plt)
    st.write("This bar chart shows the condition of schools (either satisfying,dangerous etc).")

# Plot 5
def gender_studying_in_schools(df):
    gender_studying = df['gender_studying'].value_counts()
    plt.figure(figsize=(8, 6))
    gender_studying.plot(kind='bar')
    
    # Add count values on top of the bars
    for i, count in enumerate(gender_studying):
        plt.text(i, count, str(count), ha='center', va='bottom')
    
    plt.title("Distribution of Gender Specific Schools")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    
    st.pyplot(plt)
    st.write("This bar chart shows the gender studying in schools apart from school gender (Male ,Female or Both).")
    

# Plot 6
def resource_lackness_distr(df):
    bldg_cond = df["lack_resource"].value_counts()
    condition=bldg_cond.index.to_numpy()
    plt.figure(figsize=(15,7))
    
    counts = bldg_cond.to_numpy()  # Get counts as NumPy array
    
    # # Create the bar chart
    plt.bar(condition, counts)
    for i, v in enumerate(counts):  # Loop through bars and counts
      plt.text(i, v + 0.1, str(v), ha='center', va='bottom', fontsize=12)
    # Add labels and title
    plt.xlabel('No of Resources')
    plt.ylabel('Count of Lackness')
    plt.xticks(rotation=75)
    plt.title('Distribution of Resource Lackness')
    plt.grid()
    
    st.pyplot(plt)
    st.write("This bar chart illustrates the number of specific resources schools are lacking (either 1,2,3 or 4 ) .")


