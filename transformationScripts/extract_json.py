#pragma once
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
from azure.mgmt.storage import StorageManagementClient
from io import StringIO
import csv
import json


subscription_id = "cd36dfff-6e85-4164-b64e-b4078a773259"
resource_group = "data503"
location = "uksouth"
storage_account_name = "data503paulastorage"
account_url = f"https://{storage_account_name}.blob.core.windows.net"

credential = DefaultAzureCredential()



resource_client = ResourceManagementClient(credential, subscription_id)
storage_client = StorageManagementClient(credential, subscription_id)

container_name = "talent"

#blobs
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

# Get the client for the container
container_client = BlobServiceClient.get_container_client(self = blob_service_client, container=container_name)


for blob in container_client.list_blobs():
    #checks for only json files
    if blob.name.endswith(".json"):

        print(f"Found JSON: {blob.name}")