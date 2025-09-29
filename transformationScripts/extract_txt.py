from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import pandas as pd
from datetime import datetime

subscription_id = "cd36dfff-6e85-4164-b64e-b4078a773259"
resource_group = "data503"
location = "uksouth"
storage_account_name = "data503paulastorage"
account_url = f"https://{storage_account_name}.blob.core.windows.net"

#Loaction of txt files
container_name = "talent"

#az login in bash
credential = DefaultAzureCredential()

#Create instance of blob service client class for the specific account and user credentials
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

# Get the client for the container from blob_service_client
container_client = blob_service_client.get_container_client(container_name)

#----------------------------------------------------------------------------------------------------------------------#

#Get all the txt files and blob objects.
txt_blobs = [blob for blob in container_client.list_blobs() if blob.name.endswith(".txt")]

txt_file_objs = []
for blob in txt_blobs:
    blob_client = container_client.get_blob_client(blob)
    download_stream = blob_client.download_blob()
    txt_file_objs.append(download_stream.readall().decode("utf-8"))

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
    return names.title()


def get_psycho_score_from_line(line:str)->int:
    """
    Gets psychometrics score from a line of the .txt files

    :param line:
    :return psycho_score:
    """
    names, sep, scores = line.rpartition(' - ')
    linesplit = scores.split()
    psycho_score = int(linesplit[1].split("/")[0])
    return psycho_score

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
    sparta_day = pd.DataFrame(columns=['date',
                                       'location',
                                       'name',
                                       'psychometric_score',
                                       'presentation_score'])

    for day in txt_file_objs:
        # print(day)
        day_line_list = day.split("\n")

        # Remove empty lines
        day_line_list = [item for item in day_line_list if item != '']

        # Get day
        date = get_date_from_line(day_line_list[0])

        #Get location
        location = get_location_from_line(day_line_list[1])

        #Get lines with person information
        people = day_line_list[3:]
        for person in people:
            name = get_name_from_line(person)

            psychometric_score = get_psycho_score_from_line(person)
            presentation_score = get_presentation_score_from_line(person)

            row = pd.DataFrame({'date':[date],
                   'location':[location],
                   'name':[name],
                   'psychometric_score':[psychometric_score],
                   'presentation_score':[presentation_score]})

            if row.notna().any().any():
                sparta_day = pd.concat([sparta_day, row], ignore_index=True)

        return sparta_day

print(make_dataframe_from_txt_list(txt_file_objs=txt_file_objs))