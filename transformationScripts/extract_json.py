
import pandas as pd
import json
from tqdm import tqdm


def extract_json(container_client):

    dict_df = []
    for blob in tqdm(container_client.list_blobs(), desc="Extracting JSONs"):
        #checks for only json files
        if blob.name.endswith(".json"):
            blob_client = container_client.get_blob_client(blob)
            data = blob_client.download_blob().readall()
            parsed = json.loads(data)
            df = pd.json_normalize(parsed)
            dict_df.append(df)

    combined_df = pd.concat(dict_df, ignore_index=True, sort=False)

    return combined_df
