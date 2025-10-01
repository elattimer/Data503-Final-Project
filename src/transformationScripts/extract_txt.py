import pandas as pd
from datetime import datetime
from tqdm import tqdm
import re

#----------------------------------------------------------------------------------------------------------------------#

def get_date_from_line(date_string: str)->datetime:
    ''''
    input is format 'Thursday 1 August 2019\r' as a string
    output is 2019-8-1 00:00:00 as a datetime object
    '''
    date_string = date_string.strip()
    space_position = date_string.index(" ")
    stripped_date_string = date_string[space_position+1:]
    date_object = datetime.strptime(stripped_date_string, "%d %B %Y")
    return date_object

def get_location_from_line(location_str: str)->str:
    """
    input is format 'City Academy\r' as a string
    output is 'City'
    :param location_str:
    :return location:
    """
    location = location_str.split(" ")[0]
    return location.title()

def get_name_from_line(line:str)->str:
    """
    'SELIA DIEM -  Psychometrics: 47/100, Presentation: 18/32\r'
    Get name from line and apply title case
    'Selia Diem'
    :param line:
    :return name:
    """
    names, sep, scores = line.rpartition(' - ')

    return names.strip().upper()




def get_psycho_score_from_line(line: str) -> int:
    """
    Extracts the psychometric score from a line of text like:
    "DELILA GARRET -  Psychometrics: 51/100, Presentation: 23/32"
    """

    match = re.search(r'Psychometrics:\s*(\d+)/\d+', line)

    if match:
        return int(match.group(1))
    raise ValueError(f"Could not find psychometric score in line: {line}")

def get_presentation_score_from_line(line: str) ->int:
    """
    Gets presentation score from a line of the .txt files

    :param line:
    :return presentation_score:
    """
    names, sep, scores = line.rpartition(' - ')
    linesplit = scores.split()
    presentation_score = int(linesplit[3].split("/")[0])
    return presentation_score


#----------------------------------------------------------------------------------------------------------------------#



#Iterate through sparta day files
def make_dataframe_from_txt_list(txt_file_objs:list)->pd.DataFrame:
    """
    Takes list of txt files as strings, creates a dataframe containing all the information

    :param txt_file_objs:
    :return sparta_day:
    """

    #Initiate empty dataframe
    sparta_day = pd.DataFrame({
        'date': pd.Series(dtype='datetime64[ns]'),
        'location': pd.Series(dtype='string'),
        'name': pd.Series(dtype='string'),
        'psychometric_score': pd.Series(dtype='int'),
        'presentation_score': pd.Series(dtype='int'),
        'sparta_day_id': pd.Series(dtype='int')
    })
    day_id = 0

    for day in txt_file_objs:
        day_id += 1
        # print(day)
        day_line_list = day.split("\n")

        # Remove empty lines
        day_line_list = [item for item in day_line_list if item != '']

        # Get day
        date = get_date_from_line(day_line_list[0])

        #Get location
        location = get_location_from_line(day_line_list[1])

        #Get lines with person information
        people = day_line_list[2:]
        for person in people:

            if not person.strip():  # skip empty or whitespace-only lines
                print(person)
                continue

            name = get_name_from_line(person)

            psychometric_score = get_psycho_score_from_line(person)
            presentation_score = get_presentation_score_from_line(person)

            row = pd.DataFrame({'date':[date],
                                'location':[location],
                                'name':[name],
                                'psychometric_score':[psychometric_score],
                                'presentation_score':[presentation_score],
                                'sparta_day_id':[day_id]}
                               )

            if row.notna().any().any():
                sparta_day = pd.concat([sparta_day, row], ignore_index=True)

    return sparta_day


#----------------------------------------------------------------------------------------------------------------------#

def extract_txt_to_df(container_client= None,test = False,test_data = None)->pd.DataFrame:
    """
    Gets all txt blobs from container and collates into a dataframe
    :param container_client:
    :return txt_df:
    """
    if not test:
        #Get all the txt files and blob objects.
        txt_blobs = [blob for blob in container_client.list_blobs() if blob.name.endswith(".txt")]

        txt_file_objs = []
        for blob in tqdm(txt_blobs, desc="Extracting .txts"):
            blob_client = container_client.get_blob_client(blob)
            download_stream = blob_client.download_blob()
            txt_file_objs.append(download_stream.readall().decode("utf-8"))

    if test:
        txt_file_objs = [test_data]
    txt_df = make_dataframe_from_txt_list(txt_file_objs)
    return txt_df


