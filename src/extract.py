import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from warnings import filterwarnings
from transformationScripts.extract_txt import *
from transformationScripts.extract_csv_applicants import *
from transformationScripts.extract_csv_course_behaviours import *
from transformationScripts.extract_json import *
from passwords.passwords import get_az_password

subscription_id = get_az_password()
resource_group = "data503"
location = "uksouth"
storage_account_name = "data503paulastorage"
account_url = f"https://{storage_account_name}.blob.core.windows.net"

# az login in bash
credential = DefaultAzureCredential()

# Create instance of blob service client class for the specific account and user credentials
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

# Get the client for the container from blob_service_client
container_talent = blob_service_client.get_container_client("talent")
container_academy = blob_service_client.get_container_client("academy")

filterwarnings("ignore", category=FutureWarning)


def extract()->dict:
    """
    Runs all the extract functions for each file type in the remote storage.
    Requires the container clients, container_talent and container_academy, to be defined.

    Each extract returns a DataFrame which is stored in a dictionary.

    :return Dictionary of DataFrames:
    """
    return {
        "txt": extract_txt_to_df(container_talent),
        "applicants_csv": extract_csv_apps(container_talent),
        "course_behaviours_csv": create_combined_course_behaviours(container_academy),
        "json": extract_json(container_talent),
    }

