from transformationScripts.extract_csv_course_behaviours import create_combined_course_behaviours
import pandas as pd

pd.set_option('future.no_silent_downcasting', True)

def transform_csv_course_behaviours_course(combined_df: pd.DataFrame) -> pd.DataFrame:
    """This accepts a dataframe created from course behaviour CSVs and transforms it into a dataframe that matches the relevant table on the ERD.

    Args:
        combined_df (pd.DataFrame): Course behaviours dataframe.

    Returns:
        pd.DataFrame: A dataframe matching the course behaviours table
    """  
    # Cleaning data
    combined_df = combined_df.fillna(0).infer_objects(copy=False)

    # Creating new dataframes
    course_df = pd.DataFrame()

    course_df['subject_name'] = combined_df['file_name'].apply(lambda x : x[:-18])
    course_df["trainer_name"] = combined_df["trainer"].apply(lambda x : x.upper())

    # Creating datetime column
    course_df['start_date'] = combined_df['file_name'].apply(lambda x : pd.to_datetime(x[-14:-4]))
    course_df["class_number"] = combined_df["file_name"].apply(lambda x : int(x[-17:-15]))

    # Remove duplicate entries
    course_df.drop_duplicates(inplace=True)
    course_df.reset_index(drop=True, inplace=True)

    # Creating the course_id column based on the length of the dataframe
    course_df['course_id'] = range(1, len(course_df) + 1)
    course_df = course_df[['course_id', 'subject_name', 'trainer_name', 'start_date', 'class_number']]

    return course_df


def transform_csv_course_behaviours_behaviour_scores(combined_df: pd.DataFrame) -> pd.DataFrame:
    """This accepts a dataframe created from course behaviour CSVs and transforms it into a dataframe that matches the relevant table on the ERD.

    Args:
        combined_df (pd.DataFrame): Behaviour scores dataframe.

    Returns:
        pd.DataFrame: A dataframe matching the behaviour scores table (minus person_id that will be mapped later)
    """    
    # Creating the behaviour_scores dataframe

    course_id_map_dict = {
    'Data_28_2019-02-18.csv': 1,
    'Data_29_2019-03-04.csv': 2,
    'Data_30_2019-04-08.csv': 3,
    'Data_31_2019-05-20.csv': 4,
    'Data_32_2019-07-22.csv': 5,
    'Data_33_2019-08-05.csv': 6,
    'Data_34_2019-08-19.csv': 7,
    'Data_35_2019-09-23.csv': 8,
    'Data_36_2019-10-28.csv': 9,
    'Data_37_2019-11-18.csv': 10,
    'Data_38_2019-12-16.csv': 11,
    'Data_39_2019-12-30.csv': 12,
    'Engineering_17_2019-02-18.csv': 13,
    'Engineering_18_2019-04-01.csv': 14,
    'Engineering_19_2019-04-29.csv': 15,
    'Engineering_20_2019-05-27.csv': 16,
    'Engineering_21_2019-07-15.csv': 17,
    'Engineering_22_2019-07-22.csv': 18,
    'Engineering_23_2019-08-12.csv': 19,
    'Engineering_24_2019-09-16.csv': 20,
    'Engineering_25_2019-09-23.csv': 21,
    'Engineering_26_2019-10-28.csv': 22,
    'Engineering_27_2019-11-25.csv': 23,
    'Engineering_28_2019-12-16.csv': 24,
    'Engineering_29_2019-12-30.csv': 25,
    'Business_20_2019-02-11.csv': 26,
    'Business_21_2019-03-18.csv': 27,
    'Business_22_2019-04-15.csv': 28,
    'Business_23_2019-05-20.csv': 29,
    'Business_24_2019-07-15.csv': 30,
    'Business_25_2019-07-29.csv': 31,
    'Business_26_2019-08-12.csv': 32,
    'Business_27_2019-09-16.csv': 33,
    'Business_28_2019-10-21.csv': 34,
    'Business_29_2019-11-18.csv': 35,
    'Business_30_2019-12-30.csv': 36}

    combined_df['start_date'] = combined_df['file_name'].apply(lambda x : pd.to_datetime(x[-14:-4]))
    combined_df['course_id'] = combined_df['file_name'].map(course_id_map_dict)
    combined_df = combined_df.fillna(0).infer_objects(copy=False)
    combined_df.drop('file_name', axis=1, inplace=True)


    # Created a dataframe which keeps the name, trainer, course_id and start_date the same as the original dataframe.
    # Each combination of trait and week (e.g., "Analytic_W1") becomes a row under the new 'trait_week' column.
    # The score for that 'trait_week' is placed in the next column.
    df_melted = combined_df.melt(
    id_vars=['name', 'trainer', 'course_id', 'start_date'],
    var_name='trait_week',
    value_name='score')

    df_melted[['trait', 'week']] = df_melted['trait_week'].str.extract(r'(\w+)_W(\d+)')
    df_melted['week'] = df_melted['week'].astype(int)

    # Changes df_melted back into wide form. Creating a column for each trait and assigning its score.  
    df_traits = df_melted.pivot_table(
    index=['course_id', 'name', 'week', 'start_date'],
    columns='trait',
    values='score').reset_index()

    df_traits = df_traits.astype({'Analytic': 'int', 
                      'Determined': 'int', 
                      'Imaginative': 'int', 
                      'Independent': 'int', 
                      'Professional': 'int',
                      'Studious': 'int'})
    
    df_traits.rename(columns={'Analytic': 'analytical', 
                      'Determined': 'determination', 
                      'Imaginative': 'imaginative', 
                      'Independent': 'independence', 
                      'Professional': 'professionalism',
                      'Studious': 'studious'}, inplace=True)
    
    df_traits["name"] = df_traits["name"].apply(lambda x : x.upper())

    return df_traits
