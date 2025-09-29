from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
from azure.mgmt.storage import StorageManagementClient
from io import StringIO
import pandas as pd

subscription_id = "cd36dfff-6e85-4164-b64e-b4078a773259"
resource_group = "data503"
location = "uksouth"
storage_account_name = "data503paulastorage"
account_url = f"https://{storage_account_name}.blob.core.windows.net"

#az login in bash
credential = DefaultAzureCredential()

resource_client = ResourceManagementClient(credential, subscription_id)
storage_client = StorageManagementClient(credential, subscription_id)

blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

container_client = blob_service_client.get_container_client('talent')
blobs = container_client.list_blob_names()

def extract():
    dataframes = []
    for filename in blobs:
        if filename.endswith('Applicants.csv'):
            blob_client = container_client.get_blob_client(blob=filename)
            data = blob_client.download_blob().readall().decode("utf-8")

            df = pd.read_csv(StringIO(data))
            dataframes.append(df)

    return pd.concat(dataframes, ignore_index=True)