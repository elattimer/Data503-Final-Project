from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import pandas as pd
from datetime import datetime

subscription_id = "cd36dfff-6e85-4164-b64e-b4078a773259"
resource_group = "data503"
location = "uksouth"
storage_account_name = "data503paulastorage"
account_url = f"https://{storage_account_name}.blob.core.windows.net"

#az login in bash
credential = DefaultAzureCredential()

#Create instance of blob service client class for the specific account and user credentials
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)



# Get the client for the container from blob_service_client
container_talent = blob_service_client.get_container_client("talent")
container_academy = blob_service_client.get_container_client("academy")

from transformationScripts.extract_txt import *
from transformationScripts.extract_csv_applicants import *
from transformationScripts.extract_csv_course_behaviours import *
from transformationScripts.extract_json import *

txt_df = extract_txt_to_df(container_talent)
applicants_df = extract_csv_apps(container_talent)
courses_df = create_combined_course_behaviours(container_academy)
json_df = extract_json(container_talent)

print(json_df.head())