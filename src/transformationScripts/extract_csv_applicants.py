from io import StringIO
import pandas as pd
from tqdm import tqdm


def extract_csv_apps(container_client):
    blobs = container_client.list_blob_names()

    dataframes = []
    for filename in tqdm(blobs, desc="Extracting Applicant .csvs"):
        if filename.endswith('Applicants.csv'):
            blob_client = container_client.get_blob_client(blob=filename)
            data = blob_client.download_blob().readall().decode("utf-8")

            df = pd.read_csv(StringIO(data))
            dataframes.append(df)

    return pd.concat(dataframes, ignore_index=True)