Project Title: **Funds Distribution Project - Optimizing Education Impact**

**Demo:**

A live demo of the app is available at https://schoolfundsdistribution.streamlit.app/.

**Description :**

This project empowers an ed-tech company to achieve maximum impact in improving the current education landscape by:

1. Identifying key constraints: Analyzing factors hindering educational progress.
2. Data-driven fund allocation: Strategically distributing resources to address these constraints.

By focusing on these elements, we ensure that funds reach to **50000** schools with the greatest need, fostering equitable access to quality education.

**Key Technologies:**

1.Python (programming language)
2.Streamlit (web framework)
3.Pandas (data manipulation library)
4.Matplotlib , Seaborn for visualizations
5.Numpy and Scipy for numeric and scientific calculations

**Dataset used :**

Used **Input_Schools_Data.csv** in funds allocation process 
Allocated funds to schools in the **Output_Schools_Data.csv**

**Project Structure:**

1.data: Contains raw and cleaned school data 

2.src: Contains Python scripts for:
    data_cleaning.py: Data cleaning functions to prepare the dataset.
    rsc_allocation.py: Functions for fund allocation calculations and details.
    eda.py: Functions for exploratory data analysis visualizations.
    app.py: The main Streamlit app script.

3.notebook : Jupyter notebook of whole process

4.requirements.txt: Lists dependencies required to run the project.

**Installation:**

Clone this repository: git clone https://github.com/mhuzaifa5/School_Funds_Distribution.git

Install dependencies: pip install -r requirements.txt 

**Running the App:**

Navigate to the project directory: cd School_funds_distribution
Run the Streamlit app: streamlit run app.py

**Future Improvements:**
The app is a little slow due to dense calculation in each iteration . So the main task is to make it as fast as possible.

