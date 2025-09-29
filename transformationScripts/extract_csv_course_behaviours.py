
from io import StringIO
import pandas as pd
from tqdm import tqdm

def extract_csv_course_behaviours(container_client,prefix: str):
    """ A function to acccess Azure blob storage and create dataframes from the different files based on a given file name prefix.

    Args:
        prefix (str): The name of the desired course information.

    Returns:
        DataFrame: Returns a dataframe with the combined information from all of the files with the set prefix.
    """
    new_df = pd.DataFrame(columns=['name', 'trainer', 'Analytic_W1', 'Independent_W1', 'Determined_W1',
        'Professional_W1', 'Studious_W1', 'Imaginative_W1', 'Analytic_W2',
        'Independent_W2', 'Determined_W2', 'Professional_W2', 'Studious_W2',
        'Imaginative_W2', 'Analytic_W3', 'Independent_W3', 'Determined_W3',
        'Professional_W3', 'Studious_W3', 'Imaginative_W3', 'Analytic_W4',
        'Independent_W4', 'Determined_W4', 'Professional_W4', 'Studious_W4',
        'Imaginative_W4', 'Analytic_W5', 'Independent_W5', 'Determined_W5',
        'Professional_W5', 'Studious_W5', 'Imaginative_W5', 'Analytic_W6',
        'Independent_W6', 'Determined_W6', 'Professional_W6', 'Studious_W6',
        'Imaginative_W6', 'Analytic_W7', 'Independent_W7', 'Determined_W7',
        'Professional_W7', 'Studious_W7', 'Imaginative_W7', 'Analytic_W8',
        'Independent_W8', 'Determined_W8', 'Professional_W8', 'Studious_W8',
        'Imaginative_W8', 'Analytic_W9', 'Independent_W9', 'Determined_W9',
        'Professional_W9', 'Studious_W9', 'Imaginative_W9', 'Analytic_W10',
        'Independent_W10', 'Determined_W10', 'Professional_W10', 'Studious_W10',
        'Imaginative_W10', 'file_name'])

    for blob in tqdm(container_client.list_blobs(name_starts_with=f'{prefix.title()}'), desc=f"Extracting {prefix.capitalize()} course behaviours .csvs"):

        blob_client = container_client.get_blob_client(blob)

        # Download into memory
        data = blob_client.download_blob().readall()
        text = data.decode("utf-8")  # if it's a text file

        extracted_data = pd.read_csv(StringIO(text))
        extracted_data['file_name'] = blob.name
        new_df = pd.concat([new_df, pd.DataFrame(extracted_data)], ignore_index=True)
    return new_df

def create_combined_course_behaviours(container_client):
    """A function to create dataframes for the three different course types and combine them into one large dataframe.

    Returns:
        DataFrame: Returns a combined dataframe of all three course types.
    """    
    data_df = extract_csv_course_behaviours(container_client,'data')
    engineering_df = extract_csv_course_behaviours(container_client,'engineering')
    business_df = extract_csv_course_behaviours(container_client,'business')

    course_behaviours_df = pd.concat([data_df, engineering_df, business_df], ignore_index=True)

    return course_behaviours_df