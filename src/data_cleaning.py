import pandas as pd
import numpy as np

def clean_data(init_df):
    # dropped these columns b/c of lots of null values and low significance
    init_df.drop(['drink_water_type_other', 'upgrade_primary_year', 'upgrade_middle_year', 'upgrade_high_year', 'upgrade_high_sec_year'], axis=1, inplace=True)

    # selected these features due to high significance
    features = ['school_id', 'district', 'tehsil', 'est_year', 'school_gender', 'gender_studying', 'bldg_condition', 'classes', 'functional_classrooms', 'enrollment', 'Teachers', 'NonTeachers', 'electricity', 'drink_water', 'toilets', 'teachers_toilets']
    df = init_df[features].copy()

    # filled values with various methods
    df['bldg_condition'].fillna('Medium Condition', inplace=True)
    df['teachers_toilets'].fillna(0, inplace=True)
    df['enrollment'].fillna(df['enrollment'].mean(), inplace=True)

    df.sort_values(by='district', ascending=True, inplace=True)

    df['Teachers'].interpolate('nearest', inplace=True)
    df['NonTeachers'].interpolate('nearest', inplace=True)

    df['Teachers'].fillna(df['Teachers'].mean(), inplace=True)
    df['NonTeachers'].fillna(0, inplace=True)

    resources = ['electricity', 'drink_water', 'toilets', 'teachers_toilets']

    def count_missing_resources(row):
        # Count the number of zeros (missing resources) in the resource columns
        return sum(row[resources] == 0)

    # Apply the function to each row and add a new 'lack_resource' column
    df['lack_resource'] = df.apply(count_missing_resources, axis=1)

    # determining functional classes ratio of each school
    df["fnl_class_ratio"] = df['functional_classrooms'] / df['classes']

    df['bldg_status_code'] = df['bldg_condition'].replace(['Satisfying', 'Needed Minor Repairing', 'Medium Condition', 'Partial Building is Dangerous', 'Complete Building Needs Repairing', 'Building Is Dangerous'], [1, 1.5, 2, 2.5, 4, 5])

    df['fnl_class_ratio'].replace(np.inf, 0.0, inplace=True)
    df['fnl_class_ratio'].fillna(0, inplace=True)
    df['building_age']=2024-df['est_year']
    

    return df