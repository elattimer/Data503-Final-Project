from extract_csv_course_behaviours import create_combined_course_behaviours
from src.extract import container_academy
import pandas as pd
from datetime import datetime

combined_df = create_combined_course_behaviours(container_academy)

def transform_csv_course_behaviours(combined_df: pd.DataFrame) -> pd.DataFrame:
    # Cleaning data
    combined_df.fillna(0, inplace=True)

    # Creating new dataframes
    course_df = pd.DataFrame()

    course_df['subject_name'] = combined_df['file_name'].apply(lambda x : x[:-18])
    course_df["trainer_name"] = combined_df["trainer"].apply(lambda x : x.upper())

    # Creating datetime column
    course_df['start_date'] = combined_df['file_name'].apply(lambda x : pd.to_datetime(x[-14:-4]))

    course_df["class_number"] = combined_df["file_name"].apply(lambda x : int(x[-17:-15]))
    course_df.drop_duplicates(inplace=True)
    course_df.reset_index(drop=True, inplace=True)
    course_df['course_id'] = range(1, len(course_df) + 1)
    course_df = course_df[['course_id', 'subject_name', 'trainer_name', 'start_date', 'class_number']]
    return course_df

transform_csv_course_behaviours(combined_df)


def create_behaviour_dataframe(combined_df: pd.DataFrame) -> pd.DataFrame:
    # Creating the behaviour_scores dataframe
    course_df = transform_csv_course_behaviours(combined_df)
    combined_df.fillna(0, inplace=True)
    combined_df.drop('file_name', axis=1, inplace=True)

    '''
    Created a dataframe which keeps the name and trainer the same as the original dataframe.
    Each combination of trait and week (e.g., "Analytic_W1") becomes a row under the new 'trait_week' column.
    The score for that 'trait_week' is placed in the next column.
    '''
    df_melted = combined_df.melt(
    id_vars=['name', 'trainer'],
    var_name='trait_week',
    value_name='score')

    df_melted[['trait', 'week']] = df_melted['trait_week'].str.extract(r'(\w+)_W(\d+)')
    df_melted['week'] = df_melted['week'].astype(int)

    '''
    Changes df_melted back into wide form. Creating a column for each trait and assigning its score.  
    '''
    df_traits = df_melted.pivot_table(
    index=['name', 'week'],
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

    

    print(df_traits)
    

create_behaviour_dataframe(combined_df)